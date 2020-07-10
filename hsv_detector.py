# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 20:25:00 2014
@author: duan
"""
import cv2
import numpy as np
import imutils
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
img = cv2.imread('image1.jpg')
# print("img is:",img)


hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_blue=np.array([0,50,50])
upper_blue=np.array([10,255,255])
mask=cv2.inRange(hsv,lower_blue,upper_blue)
res=cv2.bitwise_and(img,img,mask=mask)

mask1=mask.copy()
cnts = cv2.findContours(mask1, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

list1=sorted(cnts,key=cv2.contourArea,reverse=True)
for i in range(len(list1)):
    print("the area is:",cv2.contourArea(list1[i], True))

for i in range(0,3):
    c=list1[i]
    print("the maximum area is:",cv2.contourArea(c, True))
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])
    font = cv2.FONT_HERSHEY_SIMPLEX
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    now_central = (cX, cY)
    cv2.circle(img, now_central, 10, (0, 0, 255), -1)

cv2.imshow('image',img)
# cv2.imshow("mask",mask)
# cv2.imshow("mask1",mask1)
# cv2.imshow('res',res)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
print("length of cnts is:",len(cnts))

# cap=cv2.VideoCapture(0)
# while(1):
#     # 获取每一帧
#     ret,frame=cap.read()
#     # 转换到 HSV
#     hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     # 设定蓝色的阈值
#     lower_blue=np.array([0,50,50])
#     upper_blue=np.array([10,255,255])
#     # 根据阈值构建掩模
#     mask=cv2.inRange(hsv,lower_blue,upper_blue)
#     # 对原图像和掩模进行位运算
#     res=cv2.bitwise_and(frame,frame,mask=mask)
#     # 显示图像
#     cv2.imshow('frame',frame)
#     cv2.imshow('mask',mask)
#     cv2.imshow('res',res)
#     k=cv2.waitKey(5)&0xFF
#     if k==27:
#         break
# # 关闭窗口
# cv2.destroyAllWindows()

