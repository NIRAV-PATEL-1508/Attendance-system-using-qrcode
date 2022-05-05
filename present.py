import csv
import pyqrcode
import shutil,os
from pyqrcode import QRCode
import numpy as np
import cv2
import pandas as pd
import datetime
import time

enos=pd.read_csv("StudentDetails\studentdata.csv")