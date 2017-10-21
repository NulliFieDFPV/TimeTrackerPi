import serial
import time

strSerPort = "/dev/ttyS1"


ser= serial.Serial(port=strSerPort, baudrate=250000)
ser.open()

while True:

    x = ser.readline()
    print(x)