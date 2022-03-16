import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('cats.jpg')
cv2.imshow('Original Cats',image)

blank=np.zeros(image.shape[:2],dtype='uint8')

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray Cats',gray)

maskCircle=cv2.circle(blank.copy(),(image.shape[1]//2,image.shape[0]//2),100,125,-1)
#cv2.imshow('MaskCircle Cats',maskCircle)

GrayMaskedCircle=cv2.bitwise_and(gray,gray,mask=maskCircle.copy())
cv2.imshow('MaskCircle GRAY Cats',GrayMaskedCircle)

# Gray Scale Histogram
#gray_hist=cv2.calcHist([gray],[0],None,[256],[0,256])
# gray_hist=cv2.calcHist([gray],[0],GrayMaskedCircle,[256],[0,256])
gray_hist=cv2.calcHist([gray],[0],maskCircle,[256],[0,256])
plt.figure()
plt.title('Gray Scale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# Color Scale Histogram
maskedCircle=cv2.bitwise_and(image,image,mask=maskCircle)
cv2.imshow('MaskCircle RGB Color Cats',maskedCircle)

colors=('blue','green','red')
plt.figure()
for i,column in enumerate(colors):
    # hist=cv2.calcHist([image],[i],None,[256],[0,256]) # all image area
    hist=cv2.calcHist([image],[i],maskCircle,[256],[0,256]) # particular mask area
    plt.title('RGB Color Scale Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.plot(hist,color=column)
    plt.xlim([0,256])
    plt.legend(['BLUE','GREEN','RED'])
plt.show()









cv2.waitKey(0)