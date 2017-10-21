import serial
import time
import io

strSerPort = "/dev/ttyS1"
intBaudRate=250000

ser= serial.Serial()
ser.baudrate=intBaudRate
ser.port=strSerPort

ser.close()
ser.open()

message=""
eol='\x0d'
leneol=len(eol)

ser= serial.Serial(port=strSerPort, baudrate=250000)
sio= io.TextIOWrapper(io.BufferedRWPair(ser, ser))
#ser.open()

while True:

    if sio.inWaiting():
        ser_data = ser.readline()
        if ser_data !="":
            message=ser_data
            #if "\x0d" in message:
                #print(":::"+message+":::")
                #message=message + ser_data
            if message[0] !="r":
                print(":::"+message+":::")
                message=""
            #else:
                #pass
                #message= message + ser_data
