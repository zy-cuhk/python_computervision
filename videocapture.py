# -*- coding: utf-8 -*-
"""
3 Created on Fri Jan 3 21:06:22 2014
4
5 @author: duan
6 """

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# while(True):
# Capture frame-by-frame

flag=cap.isOpened()
print("the camera is open or not:",flag)

ret, frame = cap.read()
# if ret!=True:
#     break
# Our operations on the frame come here
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Display the resulting frame
cv2.imshow('frame',gray)
# if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

# When everything done, release the capture
# cap.release()
cv2.destroyAllWindows()