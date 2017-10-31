from __future__ import division
import serial
import time
import io
import Adafruit_PCA9685 as ADAdriver


def set_servo_pulse(channel, pulse):
    pulse_length = 10000000
    pulse_length //= 60
    print("{0}us per period".format(pulse_length))
    pulse_length //= 4096
    print("{0}us per bit".format(pulse_length))
    pulse *=1000
    pulse //= pulse_length

    pwm.set_pwm(channel,0,pulse)


strSerPort = "/dev/ttyS1"
intBaudRate=250000
intAvg=50
booCalib=False

pwm=ADAdriver.PCA9685(address=0x40, busnum=0)
pwm.set_pwm_freq(60)


servo_min=150
servo_max=600

print("Move it")
#set_servo_pulse(0,150)



print("to the min")
for i in range(15):
    pwm.set_pwm(i,0,servo_min)
    time.sleep(0.2)

time.sleep(1)

print("to the max")
for i in range(15):
    pwm.set_pwm(i,0,servo_max)
    time.sleep(0.2)

time.sleep(1)

ser= serial.Serial()
ser.baudrate=intBaudRate
ser.port=strSerPort


if ser.isOpen()==False:
    ser.open()

intSum=0
rssisSum={}
ser.write("s\n")

ser.write("f 0 5658\n")
ser.write("f 1 5658\n")
ser.write("f 2 5658\n")

ser.write("?\n")

if booCalib:

    print("calib")
    time.sleep(3)

    ser.write("n\n")

    time.sleep(2)
    print("max")
    time.sleep(5)

    ser.write("m\n")

minRssi=260.0
maxRssi=0.0

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
                        rssi_raw=round(rssi/intAvg)
                        floRssi=rssi_raw

                        if floRssi>10: 
                            if floRssi<minRssi:
                                minRssi=floRssi
                            if floRssi>maxRssi and floRssi<255:
                                maxRssi=floRssi
          
                        pwmValue=servo_min

                        floDiff=floRssi/(maxRssi+minRssi)
                        if floDiff<0:
                            floDiff=0
                        if floDiff>1:
                            floDiff=1

                        pwmValue=servo_max*floDiff 
                        print("set: " + str(servo_min) + " > " + str(pwmValue) + " < " + str(servo_max))
                        pwm.set_pwm(channel, 0, int(pwmValue))

                        print(str(channel) + " " + str(rssi_raw) + " (" + str(minRssi) + "-" + str(maxRssi)+" ["+str(floDiff) +"])")
                    for channel, rssi in rssisSum.iteritems():
                        rssisSum[channel]=0

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
