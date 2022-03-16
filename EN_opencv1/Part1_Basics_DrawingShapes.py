import cv2
import numpy as np

import os 
ImageFile = os.path.join(os.path.dirname(__file__), 'Resources/Photos/cat.jpg')
assert os.path.exists(ImageFile)
image=cv2.imread(ImageFile)
cv2.imshow('Cat',image)

blank=np.zeros((500,500,3),dtype='uint8') # (heigt,width,color_channel)
cv2.imshow('Blank',blank)

# 1.Paint the image a certain colour
blank[:]=0,255,0  # blank[colour size ] = RGB Color code 
cv2.imshow('Green',blank)

blank[200:400,300:600]=255,0,0  # blank[colour size ] = RGB Color code 
cv2.imshow('Blue',blank)

# 2.Draw Rectangle
cv2.rectangle(blank,(0,0),(250,250),(255,0,0),thickness=3)
cv2.rectangle(blank,(0,0),(350,350),(0,0,255),thickness=cv2.FILLED) # cv2.FILLED yerine -1 yazılabilir.
cv2.imshow('Rectangle',blank)

# 3.Draw Circle
cv2.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(255,0,0),thickness=-1)
cv2.imshow('Circle',blank)


blank_new=np.zeros((1000,1000,3),dtype='uint8') # (heigt,width,color_channel)
cv2.line(blank_new,(0,0),(500,500),(150,120,10),15) # Başlangıç ve bitiş koordinatları yazılıyor. RGB olarak renk kodu yazılıyor. Çizgi kalınlığı yazılıyor
cv2.rectangle(blank_new,(120,120),(360,560),(255,150,50),2) #başlangıç noktası, genişlik ve yükseklik,kalınlık (içini doldurmak için - li yazılıyor)
cv2.rectangle(blank_new,(720,10),(160,160),(50,150,255),-4) #başlangıç noktası, genişlik ve yükseklik,kalınlık (içini doldurmak için - li yazılıyor)
cv2.circle(blank_new,(150,650),100,(50,60,70),9) #başlangıç noktası, çap ,kalınlık (içini doldurmak için - li yazılıyor)
cv2.circle(blank_new,(550,650),100,(150,160,170),-9)
cv2.ellipse(blank_new,(500,500),(100,200),0,0,360,(0,122,255),7)#başlangıç noktası, genişlik ve yükseklik,açısı,kaç derece çizdirsin,kalınlık (içini doldurmak için - li yazılıyor)
cv2.ellipse(blank_new,(500,100),(200,100),45,0,120,(255,122,0),-7)#başlangıç noktası, genişlik ve yükseklik,açısı,kaç derece çizdirsin,kalınlık (içini doldurmak için - li yazılıyor)
cv2.putText(blank_new,'Sadettin',(100,0),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,3,(100,100,100),3,cv2.LINE_AA,True) # True olursa aynalanmış yazar,
cv2.putText(blank_new,'KAYALI',(0,200),cv2.FONT_ITALIC,3,(200,200,200),9,cv2.LINE_AA,False)# False olursa düz yazar,
cv2.imshow('All in one',blank_new)



cv2.waitKey(0)
if cv2.waitKey(20) & 0xFF==ord('d'):
    cv2.destroyAllWindows()