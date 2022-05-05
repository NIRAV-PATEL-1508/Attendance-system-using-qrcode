import csv

f = open(r'StudentDetails/studentdata.csv');

data =""
for line in f:
    data_line = line.rstrip().split(',')
    data = data_line[0]

