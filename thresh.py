import cv2 as cv
import numpy as np
import pytesseract


pytesseract.pytesseract.tesseract_cmd = 'local-onde-tesseract-foi-instalado'

img = cv.imread('database/VINEGAR/VINEGAR0004.png')
cv.imshow('Original', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

thresold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
cv.imshow('Simple Thresholded', thresh)

thresold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 10)
cv.imshow('adap', adaptive_thresh)


mask = cv.rectangle(blank.copy(), (70,70), (180,180), 255, -1)
masked = cv.bitwise_and(thresh, thresh, mask=mask)
cv.imshow('Bitwises', masked)

print(pytesseract.image_to_string(adaptive_thresh))


cv.waitKey(0)