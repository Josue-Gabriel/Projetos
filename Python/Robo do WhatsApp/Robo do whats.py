#importação das bibliotecas a serem usadas.
import PySimpleGUI as sg
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as ag
from datetime import datetime

#Tema da jenela.
sg.theme("DarkPurple")

#Corpo do layout.
layout = [
    [sg.Text("Robo de envio de mensagem", size=(21,1))],
    [sg.Text("Nome da pessoa/grupo   "), sg.Input(key="Nome",background_color="White",text_color="Black")],
    [sg.Text("Mensagem a ser enviada "), sg.Input(key="Mensagem",background_color="White",text_color="Black")],
    [sg.Text("Horario escolhido para o envio das mensagens"), sg.Input(key="Horario",background_color="White", text_color="Black")],
    [sg.Button("Botão")]
]

janela = sg.Window('', layout)

#Configurações gerais da janela.
while True:
    event, valor = janela.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Botão":
        date = datetime.now()
        hora = date.strftime('%H:%M')
        horario = valor["Horario"]
        name = valor['Nome']
        mensagem = valor['Mensagem']
        lista = name.split()
        n1 = 0
        while hora != horario:
            date = datetime.now()
            hora = date.strftime('%H:%M')
        else:
            driver = webdriver.Edge(EdgeChromiumDriverManager().install()) #Navegador escolhido para uso do WhatsApp Web.
            time.sleep(3)
            driver.get('https://web.whatsapp.com')
            time.sleep(23)
            while (n1 < 30):
                if hora == valor["Horario"]:
                    pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]') #Elementos da pagina a serem usados
                    pesquisa.click()
                    ag.write(lista[n1])
                    ag.press("enter")
                    time.sleep(5)
                    envio = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
                    envio[1].click()
                    ag.write(mensagem)
                    ag.press("enter")
                    n1 = n1 + 1