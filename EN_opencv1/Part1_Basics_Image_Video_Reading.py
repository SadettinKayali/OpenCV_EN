import cv2
import os 

## READING IMAGES
#img=cv2.imread('Resources/Photos/cat.jpg')
# açılmazsa bu şekilde resim okuması yapılabilir.
ImageFile_name = os.path.join(os.path.dirname(__file__), 'Resources/Photos/cat.jpg')
assert os.path.exists(ImageFile_name)
img = cv2.imread(ImageFile_name)
cv2.imshow('Cat',img)
cv2.waitKey(0) 


## READING VIDEOS from files
VideoFile_name = os.path.join(os.path.dirname(__file__), 'Resources/Videos/dog.mp4')
assert os.path.exists(VideoFile_name)
captureVideo=cv2.VideoCapture(VideoFile_name) # Kameradan görüntü çekilecekse 
while True:
    isTrue,frame=captureVideo.read()
    cv2.imshow('Video',frame)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
captureVideo.release()

## READING Videos from Camera
captureCamera=cv2.VideoCapture(0) # Kameradan görüntü çekilecekse 
while True:
    isTrue,frame=captureCamera.read()
    cv2.imshow('Video',frame)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
captureCamera.release()




cv2.destroyAllWindows()