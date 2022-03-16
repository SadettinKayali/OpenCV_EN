import cv2 
import numpy as np
from matplotlib import pyplot as plot

image=cv2.imread('park.jpg')
cv2.imshow('Park Original ',image)

# BGR to RGB
rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.imshow('BGR to RGB Park',rgb)

# BGR to Gray
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR to Gray Park',gray)

# BGR to HSV
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('BGR to HSV Park',hsv)

# HSV to BGR
hsv_bgr=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
cv2.imshow('HSV to BGR',hsv_bgr)

# BGR to L*a*b
lab=cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
cv2.imshow('BGR to L*a*b Park',lab)

# L*a*b to BGR
lab_bgr=cv2.cvtColor(lab,cv2.COLOR_LAB2BGR)
cv2.imshow('L*a*b to BGR',lab_bgr)















cv2.waitKey(0)


"""
titlelist=["IMAGE","IMAGE_Gray","IMAGE_HSV","IMAGE_L*a*b"]
imagelist=[image,gray,hsv,lab]


for i in range(len(imagelist)):
    plot.subplot(1,len(imagelist),i+1)
    plot.imshow(imagelist[i],"gray",vmin=0,vmax=255)
    plot.title(titlelist[i])
    plot.xticks([]),plot.yticks([])

#plot.imshow(image)
#plot.imshow(gray_scale)
plot.show()

"""