import serial
import time
import io

strSerPort = "/dev/ttyS1"
intBaudRate=250000
intAvg=500

ser= serial.Serial()
ser.baudrate=intBaudRate
ser.port=strSerPort


if ser.isOpen()==False:
    ser.open()

intSum=0
rssisSum={}

while True:
    
    size= ser.inWaiting()
    if size:
        data=ser.readline()
        if len(data)>1:
                
            #print("DATA:"+data)           
            message=str(data.replace("\r\n",""))

            if message[0] == "r":
                #print("RSSI:")
                
                rssis=message[2:].split(" ")
                #print(rssis)
                if intSum>=intAvg:
                    intSum=0
                    for channel, rssi in rssisSum.iteritems():
                      
                        print(str(channel) + " " + str((round(rssi/intAvg))))
                    rssisSum={}

                for channel in range(len(rssis)):
                    intRealChannel=channel+1

                    try:
                        intRssi=int(rssis[channel])
                    except:
                        intRssi=0

                    if (intRealChannel in rssisSum) ==False:
                        rssisSum[intRealChannel]=intRssi
                    else:    
                        rssisSum[intRealChannel] = rssisSum[intRealChannel] + intRssi

                    #print(str(channel+1) + " " + str(intRssi))

                intSum +=1
                   
            elif message[:2] =="ok":
                print("bestaetigung")

            elif message[0] == "?":
                print("Status:")
                print(message[2:])

            else:
                print("Unbekannte message:")
                print(message)
