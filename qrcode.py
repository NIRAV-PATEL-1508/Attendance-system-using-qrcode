import csv
import pyqrcode
import shutil,os
from pyqrcode import QRCode

f = open(r'StudentDetails/studentdata.csv');

data =""
for line in f:
    data_line = line.rstrip().split(',')
    data = data_line[0]
    url = pyqrcode.create(data)
    url.png(data+".png", scale=8)
    shutil.move(data+".png","Qrcodes"+'/'+data+".png")