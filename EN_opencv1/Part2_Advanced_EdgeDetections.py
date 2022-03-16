import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('park.jpg')
cv2.imshow('Original Park',image)
blank=np.zeros(image.shape[:2],dtype='uint8')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray Park',gray)

# Laplacian
laplace=cv2.Laplacian(gray,cv2.CV_64F)
laplace=np.uint8(np.absolute(laplace))
cv2.imshow('Laplacian Park',laplace)

# Sobel Gradian Magnitude Representation
sobel_X=cv2.Sobel(gray,cv2.CV_64F,1,0)
cv2.imshow('Sobel_X Park',sobel_X)
sobel_Y=cv2.Sobel(gray,cv2.CV_64F,0,1)
cv2.imshow('Sobel_Y Park',sobel_Y)

combined_sobel=cv2.bitwise_and(sobel_X,sobel_Y)
cv2.imshow('Combined Sobel_X_Y Park',combined_sobel)

# Canny Edge Detection
canny=cv2.Canny(gray,150,175)
cv2.imshow('Canny Park',canny)







cv2.waitKey(0)