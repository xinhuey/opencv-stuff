import cv2 as cv

#reading the image into the var img 
img = cv.imread('cat.jpg',0)

'''
-the image goes offscreen 
this line will display the large image, but opencv does not have a way to rescale the image to suit the dimensions 
of your computer screen
so you would need to get a display large enough to see the entire image 
'''
#img = cv.imread('Photos/cat_large.jpg')


#displays the image as a new window 
#imshow(name, pixels)
cv.imshow('Cat', img)

#keyboard binding function, delay in waiting for a key to be pressed 
cv.waitKey(0)