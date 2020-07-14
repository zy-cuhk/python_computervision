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
    # print("points1 is:",points1)
    # print("points number is:",len(points1))
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
    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)

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
    # cv2.imshow('the captured video',img)
    cv2.imshow("the mask",mask)
    cv2.imshow("the res",res)

    print("the contour number is:",len(cnts1))
    if len(cnts1)>=4:
        points=[]
        for i in range(0,4):
            c=cnts1[i]
            M = cv2.moments(c)
            if M["m00"]!=0.0:
                cx= int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                now_central = (cx, cy)
                cv2.circle(img, now_central, 10, (0, 0, 255), -1)
                points.append(int(cx))
                points.append(int(cy))

                if len(points)==8:
                    xlist=[]
                    ylist=[]
                    for i in range(len(points)/2):
                        xlist.append(int(points[2*i]))
                        ylist.append(int(points[2*i+1]))
                    xmin_index=np.array(xlist).argmin()
                    xmax_index=np.array(xlist).argmax()
                    ymin_index=np.array(ylist).argmin()
                    ymax_index=np.array(ylist).argmax()
                    points=np.array(points).reshape(4,2)
                    left_point=(points[xmin_index,0],points[xmin_index,1])
                    right_point=(points[xmax_index,0],points[xmax_index,1])
                    bot_point=(points[ymin_index,0],points[ymin_index,1])
                    top_point=(points[ymax_index,0],points[ymax_index,1])
                    cv2.line(img, left_point, top_point, [0, 255, 0], 2)
                    cv2.line(img, left_point, bot_point, [0, 255, 0], 2)
                    cv2.line(img, right_point, top_point, [0, 255, 0], 2)
                    cv2.line(img, right_point, bot_point, [0, 255, 0], 2)
                    now_central=centroid_computation(points)
                    cv2.circle(img, now_central, 10, (0, 0, 255), -1)
                    area=helen_formula(points)
                    cv2.imshow('the captured video',img)

                    print("now_central is:",now_central)



def show_image(img):
    cv2.imshow('the captured video',img)



def main():
    cap=cv2.VideoCapture(2)
    while(1):
        ret,image=cap.read()
        # image = cv2.imread('image1.jpg')
        print("can video be captured?",ret)
        # show_image(image)
        if ret==True:
            image_process(image)
        else:
            pass
        k=cv2.waitKey(5)&0xFF
        if k==27:
            break
    
if __name__=="__main__":
    main()