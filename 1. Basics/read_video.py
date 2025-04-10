import cv2 as cv

capture = cv.VideoCapture('Videos/Dog.mp4')

if not capture.isOpened():
    print("Error opening video file")
    exit()

while True:
    isTrue , Frame = capture.read()
    cv.imshow('Video that is displaying' , Frame)

    if cv.waitKey(10) & 0xff == ord(' '):
        break

capture.release()
cv.destroyAllWindows()
