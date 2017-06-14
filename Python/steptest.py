import os
from acmepins import GPIO
from time import sleep

#Step
enable = GPIO('J4.23','OUTPUT')
step = GPIO('J4.28','OUTPUT') 
dir = GPIO('J4.30','OUTPUT')
ms1 = GPIO('J4.25','OUTPUT')
ms2 = GPIO('J4.27','OUTPUT')
ms3 = GPIO('J4.29','OUTPUT')

pas = 0


def check_step():
    ms1.off()
    ms2.off()
    ms2.off()
    step.on()
    sleep(0.01)
    step.off()
    sleep(0.01)

while True:
    enable.off()

    dir.off()
    pas+=1
    check_step()
    print "Pas avant",pas


