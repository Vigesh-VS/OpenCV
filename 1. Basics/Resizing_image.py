import cv2 as cv

img = cv.imread("Photos/rose.jpg")
Resized_img = cv.resize(img, (500, 500))

cv.imshow('Resized Image' , Resized_img)
cv.waitKey(0)