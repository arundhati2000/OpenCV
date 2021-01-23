import cv2 as cv

#For Live videos, standalone images and standalone videos
def rescale_frame(frame,scale=0.20):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#For Live videos only
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


capture=cv.VideoCapture('dog_video.mp4')

while True:
    isTrue, frame=capture.read()

    frame_rescaled=rescale_frame(frame)
    cv.imshow('dog_video', frame_rescaled)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()