from gpiozero import LED
from time import sleep

green = LED(18)

while True:
    green.on()
    sleep(1)
    green.off()
    sleep(1)
