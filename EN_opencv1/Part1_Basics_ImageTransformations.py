import cv2
import numpy as np
image=cv2.imread('park.jpg')
cv2.imshow('Boston park Original',image)

# Translation
def translate(image,x,y):
    translationMatrix=np.float32([[1,0,x],[0,1,y]])
    dimensions=(image.shape[1],image.shape[0])
    return cv2.warpAffine(image,translationMatrix,dimensions)
# -x : left , -y : up , x : right , y : down
translated=translate(image,100,100) # translate(image,x,y)
cv2.imshow('Translated',translated)

# Rotation
def rotate(image,angle,rotationPoint=None):
    (height,width)=image.shape[:2]
    
    if rotationPoint is None:
        rotationPoint=(width//2,height//2)
    rotationMatrix=cv2.getRotationMatrix2D(rotationPoint,angle,1.0)
    dimensions=(width,height)

    return cv2.warpAffine(image,rotationMatrix,dimensions)

rotated=rotate(image,45) # rotate(image,CW or CCW)  CW : + angle CCW : - angle 
cv2.imshow('Rotated',rotated)

rotated_rotated=rotate(rotated,-45)
cv2.imshow('Rotated rotated',rotated_rotated)

# Resizing
resized=cv2.resize(image,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized',resized)

# Flipping
flip0=cv2.flip(image,0)
cv2.imshow('Flip 0 _ Vertical ',flip0)

flip1=cv2.flip(image,1)
cv2.imshow('Flip 1 _ Horizontal ',flip1)

# Cropping
cropped=image[300:600,400:800]
cv2.imshow('Cropped ',cropped)













cv2.waitKey(0)
if cv2.waitKey(20) & 0xFF==ord('q'):
    cv2.destroyAllWindows()