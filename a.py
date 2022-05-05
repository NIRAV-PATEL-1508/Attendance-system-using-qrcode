import sys,time
import cv2
import numpy as np

cap=cv2.VideoCapture (0)
detector=cv2.QRCodeDetector()
a=[]
while True:
    _,img=cap.read()
    data,one,_=detector.detectAndDecode(img)
    
    if data:
        a.append(data)
        break
    cv2.imshow('qrcodescanner app',img)
    if cv2.waitKey(1) ==ord('q'):
        break
print(a)
cv2.destroyAllWindows()