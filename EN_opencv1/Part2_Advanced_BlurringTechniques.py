# Smoothing
import cv2

image=cv2.imread('cats.jpg')
cv2.imshow('Original Cats',image)

# Average Blur
averageBlur=cv2.blur(image,(3,3)) # (,) : kernel size
cv2.imshow('Average Blur',averageBlur)

# Gaussian Blur
gaussBlur=cv2.GaussianBlur(image,(3,3),1)
cv2.imshow('Gaussian Blur',gaussBlur)

# Median Blur
medianBlur=cv2.medianBlur(image,3)
cv2.imshow('Median Blur',medianBlur)

# Blateral Blur
bilateralBlur=cv2.bilateralFilter(image,5,15,15)
cv2.imshow('Bilateral Blur',bilateralBlur)





















cv2.waitKey(0)