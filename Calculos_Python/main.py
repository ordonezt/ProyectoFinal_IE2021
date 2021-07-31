from serial_com import send_command_to_platform
import numpy as np
import time
import settings
import controller
import GUI
import threading
import cv2
import numpy as np
from pyzbar.pyzbar import decode

import estimador_posicion





def nicos_magic_opencv_function():
    ball_pos=settings.ball_t()
    ball_pos.pos_x=1
    ball_pos.pos_y=0
    return ball_pos

def main():
    settings.init()
    t1=threading.Thread(target=control_loop)
    t2=threading.Thread(target=estimador_posicion.estimar_posicion)
    t1.start()
    t2.start()
    GUI.start_GUI()
    #test_GUI.run_gui()



def control_loop():
    c=controller.controller_t()
    while(True):
        time.sleep(1/30)
        ball_pos = nicos_magic_opencv_function()
        angle_x,angle_y=c.control(settings.ball_pos)
        print(f'angle_x={angle_x}\n')
        print(f'angle_y={angle_y}\n')
        print("envio de comando a la plataforma comentado!")
        #send_command_to_platform("/dev/ttyACM0",angle_x,angle_y,14)


if __name__ == '__main__':
    main()