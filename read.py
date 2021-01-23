import cv2 as cv

#Reading an image
img=cv.imread('img1.png')
cv.imshow('img1',img)
cv.waitKey(0)

#Reading a video
# capture=cv.VideoCapture('dog_video.mp4')

# while True:
#     isTrue, frame=capture.read()

#     cv.imshow('dog_video',frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
   
# capture.release()
# cv.destroyAllWindows()





