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

    ser.write("s\n")
    ser.flush()
    
    print("RX 0 setzen")
    ser.write("f 0 5880\n")
    ser.flush()
    booWarte=True
    while booWarte:
        data=ser.readline()
        
        if "ok" in data:
            booWarte=False
    #if (ser.inWaiting() > 0):
    #    data = ser.read(ser.inWaiting())
    #    print(data)

    print("RX 1 setzen")
    ser.write("f 1 5658\n")
    #ser.flush()
    #if (ser.inWaiting() > 0):
    #    data = ser.read(ser.inWaiting())
    #    print(data)

    ser.write("f 2 5658\n")
    #ser.flush()
    #if (ser.inWaiting() > 0):
    #    data = ser.read(ser.inWaiting())
    #    print(data)

    print("Power Off Now")
    time.sleep(5)
    ser.write("n\n")
    ser.flush()
    
    print("Power On Now")
    time.sleep(5)
    ser.write("m\n")
    time.sleep(2)
    ser.write("s")
    while True:
        time.sleep(5)
        ser.write("?")
        ser.flush()
        print("Status?")

else:
    print("Serial is not open")
