import cv2 as cv
import os

relative_image_path = 'opencv-stuff/Photos/cats.jpg'

# Get the absolute path to the image
image_path = os.path.abspath(relative_image_path)

img = cv.imread(image_path)

cv.imshow('Cats', img)

#we smooth the image when there's too much noise 

# Averaging
# The higher kernel size specified, the more blurred the image will be 
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
# More natural than averaging
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur 
#Not meant for high kernel sizes 
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur 
#most popular, bc of how it blurs 
#retains the edges of the image
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)