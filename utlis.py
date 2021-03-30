import cv2
import numpy as np
from numpy.lib.function_base import append


def getContours(img,cThr=[100,100],showCanny=False,minArea=1000,filter=0,draw=False):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
    imgCanny = cv2.Canny(imgBlur,cThr[0],cThr[1])
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernel,iterations=1)
    imgThre = cv2.erode(imgDial,kernel, iterations=1)

    if showCanny:cv2.imshow('Canny',imgThre)
    contours,hiearchy = cv2.findContours(imgThre,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    finalCountours = []
    for i in contours:
        area = cv2.contourArea(i)
        if area > minArea:
            peri = cv2.arcLength(i,True)
            aprox = cv2.approxPolyDP(i,0.02*peri, True)
            bbox = cv2.boundingRect(aprox)
            if filter > 0:
                if len(aprox) == filter:
                    finalCountours.append([len(aprox),area,aprox,bbox,i])
            else:
                finalCountours.append([len(aprox),area,aprox,bbox,i])
    finalCountours = sorted(finalCountours,key = lambda x:x[1], reverse=True)

    if draw:
        for con in finalCountours:
            cv2.drawContours(img,con[4],-1,(0,0,255),3)
    
    return img, finalCountours
