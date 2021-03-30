import cv2
import numpy as np
import utlis
import pytesseract


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

webcam = False
path = '2.png'
cap = cv2.VideoCapture(0)
cap.set(10,160)
cap.set(3,1920)
cap.set(4,1080)


while True:
    img = cv2.imread(path)

    img, finalCountours = utlis.getContours(img,showCanny=True,draw=True)
    print(pytesseract.image_to_string(img))
    #img = cv2.resize(img,(0,0), None, 0.5, 0.5)
    cv2.imshow('Original',img)
    cv2.waitKey(1)