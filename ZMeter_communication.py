import serial
import serial.tools.list_ports
import numpy as np
import sys
import _thread

#getting info of com ports available
def get_serialInfo():
    portdata = serial.tools.list_ports.comports()
    for j in portdata:
        print(j)
#------try except
        
# opening serial port
def OpenSerial():
    try:
        ser = serial.Serial('COM3', baudrate = 115200)
        ser.open()
        print('connected to:' , ser.name)
    except Exception as error:
        print('exception: opening serial port: ' + str(error))

# closing serial port  
def CloseSerial(ser):
    if ser.is_open == True:
        ser.close()
        print ('closing ' , ser.name)
    else: 
        print(ser.name , ' already closed')

def ReadSerial():
    rawdata = ser.read_all().decode()
    data = np.array([ord(c) for c in rawdata.decode()])
    print (rawdata)
    print (data)


data1 = '\x01 7\x02WELCOME\x035A\x04\x0114\x02ZMeter4w v 4.2 CORBI\x0379\x04'
        
get_serialInfo()        
    
OpenSerial()

CloseSerial(ser)        
        
ReadSerial()    
 
ReceiveData(rawdata)

#data = data1


def ReceiveData(rawdata):
    state = 0
    for d in rawdata:
    #    print(d)
        if state == 0:
            if d == '\x01':
                state += 1
                tempLine = ''
                Length = ''
    #            print('0.0')
        elif state == 1:
            if (d != '\x02'):
                Length = Length + d            
            else:
    #            print('length', Length)
                state += 1
        elif state == 2:
            if (d != '\x03'):
                tempLine = tempLine + d            
            else:
    #            print('line-->', tempLine, 'Len--', int(Length) )            
                if len(tempLine) == int(Length, 16):
                    state += 1
                    TmpCheck = ''
                else:
                    print('error')
                    state = 0
        elif state == 3:
            if (d != '\x04'):
                TmpCheck = TmpCheck + d            
            else:            
                state = 0
                chk = 0
                for d in tempLine:
                    chk = chk ^ ord(d)
                if chk == int(TmpCheck, 16):
                    print('line-->', tempLine)
                else:
                    print('error')
                    
                