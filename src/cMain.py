import serial
import time

strSerPort="/dev/ttyS1"

ser= serial.Serial(port=strSerPort, baudrate=250000)
ser.close()
ser.open()

time.sleep(3)
booRaw=True

if ser.isOpen():

    ser.write("f 0 5658")
    if (ser.inWaiting() > 0):
        data = ser.read(ser.inWaiting())
        print(data)

    ser.write("f 1 5732")
    if (ser.inWaiting() > 0):
        data = ser.read(ser.inWaiting())
        print(data)

    ser.write("f 2 5880")
    if (ser.inWaiting() > 0):
        data = ser.read(ser.inWaiting())
        print(data)

    while True:

        print("Serial is open")

        if (ser.inWaiting()>0):
            data=ser.read(ser.inWaiting())
            print(data)


        time.sleep((2))

        if booRaw:
            ser.write("?")

            if (ser.inWaiting() > 0):
                data = ser.read(ser.inWaiting())
                print(data)

            booRaw=False
        else:
            booRaw=True

else:
    print("Serial is not open")