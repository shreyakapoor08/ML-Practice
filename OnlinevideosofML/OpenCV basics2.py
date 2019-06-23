# we are going to work with python file and read image using opencv and display on screen 
# earlier we used matplotlib to display here we are going to do with opencv only

import cv2

img = cv2.imread('dog.png')
gray = cv2.imread('dog.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Dog Image', img)
# if we use imshow of opencv then it will display rgb image only
# that conversion happens when we read using bgr and display using rgb using matplotlib
cv2.imshow('Gray dog image', gray)

cv2.waitKey(0) #0 means wait for infinite amount of time
#prog will stop is any key is pressed

cv2.destroyAllWindows() #after waiting for infinite time distroy this window