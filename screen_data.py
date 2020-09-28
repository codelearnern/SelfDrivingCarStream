from PIL import ImageGrab
import numpy as np
import cv2
import time
import datetime



MAX_FRAME = 10000
# MAX_FRAME = 100
FOLDER = "./"

recorded_frames = np.array([])
frames = np.array([])
curr_frame = 0
while True:
  curr_frame += 1
  start_time = time.time()
  img = ImageGrab.grab(bbox=(1430, 96, 2266, 565)) #bbox specifies specific region (bbox= x,y,width,height *starts top-left)
  img_np = np.array(img) #this is the array obtained from conversion
  frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
  np.append(frame, frames)
  cv2.imshow("GameView", frame)

  time_passed = time.time() - start_time
  fps = 1/time_passed
  # print(f"FPS: {fps}")

  if curr_frame % MAX_FRAME == 0:
    np.append(frames, recorded_frames)
    frames = np.array([])
    print("Done recording 10000 frames!")

  if (cv2.waitKey(1) & 0xFF) == ord('q'):
    cv2.destroyAllWindows()
    break