import sys,time
import cv2
import numpy as np

cap=cv2.VideoCapture(0)
names = []
fob=open('attendence.txt', 'a+')
def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        z=".join(str(z))"
        fob.write(z+'\n')
        return names
        print('Reading code.............')
 
def checkData(data):
    data = str(data)
    if data in names:
      print('Already present')
    else:
        print('\n'+str(len (names)+1)+ '\n'+'Present done')
    enterData(data)
 

detector=cv2.QRCodeDetector()
while True:
    _,img=cap.read()
    data,one,_=detector.detectAndDecode(img)
    for obj in data:
        checkData(obj.data)
        time.sleep(1)
    cv2.imshow('Frame', data)