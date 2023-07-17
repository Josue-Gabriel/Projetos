import cv2
import pyttsx3

class detector_de_movimento():
    def detector(url):
        captura = cv2.VideoCapture(url)
        subtracao_fundo = cv2.createBackgroundSubtractorMOG2()
        robo = pyttsx3.init()
        deteccao = 0
        gravacao = True

        while True:
            
            _, frame_inicial = captura.read()

            mascara = subtracao_fundo.apply(frame_inicial)
            dados = str(mascara)
            dados = list(dados)
            dados = dados[6]
            if dados != "0" and deteccao < 2:
                deteccao += 1
                if deteccao == 2:
                    robo.say("Movimento detectado!")
                    robo.runAndWait()
                    cv2.imwrite('D:\Python\captura.jpg', frame_inicial)

            cv2.imshow("Máscara de Movimento", frame_inicial)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                gravacao = False
                break
            
            click = cv2.waitKey(5) & 0xFF
            
            if click == 0:
                break

        captura.release()
        cv2.destroyAllWindows()
        
        return gravacao
