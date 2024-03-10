import cv2 as cv
# read images
# img=cv.imread('photos/cat_large.jpg')
# cv.imshow('large',img)
# cv.waitKey(0)



#read videos
capture=cv.VideoCapture('videos\dog.mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
