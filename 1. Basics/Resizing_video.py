import cv2 as cv

capture = cv.VideoCapture('../Resources/Videos/Dog.mp4')

if not capture.isOpened():
    print("Error opening video file")
    exit()

while True:
    isTrue, Frame = capture.read()
    Resized_video = cv.resize(Frame, (500,500))

    cv.imshow('Original video' , Frame)
    cv.imshow('Resized video' , Resized_video)

    if cv.waitKey(10) & 0xff == ord('f'):
        break

capture.release()
cv.destroyAllWindows()