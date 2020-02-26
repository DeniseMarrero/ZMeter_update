import serial
import numpy as np
import sys
import _thread



# Opening serial port  
def OpenSerial():
    try:
        ser = serial.Serial('COM3', baudrate = 115200, timeout = None) 
        
    except Exception as error:
        print('Exception: Opening serial port: ' + str(error))
        ser.close()
        ser.open()  
    else:
        ser.isOpen()
        print ('Port is opened')
   
        
    
# Closing serial port  
def CloseSerial():
        ser.close()
        print ('Closing ' + ser.name)
        
        
OpenSerial()

RetrieveData ()

CloseSerial()        
        
        
        
def RetrieveData ():
       rawdata = ser.read_all()
       print(rawdata) 
       for s in rawdata:
           #data.append(s)
           print(s)       
    
def ReceiveData (str data):
        for i in range (0, len(data)):
            
def SendData
            
   
res = None
for i in range(0, len(data)):
    if data[i] == 4:
        res = i +1
        break
if res == None:
    print('No end of transmission')
else:
    print ('End of transmission')

if 4 in rawdata:print ('First line \n Second line')


#from ASCII values to characters
data =[1, 32, 55, 2, 87, 69, 76, 67, 79, 77, 69, 3, 53, 65, 4, 1, 49, 52, 2, 90, 77, 101, 116, 101, 114, 52, 119, 32, 118, 32, 52, 46,
 50, 32, 67, 79, 82, 66, 73, 3, 55, 57, 4]
characters = [chr(ascii) for ascii in data]
''.join(characters)

#from characters to ASCII values
s = '\x01 7\x02WELCOME\x035A\x04\x0114\x02ZMeter4w v 4.2 CORBI\x0379\x04'
ASCII = [ord(c) for c in s]


