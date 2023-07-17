import cv2

class camera():
    def sistema_seguranca(url):

        gravacao = True
        camera = url
        captura = cv2.VideoCapture(camera)
        
        while True:
            
            ret, quadro = captura.read()
            
            if not ret:
                break
            
            cv2.imshow("Gravações", quadro)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                gravacao = False
                break
            
            click = cv2.waitKey(5) & 0xFF
            
            if click == 0:
                break
        
        captura.release()
        cv2.destroyAllWindows()

        return gravacao
