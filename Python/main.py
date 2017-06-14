import os
from acmepins import GPIO
from time import sleep

#Stepper
enable = GPIO('J4.23','OUTPUT')
step = GPIO('J4.28','OUTPUT') 
dir = GPIO('J4.30','OUTPUT')
ms1 = GPIO('J4.25','OUTPUT')
ms2 = GPIO('J4.27','OUTPUT')
ms3 = GPIO('J4.29','OUTPUT')

#Diodes
ledIR = GPIO('J4.32','OUTPUT')
data_photo = 0

check = False 
pas = 0
ratio = 1.3072
poids = 0

def check_step():
    ms1.off()
    ms2.off()
    ms2.off()
    if 200 < data_photo < 900:
        step.on()
        sleep(0.5)
        step.off()
        sleep(0.5)
        print "Doucement"
    else:
        step.on()
        sleep(0.001)
        step.off()
        sleep(0.001)
        print "Rapide"

def mediane(L):
    L.sort()
    if len(L)%2:
        mid=len(L)/2
        return (L[mid-1]+L[mid]) / 2.0
    else:
        return(L[mid])


while True:
    enable.off()
    ledIR.off()

    with open('/sys/bus/iio/devices/iio:device0/in_voltage0_raw') as f:
        data_photo = int ( f.read() )
 
    if 200 < data_photo < 900:
        data_photo_mediane = []
        for i in range(21):
            with open('/sys/bus/iio/devices/iio:device0/in_voltage0_raw') as f:
                data_photo = int ( f.read() )
            data_photo_mediane.append( data_photo )
            sleep(0.001)

        print data_photo_mediane
        data_photo = mediane(data_photo_mediane)

    print data_photo
    

    if data_photo > (512+7):
        dir.on()
        pas+=1

        print "Diode ",data_photo
        check_step()
        print "Pas avant",pas
        check = False 
    elif data_photo < (512-7):
        dir.off()
        pas-=1
        print "Diode ",data_photo
        check_step()
        print "Pas arriere",pas
        check = False 
    else:
        if check == False:
            print "EQUILIBRE"
            print "Diode ",data_photo
            print "Pas ",pas
            poids = ratio * pas
            print "Poids ",poids
            enable.on()
            sleep(5)
            #pas = 0
            check = True 
        else:
            sleep(10)


