import cv2
import os 

def rescaleFrame(frame,scale=0.33): # Images,Videos,Live Video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

# Rescale Photos
ImageFile_name = os.path.join(os.path.dirname(__file__), 'Resources/Photos/cat_large.jpg')
assert os.path.exists(ImageFile_name)

image = cv2.imread(ImageFile_name)
imageScaled=rescaleFrame(image)
cv2.imshow('Cat',image)
cv2.imshow('Cat Scaled',imageScaled)

cv2.waitKey(0) 

# Rescale Videos
VideoFile_name = os.path.join(os.path.dirname(__file__), 'Resources/Videos/dog.mp4')
assert os.path.exists(VideoFile_name)
captureVideo=cv2.VideoCapture(VideoFile_name) # Kameradan görüntü çekilecekse 
while True:
    isTrue,frame=captureVideo.read()
    frame_resized=rescaleFrame(frame)

    cv2.imshow('Video',frame)
    cv2.imshow('Video Resized',frame_resized)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
captureVideo.release()