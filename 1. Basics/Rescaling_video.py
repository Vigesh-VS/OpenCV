import cv2 as cv

def rescale_video(frame , scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width , height)
    return cv.resize(frame , dimensions , interpolation = cv.INTER_AREA) # use INTER_AREA for shrinking and INTER_LINEAR or INTER_CUBIC for enlarging

capture = cv.VideoCapture('../Resources/Videos/Dog.mp4')

if not capture:
    print("Error opening video file")
    exit()

while True:
    isTrue , frame = capture.read()
    cv.imshow('original Video' , frame)

    rescaled_video = rescale_video(frame)
    cv.imshow('Rescaled Video' , rescaled_video)

    if cv.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv.destroyAllWindows()