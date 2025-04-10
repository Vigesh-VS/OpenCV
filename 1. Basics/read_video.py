import cv2 as cv

capture = cv.VideoCapture('../Resources/Videos/Dog.mp4')

if not capture.isOpened():
    print("Error opening video file")
    exit()

while True:
    isTrue , Frame = capture.read()
    cv.imshow('Video is Playing' , Frame)

    if cv.waitKey(10) & 0xff == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
