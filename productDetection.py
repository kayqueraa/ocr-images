import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = 'local-onde-tesseract-foi-extraido'

img = cv2.imread('DATABASE PANTHER/MILK/MILK0000.png')
cv2.imshow('Original', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow('Blank', blank)

circle = cv2.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv2.imshow('Mask', circle)

rectangle = cv2.rectangle(blank.copy(), (60,20), (165,160), 255, -1)

weird_shape = cv2.bitwise_and(circle, rectangle)
cv2.imshow('Weird Shape', weird_shape)

masked = cv2.bitwise_and(img, img, mask=weird_shape)
cv2.imshow('Bitwise AND', masked)

#position = (81,54)(163,54) - (163,150)(150,81) img[64:192,0:256]

# rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
# circle = cv2.circle(blank.copy(), (200,200), 200, 255, -1)

# cv2.imshow('Rectangle', rectangle)
# cv2.imshow('Circle', circle)

# bitwise_and = cv2.bitwise_and(rectangle, circle)
# cv2.imshow('Bitwise AND', bitwise_and)

# bitwise_or = cv2.bitwise_or(rectangle, circle)
# cv2.imshow('Bitwise OR', bitwise_or)

# bitwise_xor = cv2.bitwise_xor(rectangle, circle)
# cv2.imshow('Bitwise XOR', bitwise_xor)

# bitwise_not = cv2.bitwise_not(rectangle)
# cv2.imshow('Bitwise NOT', bitwise_not)

# average = cv2.blur(img, (3,3))
# #cv2.imshow('Average Blur', average)

# gauss = cv2.GaussianBlur(img, (3,3), 0)
# #cv2.imshow('Gaussian', gauss)

# median = cv2.medianBlur(img, 3)
# #cv2.imshow('Medium Blur', median)

# bilateral = cv2.bilateralFilter(img, 30, 85, 90)
# cv2.imshow('Bilateral', bilateral)

# blank = np.zeros(img.shape[:2], dtype='uint8')

# b,g,r = cv2.split(img)

# blue = cv2.merge([b,blank,blank])
# green = cv2.merge([blank,g,blank])
# red = cv2.merge([blank,blank,r])

# cv2.imshow('Blue', blue)
# cv2.imshow('Green', green)
# cv2.imshow('Red', red)

# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)

# merged = cv2.merge([b,g,r])
# cv2.imshow('Merged', merged)
# plt.imshow(img)
# plt.show()

# blank = np.zeros(img.shape, dtype='uint8')
# cv2.imshow('Blank', blank)

# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray', imgGray)

# imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow('HSV', imgHsv)

# imgLab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# cv2.imshow('LAB', imgLab)

# imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow('RGB', imgRgb)

# hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
# cv2.imshow('HSV --> BGR', hsv_bgr)

# plt.imshow(imgRgb)
# plt.show()


#position = (81,54)(163,54) - (163,150)(150,81)
# imgBlur = cv2.GaussianBlur(imgGray, (5,5), cv2.BORDER_DEFAULT)
# cv2.imshow('Blur', imgBlur)

# imgCanny = cv2.Canny(imgBlur, 125, 175)
# cv2.imshow('Canny', imgCanny)

# # ret, thresh = cv2.threshold(imgGray, 125, 255, cv2.THRESH_BINARY)
# # cv2.imshow('Thresh', thresh)

# countours, hierarchies = cv2.findContours(imgCanny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# print(f'{len(countours)} countour (s) found!')

# cv2.drawContours(blank, countours, -1, (0,0,255), 1)
# cv2.imshow('Contours Drawn', blank)

#imgDilated = cv2.dilate(imgCanny, (7,7), iterations=3)
#cv2.imshow('Dilated', imgDilated)

#imgEroded = cv2.erode(imgDilated, (7,7), iterations=3)
#cv2.imshow('Erode', imgEroded)

#imgResize = cv2.resize(img, (100,100), interpolation=cv2.INTER_CUBIC)
#cv2.imshow('Resize', imgResize)

#imgCrop = img[64:192,0:256]
#cv2.imshow('Cropped', imgCrop)

#print(pytesseract.image_to_string(imgGray))

cv2.waitKey(0)
'''

#imgResize = cv2.resize(img,(256,256))
#print(imgResize.shape)
imgCropped = img[64:192,0:256]
#print(imgCropped.shape)
imgGray = cv2.cvtColor(imgCropped, cv2.COLOR_BGR2GRAY)
print(imgGray.shape)
imgRgb = cv2.cvtColor(imgGray, cv2.COLOR_BGR2RGB)
#cv2.rectangle(img,(0,64),(256,192),(0,0,255),2)
print(pytesseract.image_to_string(img))
    
  

#imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
#imgCanny = cv2.Canny(imgBlur,50,50)
#imgHSV = cv2.cvtColor(imgCropped,cv2.COLOR_BGR2HSV)
#imgRgb = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2RGB)

    
while True:    
    #cv2.imshow("Original",img)
    cv2.imshow("Gray",imgGray)
    cv2.imshow("Image Cropped", imgCropped)
    #cv2.imshow("HSV",imgHSV)
    cv2.imshow("RGB",imgRgb)
    cv2.waitKey(1)
'''

