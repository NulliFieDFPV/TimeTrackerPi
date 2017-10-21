import serial
import time
import io

strSerPort="/dev/ttyS1"
intBaudRate=250000

ser= serial.Serial()
ser.baudrate=intBaudRate
ser.port=strSerPort

ser.close()
ser.open()

sio= io.TextIOWrapper(io.BufferedRWPair(ser, ser))

booRaw=True

if sio.isOpen():
    print("Serial is open")

    sio.write(u's')

    print("RX 0 setzen")
    sio.write(u'f 0 5880')

    print("RX 1 setzen")
    sio.write(u'f 1 5880')

    print("RX 2 setzen")
    sio.write(u'f 2 5880')

    while True:
        time.sleep(5)
        sio.write(u"?")
        print("Status?")

else:
    print("Serial is not open")
