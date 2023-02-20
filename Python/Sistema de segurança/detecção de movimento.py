import time
from camera import sistema_de_cameras
from layout import janela

url = janela.layout()
numero_da_camera = 0
while True: 
    x = sistema_de_cameras.cameras(url, numero_da_camera)
    time.sleep(1)
    if x == 27:
        break