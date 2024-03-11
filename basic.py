import cv2 as cv
img=cv.imread('photos\park.jpg')
cv.imshow('park',img)

#converting to greyscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#blur
blur=cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
cv.imshow('gray blur',blur)

#edge cascade
canny=cv.Canny(img,125,175)
cv.imshow('canny',canny)

#Dilating the images
dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dilate',dilated)

#eroding
eroded=cv.erode(dilated,(7,7),iterations=1)
cv.imshow('eroded',eroded)

#Resize
resized=cv.resize(img,(1500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

#cropping
cropped=img[50:200,200:400]
cv.imshow('cropped',cropped)
cv.waitKey(0)