import os
from acmepins import GPIO
from time import sleep

ledIR = GPIO('J4.32','OUTPUT')
#photo = GPIO('J4.34','INPUT')
data_photo = 0

def mediane(L):
    L.sort()
    if len(L)%2:
        mid=len(L)/2
        return (L[mid-1]+L[mid]) / 2.0
    else:
        return(L[mid])

while True:
    ledIR.off()
    data_photo_mediane = []
    for i in range(7):
        with open('/sys/bus/iio/devices/iio:device0/in_voltage0_raw') as f:
            data_photo = int ( f.read() )
        data_photo_mediane.append( data_photo )
        sleep(0.001)

    print data_photo_mediane
    data_photo = mediane(data_photo_mediane)

    print data_photo
    """
    if data_photo > 512:
        print "data_photo > 512"
    elif data_photo < 512:
        print "data_photo < 512"
    else:
        print "EQUILIBRE"
    """
    sleep(0.1)
    #ledIR.off()
    sleep(0.1)


