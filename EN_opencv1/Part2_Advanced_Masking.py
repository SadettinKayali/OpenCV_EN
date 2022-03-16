#ls ,  chdir Python_openCV_ImageProcessing_Youtube/freeCodeCamp_OPENCV/Resources/Photos
import cv2
import numpy as np

image=cv2.imread('cats 2.jpg')
cv2.imshow('Original Cats',image)

blank=np.zeros(image.shape[:2],dtype='uint8')
#cv2.imshow('Blank Image',blank)
maskCircle=cv2.circle(blank.copy(),(image.shape[1]//2,image.shape[0]//2),100,255,-1)
#cv2.imshow('Circle Mask',maskCircle)
maskedCircle=cv2.bitwise_and(image,image,mask=maskCircle)
cv2.imshow('Circle Mask Cats',maskedCircle)

maskRectangle=cv2.rectangle(blank.copy(),(image.shape[1]//2,image.shape[0]//2),(image.shape[1]//2+100,image.shape[0]//2+100),255,-1)
#cv2.imshow('Circle Mask',maskRectangle)
maskedRectangle=cv2.bitwise_and(image,image,mask=maskRectangle)
cv2.imshow('Rectangle Mask Cats',maskedRectangle)

mask_weird_shape=cv2.bitwise_and(maskCircle,maskRectangle)
masked_weird_shape=cv2.bitwise_and(image,image,mask=mask_weird_shape)
cv2.imshow('Weird Shaped Masked Image',masked_weird_shape)

cv2.waitKey(0)