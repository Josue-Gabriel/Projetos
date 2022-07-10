from asyncio.windows_events import NULL
from json.tool import main
from logging.config import listen
from mimetypes import init
import os
import speech_recognition as sr
import random
import pyttsx3
import pyautogui as au
from datetime import datetime as dt

lista = ['Sim, o que o senhor gostaria', 'Olá, no que posso te ajudar?', 'Sim mestre o que senhor gostaria']
lista_de_palavras = random.choice(lista)

rec = sr.Recognizer()

robo = pyttsx3.init()        

audio = NULL

with sr.Microphone() as mic:
    while True:
        rec.adjust_for_ambient_noise(mic)
        audio = rec.listen(mic)
        text = rec.recognize_google(audio, language="pt-BR", show_all=True)
        if(text == {'alternative': [{'transcript': 'Ok assistente', 'confidence': 0.96170539}], 'final': True}):
            with sr.Microphone() as mix:
                rec.adjust_for_ambient_noise(mix)
                msg_robo = lista_de_palavras
                robo.setProperty("voice", "slovak")
                robo.setProperty("rate", 190)
                robo.setProperty("Volume", 0.3)
                robo.say(msg_robo)
                robo.runAndWait()
                audio = rec.listen(mix)
                text = rec.recognize_google(audio, language="pt-BR", show_all=True)
                if(text == {'alternative': [{'transcript': 'pesquisar', 'confidence': 0.96170539}], 'final': True}):
                    os.startfile(r"") #Caminho do navegador que será usado.
                    with sr.Microphone() as miz:
                        au.sleep(seconds=6.0)
                        rec.adjust_for_ambient_noise(miz)
                        msg_robo = "O que o senhor gostaria de pesquisar?"
                        robo.setProperty("voice", "slovak")
                        robo.setProperty("rate", 190)
                        robo.setProperty("Volume", 0.3)
                        robo.say(msg_robo)
                        robo.runAndWait()
                        audio = rec.listen(miz)
                        text = rec.recognize_google(audio, language="pt-BR")
                        au.hotkey('ctrl', 'e')
                        au.sleep(seconds=0.5)
                        au.write(text)
                        au.sleep(seconds=1.5)
                        au.press("enter")
                elif(text == {'alternative': [{'transcript': 'abrir', 'confidence': 0.96170539}], 'final': True}):
                    with sr.Microphone() as mil:
                        rec.adjust_for_ambient_noise(mil)
                        msg_robo = "O que gostaria de abrir?"
                        robo.setProperty("voice", "slovak")
                        robo.setProperty("rate", 190)
                        robo.setProperty("Volume", 0.3)
                        robo.say(msg_robo)
                        robo.runAndWait()
                        audio = rec.listen(mil)
                        text = rec.recognize_google(audio, language="pt-BR")
                        os.startfile(text)#Somente os arquivos dentro da mesma pasta da assistente serão abertos.
                elif(text == {'alternative': [{'transcript': 'vídeo', 'confidence': 0.96170539}, {'transcript': 'o vídeo'}, {'transcript': 'video'}], 'final': True}):
                    os.startfile(r"")#Caminho do navegador que será usado.
                    au.sleep(seconds = 8.0)
                    au.hotkey('ctrl', 'e')
                    au.sleep(seconds = 1.0)
                    au.write('youtube')
                    au.press('enter')
                    au.sleep(seconds = 5.0)
                    au.press(['tab', 'tab', 'tab', 'tab'])
                    with sr.Microphone() as min:
                        rec.adjust_for_ambient_noise(min)
                        msg_robo = "O que o senhor gostaria de assistir?"
                        robo.setProperty("voice", "slovak")
                        robo.setProperty("rate", 190)
                        robo.setProperty("Volume", 0.3)
                        robo.say(msg_robo)
                        robo.runAndWait()
                        audio = rec.listen(min)
                        text = rec.recognize_google(audio, language="pt-BR")
                        au.write(text)
                        au.press('enter')
                        au.sleep(seconds = 3.0)
                        au.press(['tab'])
                        au.sleep(seconds = 1.0)
                        au.press('enter')
                elif(text == {'alternative': [{'transcript': 'anotação', 'confidence': 0.96170539}, {'transcript': 'a notação'}], 'final': True}):
                        au.press('win')
                        au.sleep(seconds = 1.0)
                        au.write('bloco de notas')
                        au.sleep(seconds = 1.0)
                        au.press('enter')
                        with sr.Microphone() as mih:
                            rec.adjust_for_ambient_noise(mih)
                            msg_robo = "Pode falar"
                            robo.setProperty("voice", "slovak")
                            robo.setProperty("rate", 190)
                            robo.setProperty("Volume", 0.3)
                            robo.say(msg_robo)
                            robo.runAndWait()
                            audio = rec.listen(mih)
                            text = rec.recognize_google(audio, language="pt-BR")
                            au.write(text)
                            au.sleep(seconds = 1.5)
                            au.hotkey('ctrl', 's')
                            au.sleep(seconds = 1.5)
                            au.press(['tab', 'tab', 'tab', 'tab'])
                            au.sleep(seconds = 2.0)
                            au.press('enter')
                elif(text == {'alternative': [{'transcript': 'Que horas são', 'confidence': 0.96170539}, {'transcript': 'o que horas são'}, {'transcript': 'a que horas são'}], 'final': True}):
                    msg_robo = dt.now().time.strftime('%H:%M')
                    robo.setProperty("voice", "slovak")
                    robo.setProperty("rate", 190)
                    robo.setProperty("Volume", 0.3)
                    robo.say(msg_robo)
                    robo.runAndWait()
        elif(text == {'alternative': [{'transcript': 'Pausar vídeo', 'confidence': 0.96170539}], 'final': True}):
            au.press('space')
        elif(text == {'alternative': [{'transcript': 'despausar', 'confidence': 0.96170539}], 'final': True}):
            au.press('space')
        elif(text == {'alternative': [{'transcript': 'descansar', 'confidence': 0.96170539}], 'final': True}):
            msg_robo = 'Ok, se precisar de algo estarei aqui'
            robo.setProperty("voice", "slovak")
            robo.setProperty("rate", 190)
            robo.setProperty("Volume", 0.3)
            robo.say(msg_robo)
            robo.runAndWait()
            
            