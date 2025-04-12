import cv2 as cv

img = cv.imread('../Resources/Photos/cat.jpg')
cv.imshow('Original Image' , img)

def rescale_image(frame , scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width , height)
    return cv.resize(frame , dimensions , interpolation = cv.INTER_AREA) # use INTER_AREA for shrinking and INTER_LINEAR or INTER_CUBIC for enlarging

Rescaled_image = rescale_image(img)
cv.imshow("Rescaled image" , Rescaled_image)

cv.waitKey(0)
