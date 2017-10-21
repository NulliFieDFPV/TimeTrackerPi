import serial
import time

strSerPort="/dev/ttyS1"

ser= serial.Serial(port=strSerPort, baudrate=250000)
ser.close()
ser.open()

while True:
    if ser.isOpen():
        print("Serial is open")

        if (ser.inWaiting()>0):
            data=ser.read(ser.inWaiting()).decode()
            print(data)
    else:
        print("Serial is not open")

    time.sleep((2))

