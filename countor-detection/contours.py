'''
countors are boundaries of objects 
line occurred that joins the points along the boundaries of an object 
contours are useful in shape analysis, object detection and recognition 
'''

import cv2 as cv 
import numpy as np 

img= cv.imread('Photos/cats.jpg')

cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

'''blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#grab the edges of the image using the canny detector 
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)'''

#thresholding
#tries to binalise the pixel if the pixel is below 125 it will be black, if it is above 125 it will be white
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

#findContours
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

#draw the contours on the blank image
#-1 for drawing all contours 
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)

'''
canny -> find contours
rather than thresholding 
'''