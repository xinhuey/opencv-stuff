import cv2 as cv
import numpy as np
img = cv.imread('Photos/park.jpg')

cv.imshow('Boston', img)

#Translation 
def translate(img, x, y):
    '''
    x, y: # of pixels that you want to shift the image on the x and y axis 
    '''
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up 
#x --> right
#y --> down 

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

#rotation 
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None: #if the rotation point is not specified 
        rotPoint = (width//2, height//2) #rotate about centre 

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('rotate', rotated)

cv.waitKey(0)