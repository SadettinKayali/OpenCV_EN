# 5 Essential Functions
import cv2
from cv2 import INTER_AREA

import os 
os.chdir('Python_openCV_ImageProcessing_Youtube\freeCodeCamp_OPENCV/Resources/Photos')
ImageFile = os.path.join(os.path.dirname(__file__), 'Resources/Photos/cat.jpg')
assert os.path.exists(ImageFile)
# ls , chdir 

image=cv2.imread('cat.jpg')

#image=cv2.imread('Resources/Photos/cat.jpg') # Bu bazen çalışmıyor
cv2.imshow('Original Cat',image)

# Converting to grayscale
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Cat',gray)

# Converting to Blur
image2=cv2.imread('park.jpg')
cv2.imshow('Original Park',image2)
blur=cv2.GaussianBlur(image2,(7,7),cv2.BORDER_DEFAULT)
cv2.imshow('Gaussian Blur',blur)

# Edge Cascade
canny2=cv2.Canny(blur,125,175)
cv2.imshow('Canny Edges Park',canny2)

# Dilating the image
dilated=cv2.dilate(canny2,(3,3),iterations=5)
cv2.imshow('Canny Dilated Park',dilated)

# Eroding
eroded=cv2.erode(dilated,(7,7),iterations=5)
cv2.imshow('Eroded Park',eroded)

# Resize
resized=cv2.resize(image,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized Cat',resized)

# Cropping
cropped=image[150:400, 350:600]
cv2.imshow('Crop Cat',cropped)




cv2.waitKey(0)
if cv2.waitKey(20) & 0xFF==ord('q'):
    cv2.destroyAllWindows()