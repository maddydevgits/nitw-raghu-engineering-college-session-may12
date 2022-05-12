import serial
import time

# create a serial object
ser=serial.Serial('COM3',9600,timeout=0.5)

def readDataFromArduino():
    if ser.inWaiting()>0: # returning the length of queue(0)
        dataSample=ser.readline().decode('utf-8') # bytes data into str data
        dataSample=dataSample.split("~")
        hum=dataSample[1]
        temp=dataSample[2]
        print(hum,temp)
        return(hum,temp)

# while True:
#     readDataFromArduino()
