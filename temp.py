import serial
import serial.tools.list_ports
import numpy as np
import sys
import _thread

#Getting info of com ports available
def get_serialInfo():
    portData = serial.tools.list_ports.comports()
    for j in portData:
        print(j)
#------try except
        
# Opening serial port
def OpenSerial():
    try:
        ser = serial.Serial('COM5', baudrate = 115200)
        ser.open()
        print('Connected to ' + ser.name)
    except Exception as error:
        print('Exception: Opening serial port: ' + str(error))

# Closing serial port  
def CloseSerial():
    if ser.is_open == True:
        ser.close()
        print ('Closing ' + ser.name)
    else: 
        print(ser.name + ' already closed')

def ReadSerial():
    rawdata = ser.read_all()
    data = np.array([ord(c) for c in rawdata.decode()])
    print (rawdata)
    print (data)
    return data

def CheckSum(data):
    temporal = 0
    for d in data:
        temporal = temporal ^ d
        return temporal
    
data1 = '\x01 7\x02WELCOME\x035A\x04\x0114\x02ZMeter4w v 4.2 CORBI\x0379\x04'

def ReceiveData(data):
    tempLine = 0
    tempVal = 0
    tempLen = 0
    state = 0
    for i in range(len(data)):
        if state == 0:
            if data[0] == 1:
                state += 1
                tempLine = 0
                tempVal = 0
                print('0.0')
        elif state == 1:
            if (data[0] != 32):
                tempVal = tempVal + data
                print('0.1')
            state += 1
        elif state == 2:
            tempVal = tempVal + data
            try:
                tempLen = tempVal
                state += 1
                tempVal = 0
                print('1.0')
            except:
                state = 0
        elif state == 3:
            if data[0] == 2:
                state += 1
                print('2.0')
            else:
                state = 0
        elif state == 4:
            if data[0] == 3:
                state += 1
                print('3.0')
            else:
                tempLine = tempLine + data
            if len(tempLine) != tempLen:
                state = 0
        elif state == 5:
            if len(tempLine) != tempLen:
                state = 0
                print('4.0')
            elif data != 32:
                tempVal = tempVal + data
            state += 1
        elif state == 6:
            tempVal = tempVal + data
            if tempVal == CheckSum(tempLine):
                state += 1
                print('5.1')
            else: state = 0
        elif state == 7:
            print('6')
            if data[0] == 4:
                print('fdfs')
                
        
                
                
            
get_serialInfo()        
    
OpenSerial()

CloseSerial()        
        
ReadSerial()    

CheckSum(data)  

ReceiveData(data)





        
            

