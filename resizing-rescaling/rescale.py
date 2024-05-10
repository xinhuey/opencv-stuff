'''
generally a good practice to rescale the image to a size that fits your screen

'''
import cv2 as cv 

#rescaling images 
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale= 0.75):
    #works for images, video, and live video
    #converting from a floating point to an int 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def changeRes(width, height):
    #only works for live video
    capture.set(3, width)
    capture.set(4, height)


cv.imshow('Cat Resized', rescaleFrame(img, scale = 0.2))

capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read() #returns a tuple, the first value is a boolean, the second is the frame
    frame_resized = rescaleFrame(frame, scale =.2)
    #display the frame
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    #stop the video from playing indefinitely
    if cv.waitKey(20) & 0xFF ==ord('d'):
        #if the letter d is pressed, break out of the loop 
        break
capture.release()


cv.destroyAllWindows()