import serial
import time

strSerPort="/dev/ttyS1"

ser= serial.Serial(port=strSerPort, baudrate=250000)
ser.close()
ser.open()

time.sleep(3)
booRaw=True

if ser.isOpen():
    print("Serial is open")

    print("set calib")
    #ser.write("s\n")
    ser.write("r\n")
    #ser.flush()
    print("RX 0 setzen")
    ser.write("f 0 5658\n")
    #ser.flush()
 
    #if (ser.inWaiting() > 0):
    #    data = ser.read(ser.inWaiting())
    #    print(data)

    print("RX 1 setzen")
    ser.write("f 1 5880\n")
 
    #ser.flush()
    #if (ser.inWaiting() > 0):
    #    data = ser.read(ser.inWaiting())
    #    print(data)
    print("RX 2 setzen")
    ser.write("f 2 5658\n")
    ser.flush()
     #if (ser.inWaiting() > 0):
    #    data = ser.read(ser.inWaiting())
    #    print(data)

    while True:
        time.sleep(5)
        ser.write("?")
        ser.flush()
        #data = ser.readline()
	#print data

else:
    print("Serial is not open")
