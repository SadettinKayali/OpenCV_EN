import cv2
import numpy as np

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv2.rectangle(blank.copy(),(30,30),(370,370),255,-1)
cv2.imshow('Rectangle',rectangle)

circle=cv2.circle(blank.copy(),(200,200),200,255,-1)
cv2.imshow('Circle',circle)

# AND bitwise  : Intersecting Regions
bitwise_and=cv2.bitwise_and(rectangle,circle)
cv2.imshow('Bitwise AND',bitwise_and)

# OR bitwise   : Non-Intersecting Regions + Intersection Regions
bitwise_or=cv2.bitwise_or(rectangle,circle)
cv2.imshow('Bitwise OR',bitwise_or)

# XOR bitwise  : Non-Intersecting Regions
bitwise_xor=cv2.bitwise_xor(rectangle,circle)
cv2.imshow('Bitwise XOR',bitwise_xor)

# NOT bitwise  : Nothing
bitwise_not=cv2.bitwise_not(rectangle)
cv2.imshow('Bitwise NOT rectangle',bitwise_not)

bitwise_not=cv2.bitwise_not(circle)
cv2.imshow('Bitwise NOT circle',bitwise_not)







cv2.waitKey(0)