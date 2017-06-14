from acmepins import GPIO
from time import sleep

#FOX Board G20 example
#led = GPIO('J7.3','OUTPUT') 

#Aria G25 example
#led = GPIO('W9','OUTPUT') 

#Arietta G25 example
led = GPIO('J4.40','OUTPUT') 

#Acqua A5 example
#led = GPIO('J3.32','OUTPUT') 

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
