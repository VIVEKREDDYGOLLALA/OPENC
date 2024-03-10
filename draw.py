import cv2 as cv
import numpy as np 

#blank image
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)

# img= cv.imread('photos\face')

#paint image a certain colour
blank[300:400, 100:200]=0,255,0
cv.imshow('blank',blank)

#draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
cv.imshow('blank',blank)

#draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),50,(255,0,0),thickness=-1)
cv.imshow('blank',blank)

#draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=5)
cv.line(blank,(0,0),(100,250),(255,255,255),thickness=5)
cv.imshow('blank',blank)

#write a text on a image
cv.putText(blank,'fuck you',(0,200),cv.FONT_HERSHEY_COMPLEX,1.0,(255,0,255),2)
cv.imshow('blank',blank)



cv.waitKey(0)