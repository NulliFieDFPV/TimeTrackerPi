import datetime
import time
import random

class settings(object):

    rssiThreshold=0
    calibrationOffset=0

    def __init__(self):


        self.rssiThreshold=20
        self.calibrationOffset=-5

class pilot(object):


    __rssi=0
    __rssiRaw=0

    __rssiPeak=0
    __lastPeak = 0
    __rssiTrigger=0

    __threshold=0
    __lastThreshold=0

    __rssiPeakTimeStamp=datetime.datetime.now()
    __lastPeakTimeStamp=datetime.datetime.now()
    __rssiTimeStamp = datetime.datetime.now()
    __lastTimeStamp = datetime.datetime.now()

    def __init__(self):

        self.settings=settings()
        self.__rssiTrigger=240
        while True:
            x = random.randint(0, 255)
            self.getNewRssi(x)
            time.sleep(1)

    def getNewRssi(self,intRssi):

        now = datetime.datetime.now()
        timestamp = time.mktime(now.timetuple()) + now.microsecond / 1e6

        print(now, intRssi)

        self.__lastThreshold = self.__threshold
        self.__lastTimeStamp=self.__rssiTimeStamp

        if intRssi>self.__rssiPeak:
            self.__lastPeak=self.__rssiPeak
            self.__lastPeakTimeStamp=self.__rssiPeakTimeStamp

            self.__rssiPeak=intRssi
            self.__rssiPeakTimeStamp=timestamp


        self.__threshold=(self.__rssi - intRssi)

        if self.__threshold>(self.__rssiTrigger-intRssi):
            if intRssi > self.__rssiPeak:
                self.__lastPeak = self.__rssiPeak
                self.__lastPeakTimeStamp = self.__rssiPeakTimeStamp

                self.__rssiPeak = intRssi
                self.__rssiPeakTimeStamp = timestamp

            print(self.__threshold, self.__lastPeakTimeStamp, self.__lastPeak,  self.__rssiPeak, self.__rssiPeakTimeStamp)

        self.__rssi = intRssi
        self.__rssiTimeStamp = timestamp


    @property
    def rssi(self):
        return self.__rssi



if __name__ == '__main__':

    clsPilot=pilot()

