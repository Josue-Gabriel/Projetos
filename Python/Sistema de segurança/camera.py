import cv2

class camera():
    def sistema_seguranca(url): #Essa função irá receber o link de acesso a câmera do celular

        #Campo para a definição de variáveis
        gravacao = True #Variável que definira o loop de trocas de câmeras no arquivo layout.py, True indica que o loop continuara, enquanto False indica que a câmera pode ser fechada
        captura = cv2.VideoCapture(url) #Captura os frames da câmera selecionada
        
        while True:
            
            ret, quadro = captura.read() #Efetua a leitura dos frames
            
            if not ret:
                break
            
            cv2.imshow("Gravações", quadro) #Mostra os frames capturados na tela do computador

            #Condição para verificar se a tecla 'q' foi pressionada e fechar a janela e encerra o loop presente no arquivo layout.py
            if cv2.waitKey(1) & 0xFF == ord('q'):
                gravacao = False
                break

            #Condição para verificar se a tecla 'right' (ou no caso a ceta da para a direita do teclado) foi pressionada, e em seguida fechar a janela sem encerrar o loop, para que outra camera seja mostrada
            if cv2.waitKey(5) & 0xFF == 0::
                break

        #Libera os dados pegos e fecha as janelas abertas
        captura.release()
        cv2.destroyAllWindows()

        
        return gravacao
