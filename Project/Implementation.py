import serial
import time
import pandas as pd


ser = serial.Serial("COM5",9600,timeout=0.5)
dataset =[]
count=0

while True:
    if(ser.inWaiting() > 0):
        data = ser.readline()
        data = data.decode('utf-8')
        if(data.startswith('#')):
            data = data [ :-1]
            data = data.split(',')
            count+=1
            dummy=[]
            dummy.append(data[1])
            dummy.append(data[2])
            dummy.append(data[3])
            dataset.append(dummy)
            if(count==50):
                df=pd.DataFrame(dataset)
                df.to_csv('project.csv')
                count=0
            print(dataset)



