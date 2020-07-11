# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 20:25:00 2014
@author: duan
"""
import cv2
import numpy as np
import imutils

def cal_distance(point1, point2):
    dis = np.sqrt(np.sum(np.square(point1[0] - point2[0]) + np.square(point1[1] - point2[1])))
    return dis

def helen_formula(coord):
    coord = np.array(coord).reshape((4, 2))
    dis_01 = cal_distance(coord[0], coord[1])
    dis_12 = cal_distance(coord[1], coord[2])
    dis_23 = cal_distance(coord[2], coord[3])
    dis_13 = cal_distance(coord[1], coord[3])
    dis_30 = cal_distance(coord[3], coord[0])
    p1 = (dis_01 + dis_30 + dis_13) * 0.5
    p2 = (dis_12 + dis_23 + dis_13) * 0.5
    area1 = np.sqrt(p1 * (p1 - dis_01) * (p1 - dis_30) * (p1 - dis_13))
    area2 = np.sqrt(p2 * (p2 - dis_12) * (p2 - dis_23) * (p2 - dis_13))
    return (area1 + area2) / 2

def centroid_computation(points):
    points1=points.reshape(4,2)
    print("points1 is:",points1)
    print("points number is:",len(points1))
    sum_x=0
    sum_y=0
    for i in range(len(points1)):
        sum_x+=points1[i,0]
        sum_y+=points1[i,1]
    cx=int(sum_x/len(points1))
    cy=int(sum_y/len(points1))
    now_central = (cx, cy)
    return now_central

def image_process(img):
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)

    # point contour extraction
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_red=np.array([0,50,50])
    upper_red=np.array([10,255,255])
    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(img,img,mask=mask)
    mask1=mask.copy()
    cnts = cv2.findContours(mask1, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts1=sorted(cnts,key=cv2.contourArea,reverse=True)
    for i in range(len(cnts1)):
        print("the area is:",cv2.contourArea(cnts1[i], True))

    # points feature computation 
    points=np.zeros(8)
    for i in range(0,4):
        c=cnts1[i]
        # print("c is:",c)
        M = cv2.moments(c)
        cx= int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        now_central = (cx, cy)
        cv2.circle(img, now_central, 10, (0, 0, 255), -1)
        points[2*i]=cx
        points[2*i+1]=cy

    # central point computation
    now_central=centroid_computation(points)
    print("now central is:",now_central)
    cv2.circle(img, now_central, 10, (0, 0, 255), -1)
    area=helen_formula(points)
    print("area is:",area)

    cv2.imshow('image',img)

# k = cv2.waitKey(0)
# if k == 27: 
#     cv2.destroyAllWindows()
# print("length of cnts is:",len(cnts))


cap=cv2.VideoCapture(0)
while(1):
    ret,image=cap.read()
    image_process(image)

    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
