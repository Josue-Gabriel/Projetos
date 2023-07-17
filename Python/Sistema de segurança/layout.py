import PySimpleGUI as sg
from camera import camera
from detector_de_movimento import detector_de_movimento

lista_de_cameras = []
camera_selecionada = 0
gravacao = True
detecção = False

sg.theme("DarkPurple")

layout = [
    [sg.Text("Sistema de segurança", key="mensagem")],
    [sg.Input('0.0.0.0:8080', key="cam", size=(55,1))],
    [sg.Button("Iniciar"), sg.Button("Adicionar câmera"), sg.Button("WebCam", key="webcam"), sg.Button("Detector de movimento", key="detector")],
    [sg.Text("", key='cameras')]
]

janela = sg.Window("", layout)

while True:
    acao, valor = janela.read()
    if acao == sg.WINDOW_CLOSED:
        break
    if acao == "Adicionar câmera":
        ip_endress = valor['cam']
        id_camera = f"http://{ip_endress}/video" 
        lista_de_cameras.append(id_camera)
        janela['cameras'].update("Câmera adicionada: " + id_camera)
    if acao == "Iniciar":
        if detecção == False:
            try:
                url = lista_de_cameras[camera_selecionada]
                quantia_de_cameras = len(lista_de_cameras)
                while gravacao == True:
                    gravacao = camera.sistema_seguranca(url)
                    camera_selecionada += 1
                    if camera_selecionada == quantia_de_cameras:
                        camera_selecionada = 0
                    url = lista_de_cameras[camera_selecionada]
                gravacao = True
                janela["cameras"].update("")
            except:
                janela['mensagem'].update("Camera não encontrada")
                lista_de_cameras = []
                janela["cameras"].update("")
        else:
            try:
                url = lista_de_cameras[camera_selecionada]
                quantia_de_cameras = len(lista_de_cameras)
                while gravacao == True:
                    gravacao = detector_de_movimento.detector(url)
                    camera_selecionada += 1
                    if camera_selecionada == quantia_de_cameras:
                        camera_selecionada = 0
                    url = lista_de_cameras[camera_selecionada]
                gravacao = True
                janela["cameras"].update("")
            except:
                janela['mensagem'].update("Camera não encontrada")
                lista_de_cameras = []
                janela["cameras"].update("")

    if acao == "webcam":
        url = 0
        if detecção == False:
            camera.sistema_seguranca(url)
        else: 
            detector_de_movimento.detector(url)
        
    if acao == "detector":
        if detecção == False:
            detecção = True
        else:
            detecção = False
                
