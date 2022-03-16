import cv2
import numpy as np

image=cv2.imread('cats.jpg')
cv2.imshow('Cats',image)

# blank=np.zeros(image.shape[:2],dtype='uint8') # image.shape[:2] : same dimensions with original cat images
# cv2.imshow('Blank',blank)
blank=np.zeros(image.shape,dtype='uint8') # image.shape[:2] : same dimensions with original cat images
#cv2.imshow('Blank',blank)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Cats',gray)

blur=cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow('Blur Cats',blur)

# ctrl+ö hızlı comment
blankCanny=np.zeros(image.shape,dtype='uint8') # image.shape[:2] : same dimensions with original cat images
canny=cv2.Canny(image,125,175)
cv2.imshow('Canny Edges Cats',canny)
contoursCanny,hierarchiesCanny=cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contoursCanny)} contour(s) found Canny !')
cv2.drawContours(blankCanny,contoursCanny,-1,(0,0,255),1)
cv2.imshow('ContoursCanny Drawn with Red',blankCanny)

blankThresh=np.zeros(image.shape,dtype='uint8') # image.shape[:2] : same dimensions with original cat images
ret,thresh=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
cv2.imshow('Threshold',thresh)
contoursThresh,hierarchies2=cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contoursThresh)} contour(s) found Thresh !')
cv2.drawContours(blankThresh,contoursThresh,-1,(0,0,255),1)
cv2.imshow('ContoursThresh Drawn with Red',blankThresh)

blankBlur=np.zeros(image.shape,dtype='uint8') # image.shape[:2] : same dimensions with original cat images
cannyBlur=cv2.Canny(blur,125,175)
cv2.imshow('Canny Blur Edges Cats',cannyBlur)
contoursBlur,hierarchiesBlur=cv2.findContours(cannyBlur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contoursBlur)} contour(s) found Canny Blur!')
cv2.drawContours(blankBlur,contoursBlur,-1,(255,0,0),1)
cv2.imshow('ContoursBlur Drawn with Blue',blankBlur)











cv2.waitKey(0)
