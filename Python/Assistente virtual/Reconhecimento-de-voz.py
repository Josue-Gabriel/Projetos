import PySimpleGUI as sg
import speech_recognition as sr
import pyttsx3
import os
import psutil
import threading
from datetime import datetime
import wikipedia
import mysql.connector
import pyautogui as ag
import time
import pygame

con = mysql.connector.connect(host='localhost', database='agendamento', user='root', password='jo4056')
cursor = con.cursor()

robo = pyttsx3.init()

date = datetime.now()
ano = date.strftime('%y')

robo.say("Inicializando sistemas!")
robo.runAndWait()
robo.say("Olá, mestre!")
robo.runAndWait()

def horas():
    t = date.strftime("%H:%M")
    return t

def voz():
    rec = sr.Recognizer()
    try:
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            audio = rec.listen(mic)
            text = rec.recognize_google(audio, language="pt-BR")
            texto = text.lower()
    except:
        texto = ""    
    return texto

def comando_de_voz():
    comando = voz()
    if "verônica" in comando:
        comando = comando.replace('verônica', '')
        if "horas" in comando:
            robo.say(horas())
            robo.runAndWait()
        elif "dia" in comando:
                robo.say("Bom dia mestre!")
                robo.say("Gostaria de escultar um musica, para começar bem o dia?")
                robo.runAndWait()
                print("pode falar")
                comando = voz()
                if "sim" in comando:
                    os.startfile("Spotify")
                    time.sleep(15)
                    ag.press('space')
        elif "pesquise" in comando:
            robo.say("Pesquisando")
            robo.runAndWait()
            procurar = comando.replace('pesquise', '')
            print(procurar)
            wikipedia.set_lang("pt")
            try:
                resultado = str(wikipedia.summary(procurar,4))
                print(resultado)
                robo.say(resultado)
                robo.say("Gostaria de anotar essa pesquisa")
                robo.runAndWait()
                comando = voz()
                if "sim" in comando:
                    arquivo = open("texto.txt", "a", encoding="utf-8")
                    arquivo.write(resultado)
            except:
                robo.say("Nenhum resultado encontrado")
                robo.runAndWait()
        elif "noite" in comando:
            robo.say("Boa noite mestre!")
            robo.say("Entrando em modo de descanso")
            robo.runAndWait()
            os.system("shutdown /s /t 1")
        elif "bateria" in comando:
            bateria = psutil.sensors_battery()
            porcentual = str(bateria.percent)
            robo.say(porcentual + "porcento")
            robo.runAndWait()
        elif "agendamento" in comando:
            robo.say("O que gostaria de agendar senhor?")
            robo.runAndWait()
            comando = voz()
            mensage = comando
            robo.say("Para que dia?")
            robo.runAndWait()
            comando = voz()
            dia = comando
            robo.say("De que mes?")
            robo.runAndWait()
            comando = voz()
            mes = comando
            data_do_dia = dia + "/" + mes + "/" + ano
            comando = f"INSERT INTO agendar (id, data, mensagem) VALUES (DEFAULT, '{data_do_dia}', '{mensage}');"
            cursor.execute(comando)
            con.commit()
            robo.say("Esta agendado mestre!")
            robo.runAndWait()
        elif "desligar" in comando:
            robo.say("Desligando sistemas")
            robo.runAndWait()
            os.system("shutdown /s /t 1")

while True:
    comando_de_voz()