# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 19:16:05 2013
@author: duan
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load an color image in grayscale
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
img = cv2.imread('image1.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite("image2.png",img)
    cv2.destroyAllWindows()
# cv2.imwrite("image2.png",img)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()

