import cv2 as cv
img =imread('photos/cats.jpg')
cv.imshow('cats',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)