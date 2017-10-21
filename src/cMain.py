import serial
import time

strSerPort="/dev/ttyS1"

ser= serial.Serial(port=strSerPort, baudrate=250000)
ser.close()
ser.open()

ser.write("f 0 5658")
ser.write("f 0 5732")
ser.write("f 0 5880")

if ser.isOpen():
    while True:

        print("Serial is open")

        if (ser.inWaiting()>0):
            data=ser.read(ser.inWaiting())
            print(data)


        time.sleep((2))

else:
    print("Serial is not open")