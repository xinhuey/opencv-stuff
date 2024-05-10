import cv2 as cv 

#reading the video into the var capture
'''
how videoCapture works:
-it accepts several arguments
-integer argument: the camera index, if you have multiple cameras, you can specify which one to use
e.g : 0 is the webcam, 1 is the 1st camera connected to the computer
-string argument: the path to the video file you want to read
'''
capture = cv.VideoCapture('Videos/dog.mp4')

#use a while loop to read the video frame by frame
while True:
    isTrue, frame = capture.read() #returns a tuple, the first value is a boolean, the second is the frame
    #display the frame
    cv.imshow('Video', frame)

    #stop the video from playing indefinitely
    if cv.waitKey(20) & 0xFF ==ord('d'):
        #if the letter d is pressed, break out of the loop 
        break
capture.release()
cv.destroyAllWindows()

'''
Error received:
cv2.error: OpenCV(4.9.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:971: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'

-opencv could not find the media file at the location specified 
-video ran out of frames, so it cannot find anymore frames  

this also happens if you specify a non-existent file path 
'''

