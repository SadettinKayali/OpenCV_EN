import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('cats.jpg')
cv2.imshow('Original Cats',image)
blank=np.zeros(image.shape[:2],dtype='uint8')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Cats',gray)

# SIMPLE THRESHOLDING
threshold,thresh=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
cv2.imshow('Simple Thresholded Cats',thresh)
threshold_inv,thresh_inv=cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Simple Inverse Thresholded Cats',thresh_inv)

# Adaptive Thresholding
thresh_adaptive=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)
cv2.imshow('Simple Adaptive Thresholded Cats',thresh_adaptive)

thresh_inv_adaptive=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,3)
cv2.imshow('Simple Adaptive Inverse Thresholded Cats',thresh_inv_adaptive)











cv2.waitKey(0)