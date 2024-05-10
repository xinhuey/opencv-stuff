import cv2 as cv

img = cv.imread('Photos/park.jpg')

cv.imshow('Cat', img)

#convert to a grayscale image 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur an image 
'''
removes noise from an image 
e.g bad lighting, camera sensor issues
'''
#using gaussian blur 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) 
#increase the kernel size (second argument) to increase the blur
cv.imshow('Blur', blur)

#Edge cascade
#create a structuring element
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

#Dilate the image using a specific structuring element 
dilated = cv.dilate(canny, (3,3), iterations = 1)
cv.imshow('Dilated', dilated)

#Eroding 
#erodes away the boundaries of foreground object
eroded = cv.erode(dilated, (3,3), iterations = 1)
cv.imshow('Eroded', eroded)

#resize 
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resize)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)