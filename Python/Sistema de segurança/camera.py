import cv2
import pyttsx3
import requests
import numpy as np
from layout import janela

#Para se obter a URL, é necessario instalar a aplicação IP Webcam na Play Store, no celular.
#Após isso, certificasse de seu celular e computador estejam conectados a mesma rede.
#Assim que abrir a aplicação vá até a ultima opção e comece a gravar. É possivel conectar mais de uma câmera.

class sistema_de_cameras:
    def cameras(url, numero_da_camera):
        robo = pyttsx3.init()
        numero_da_camera = 0
        bg = cv2.createBackgroundSubtractorMOG2(history=500,varThreshold=100,detectShadows=False)
        detecção = 0
        while True:
            try:
                img_resp = requests.get(url[numero_da_camera])
                img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
                img = cv2.imdecode(img_arr, -1)
                img = cv2.resize(img, (0,0),fx=0.5, fy=0.5)
                cv2.imshow('sem movimentação', img)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                bg_frame=bg.apply(img)
                texto = str(bg_frame)
                lista = list(texto)
                movimentacao = lista[6]
                click = cv2.waitKey(5) & 0xFF
                if movimentacao != '0' and detecção < 2:
                    detecção = detecção + 1
                    if detecção == 2:
                            robo.say("MOVIMENTAÇÃO SUSPEITA DETECTADA")
                            robo.runAndWait()
                            cv2.imwrite('D:\Python\experimento.jpg', img)
                if click == 0:
                    numero_da_camera = 0
                    break
                if click == 27:
                    break
            except:
                numero_da_camera = 0
        
        return click