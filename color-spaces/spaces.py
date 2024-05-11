import cv2 as cv 
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

#matplotlib will interpret the bgr as rgb colors 
#plt.imshow(img)
#plt.show()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#convert to hsv format (hue saturation value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#lab color space 
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#bgr to rgb 
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

'''
opencv reads in images in BGR format 
'''
cv.waitKey(0)