import serial
import time

strSerPort = "/dev/ttyS1"
message=""
eol='\x0d'
leneol=len(eol)

ser= serial.Serial(port=strSerPort, baudrate=250000)
#ser.open()

while True:

    if ser.inWaiting():
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
