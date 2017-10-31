import serial
import time
import io

strSerPort="/dev/ttyS1"
intBaudRate=250000

ser= serial.Serial()
ser.baudrate=intBaudRate
ser.port=strSerPort

if ser.isOpen()==False:
    ser.open()

booRaw=True

if ser.isOpen():
    print("Serial is open")
    time.sleep(3)
    ser.write("r\n")
    print("n")

    ser.write("n\n")
    time.sleep(6)
    print("m")
    time.sleep(5)
    ser.write("m\n")

    ser.write("?\n")

    print("RX 0 setzen")
    ser.write('f 0 5658\n')
   
    print("RX 1 setzen")
    ser.write('f 1 5658\n')

    print("RX 2 setzen")
    ser.write('f 2 5658\n')

    while True:
        time.sleep(5)
        ser.write("?\n")
        print("Status?")
else:
    print("Serial is not open")
