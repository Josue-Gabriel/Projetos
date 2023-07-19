import cv2
import pyttsx3

class detector_de_movimento():
    def detector(url):
        
        #Campo para a definição de variáveis
        captura = cv2.VideoCapture(url) #Captura os frames da câmera selecionada
        subtracao_fundo = cv2.createBackgroundSubtractorMOG2() #Efetua a subtração do fundo dos frames capturados
        robo = pyttsx3.init()
        deteccao = 0
        gravacao = True #Variável que definira o loop de trocas de câmeras no arquivo layout.py, True indica que o loop continuara, enquanto False indica que a câmera pode ser fechada

        while True:
            
            _, frame_inicial = captura.read() #Efetua a leitura dos frames

            mascara = subtracao_fundo.apply(frame_inicial) #Adiciona como mascara nos frames pegos o variável subtracao_fundo
            
            #Leitura dos dados para determinar se houve movimentação proxima da câmera ou não
            dados = str(mascara)
            dados = list(dados)
            dados = dados[6]
            if dados != "0" and deteccao < 2:
                deteccao += 1 #Váriavel que determinara quantas vezes o alerta será soado
                if deteccao == 2:
                    robo.say("Movimento detectado!") #Alerta de movimentação
                    robo.runAndWait()
                    cv2.imwrite('D:\Python\captura.jpg', frame_inicial) #Pasta onde será salva o frame pego após a detecção de movimentos

            cv2.imshow("Máscara de Movimento", frame_inicial) #Mostra os frames capturados na tela do computador

            #Condição para verificar se a tecla 'q' foi pressionada e fechar a janela e encerra o loop presente no arquivo layout.py
            if cv2.waitKey(1) & 0xFF == ord('q'):
                gravacao = False
                break

            #Condição para verificar se a tecla 'right' (ou no caso a ceta da para a direita do teclado) foi pressionada, e em seguida fechar a janela sem encerrar o loop, para que outra câmera seja mostrada
            if click = cv2.waitKey(5) & 0xFF == 0:
                break

        #Libera os dados pegos e fecha as janelas abertas
        captura.release()
        cv2.destroyAllWindows()
        
        return gravacao
