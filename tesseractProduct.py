import cv2 as cv
import numpy as np
import pytesseract

#local onde foi instalado o tesseract
pytesseract.pytesseract.tesseract_cmd = 'local-onde-tesseract-foi-instalado'
img = cv.imread("ROI_1.png")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print("Number of countours = " + str(len(contours)))
print(contours[0])

cv.drawContours(img, contours, 0, (0, 255, 0), 3)

# adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 10)
# thresold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
# thresold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)

#print(pytesseract.image_to_string(mask))


cv.imshow('Result' ,img)
cv.waitKey(0)