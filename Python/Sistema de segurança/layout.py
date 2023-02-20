import PySimpleGUI as sg

class janela:
    def layout():
        url = []
        ligar = True
        sg.theme("DarkPurple")

        inicialização = [
            [sg.Button("Iniciar"), sg.Button("Adicionar cameras")]
        ]

        adicionar_camera = [
            [sg.Text("Link da camera")],
            [sg.Input(key="camera", size=(20, 20))],
            [sg.Button("Adicionar nova camera")]
        ]

        layout_one = sg.Window('Inicialização', inicialização)
        layout_two = sg.Window('Cameras', adicionar_camera)

        while ligar == True:
            acao, valor = layout_one.read()
            ligar_adicionar = True
            if acao == sg.WINDOW_CLOSED:
                ligar = False
            if acao == "Iniciar":
                ligar = False
            if acao == "Adicionar cameras" and ligar_adicionar == True:
                    acao, valor = layout_two.read()
                    if acao == sg.WINDOW_CLOSED:
                        ligar_adicionar = False
                    if acao == "Adicionar nova camera":
                        camera = valor["camera"]
                        url.append(camera)
        
        return url