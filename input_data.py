from PIL import ImageGrab
import numpy as np
import cv2
import time
import datetime
import keyboard

def keysOutput():

    output = [0, 0, 0, 0, 0, 0, 0, 0, 0] # w,a,s,d,wa,wd,sa,sd,nk

    if keyboard.is_pressed("w") and keyboard.is_pressed("a"):
        output[4] = 1
    elif keyboard.is_pressed("w") and keyboard.is_pressed("d"):
        output[5] = 1
    elif keyboard.is_pressed("s") and keyboard.is_pressed("a"):
        output[6] = 1
    elif keyboard.is_pressed("s") and keyboard.is_pressed("d"):
        output[7] = 1
    elif keyboard.is_pressed("w"):
        output[0] = 1
    elif keyboard.is_pressed("a"):
        output[1] = 1
    elif keyboard.is_pressed("s"):
        output[2] = 1
    elif keyboard.is_pressed("d"):
        output[3] = 1
    else:
        output[8] = 1
        
    return output




def screen_data():
        curr_frame += 1
        start_time = time.time()
        img = ImageGrab.grab(bbox=(1430, 96, 2266, 565)) #bbox specifies specific region (bbox= x,y,width,height *starts top-left)
        img_np = np.array(img) #this is the array obtained from conversion
        frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
        np.append(frame, frames)
        cv2.imshow("GameView", frame)

        time_passed = time.time() - start_time
        fps = 1/time_passed
        print(f"FPS: {fps}")

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break

recorded_frames = np.array([])
frames = np.array([])
curr_frame = 0
while True:
    keyboard_output = keysOutput()

    complete_output = np.array([])