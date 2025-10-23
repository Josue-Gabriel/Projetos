"""
envia_whatsapp_use_existing_tab_cc55_simple_wait_random_interval.py

Versão: após abrir a pesquisa/URL do número no navegador, o script
aguarda 5 segundos antes de colar/enviar; entre envios escolhe um intervalo
aleatório entre 1 e 60 segundos.
"""
import os
import re
import csv
import time
import random
import webbrowser
import urllib.parse
import subprocess
import shutil
from datetime import datetime

import pandas as pd
import pyautogui
import pyperclip

# tentativa de import pygetwindow (para focar janelas)
try:
    import pygetwindow as gw
except Exception:
    gw = None

# --------------------------
# CONFIGURAÇÕES
# --------------------------
EXCEL_FILE = r"C:/Users/mixcom/Documents/Robo Whats/lista_clientes.xlsx"
COL_NUMEROS = "numeros"
COL_MENSAGENS = "mensagens"

# Intervalo entre envios: agora aleatório dentro de 1 minuto (1 a 60 segundos)
MIN_WAIT = 1    # segundos (mínimo)
MAX_WAIT = 60   # segundos (máximo)

# Após abrir a pesquisa/URL, aguardar este número de segundos antes de colar/enviar
WAIT_AFTER_SEARCH = 5  # segundos

APP_OPEN_WAIT = 3.5    # (mantido caso queira continuar usando em outros pontos)
POST_PASTE_WAIT = 0.15
LOG_FILE = "log_envios.csv"
MIN_DIGITS_PHONE = 6
MAX_SEND_ATTEMPTS = 2

# Se quiser forçar limpeza do campo antes de colar:
CLEAR_INPUT_BEFORE_PASTE = False

# Adição automática do código do país:
AUTO_ADD_COUNTRY_CODE = True
COUNTRY_CODE = "55"

# Possíveis caminhos do Chrome (caso o fallback precise chamar o executável)
CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]

# Substrings de títulos de janela a procurar (prioriza Chrome e Edge)
BROWSER_TITLE_KEYWORDS = ["Chrome", "Google Chrome", "Edge", "Microsoft Edge", "Brave"]

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.12

# --------------------------
def sanitize_phone(raw):
    """
    Extrai a maior sequência contínua de dígitos do campo raw.
    """
    if raw is None:
        return ""
    s = str(raw).strip()
    if s.lower() in ("nan", "none", ""):
        return ""
    seqs = re.findall(r'\d+', s)
    if not seqs:
        return ""
    seqs_sorted = sorted(seqs, key=lambda x: len(x), reverse=True)
    for seq in seqs_sorted:
        if len(seq) >= MIN_DIGITS_PHONE:
            return seq
    return seqs_sorted[0]

def ensure_country_code(phone):
    """
    Garante que o telefone comece com COUNTRY_CODE.
    Retorna (phone_with_code, added_flag)
    """
    if not phone:
        return phone, False
    if phone.startswith(COUNTRY_CODE):
        return phone, False
    return COUNTRY_CODE + phone, True

def log_entry(number, message, status, note=""):
    exists = os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(["timestamp","number","message_preview","status","note"])
        preview = (message[:120] + "...") if message and len(message) > 120 else (message or "")
        writer.writerow([datetime.now().isoformat(), number, preview, status, note])

def build_wa_me_url(phone):
    return f"https://wa.me/{phone}"

# ---- nova função: abre URL na aba já aberta (se possível) ----
def open_url_in_existing_tab(url, timeout_after_focus=0.3):
    """
    Tenta focar uma janela de navegador já aberta e navegar na aba atual:
      - ativa a janela (pygetwindow) contendo um dos BROWSER_TITLE_KEYWORDS
      - envia Ctrl+L, cola URL e Enter
    Retorna (True,note)
    """
    if gw is None:
        return False, "pygetwindow_not_installed"

    wins = gw.getWindowsWithTitle("")  # retorna todas as janelas
    target = None
    for w in wins:
        title = (w.title or "").lower()
        for key in BROWSER_TITLE_KEYWORDS:
            if key.lower() in title:
                target = w
                break
        if target:
            break

    if not target:
        return False, "browser_window_not_found"

    try:
        target.activate()
        time.sleep(timeout_after_focus)

        # Foca barra de endereço (Ctrl+L) e cola a URL
        if os.name == "posix" and ("darwin" in os.sys.platform):
            pyautogui.hotkey('command', 'l')
        else:
            pyautogui.hotkey('ctrl', 'l')
        time.sleep(1)

        pyperclip.copy(url)
        time.sleep(1)
        if os.name == "posix" and ("darwin" in os.sys.platform):
            pyautogui.hotkey('command', 'v')
        else:
            pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(10)
        return True, "navigated_in_existing_tab"
    except Exception as e:
        return False, f"exception_activating_or_pasting:{e}"

def open_url_direct_fallback(url):
    """
    Fallback: tenta os.startfile / webbrowser / abrir chrome executável.
    """
    try:
        if os.name == "nt":
            os.startfile(url)
            return True, "os_startfile"
    except Exception:
        pass
    try:
        webbrowser.open_new_tab(url)
        return True, "webbrowser"
    except Exception:
        pass
    for chrome_path in CHROME_PATHS:
        if os.path.exists(chrome_path):
            try:
                subprocess.Popen([chrome_path, '--new-tab', url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return True, "chrome_exec"
            except Exception:
                continue
    return False, "all_fallbacks_failed"

def try_send_for_phone(phone, message):
    """
    Abre wa.me/<phone> usando aba existente se possível, aguarda WAIT_AFTER_SEARCH segundos,
    e então cola+enter a mensagem.
    """
    url = build_wa_me_url(phone)
    ok, note = open_url_in_existing_tab(url)
    if not ok:
        ok2, note2 = open_url_direct_fallback(url)
        note = note + ";" + note2 if note2 else note

    # Espera fixa logo após abrir a pesquisa (solicitação do usuário)
    time.sleep(WAIT_AFTER_SEARCH)

    # opcional: limpar campo antes de colar
    if CLEAR_INPUT_BEFORE_PASTE:
        try:
            if os.name == "posix" and ("darwin" in os.sys.platform):
                pyautogui.hotkey('command', 'a')
            else:
                pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.05)
            pyautogui.press('backspace')
            time.sleep(0.05)
        except Exception:
            pass

    pyperclip.copy(message)
    time.sleep(0.08)
    try:
        if os.name == "posix" and ("darwin" in os.sys.platform):
            pyautogui.hotkey('command', 'v')
        else:
            pyautogui.hotkey('ctrl', 'v')
        time.sleep(POST_PASTE_WAIT)
        pyautogui.press('enter')
        return True, note or "sent"
    except Exception as e:
        return False, f"paste_enter_failed:{e}"

def main():
    print("Iniciando (reaproveitar aba aberta -> navegar -> aguardar 5s -> colar -> enter) com COUNTRY_CODE inserido se necessário")
    try:
        df = pd.read_excel(EXCEL_FILE, engine="openpyxl", dtype=str)
    except Exception as e:
        print("Erro ao ler Excel:", e)
        return

    if COL_NUMEROS not in df.columns or COL_MENSAGENS not in df.columns:
        print("ERRO: verifique colunas no Excel.")
        return

    messages_pool = df[COL_MENSAGENS].dropna().astype(str).tolist()
    if not messages_pool:
        print("ERRO: sem mensagens no pool.")
        return

    raw_numbers = df[COL_NUMEROS].astype(str).fillna("").tolist()
    total = len(raw_numbers)
    sent = skipped = errors = 0

    for idx, raw in enumerate(raw_numbers, start=1):
        try:
            print("--------------------------------------------------")
            print(f"[{idx}/{total}] raw: {raw}")
            sanitized = sanitize_phone(raw)
            if not sanitized or len(sanitized) < MIN_DIGITS_PHONE:
                print(f"  -> inválido após sanitização: '{raw}' -> '{sanitized}'. Pulando.")
                log_entry(raw, "", "SKIPPED", "invalid_after_sanitize")
                skipped += 1
                time.sleep(1.0)
                continue

            # garante prefixo do país se necessário
            phone_with_cc = sanitized
            cc_added = False
            if AUTO_ADD_COUNTRY_CODE:
                phone_with_cc, cc_added = ensure_country_code(sanitized)

            message = random.choice(messages_pool).strip()

            note_prefix = "cc_added" if cc_added else ""

            ok, note = try_send_for_phone(phone_with_cc, message)
            full_note = (note_prefix + (";" if note_prefix and note else "") + (note or "")).strip(";")
            if ok:
                print(f"  >> Enviado para {phone_with_cc} ({full_note})")
                log_entry(phone_with_cc, message, "SENT", full_note)
                sent += 1
            else:
                print(f"  !! Falha para {phone_with_cc}: {full_note}")
                log_entry(phone_with_cc, message, "ERROR", full_note)
                errors += 1

        except Exception as e:
            print(f"  !! Erro inesperado ao processar '{raw}': {e}")
            log_entry(raw, "", "ERROR", str(e))
            errors += 1

        # tempo aleatório entre 1 e 60 segundos antes do próximo envio
        wait_seconds = random.randint(MIN_WAIT, MAX_WAIT)
        print(f"  -> Aguardando {wait_seconds} segundos antes do próximo...")
        time.sleep(wait_seconds)

    print("--------------------------------------------------")
    print(f"Finalizado. enviados={sent} | pulados={skipped} | erros={errors}")
    print(f"Log: {os.path.abspath(LOG_FILE)}")

if __name__ == "__main__":
    main()
