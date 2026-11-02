import random
import time
from machine import TM1637 
from digitalio import LED, button
from signal import pause

led = LED(12)
button = Button(4)

button.when_pressed = led.on
button.when_released = led.off

pause()

last_state = 1

print("Press the button to generate a random 4-digit number...")

while True:
    current_state = button.value()
    
    if last_state == 1 and current_state == 0:
        rand_num = random.randint(1000, 9999)
        
        print(f"Button pressed! Generated number: {rand_num}")
        
        time.sleep(0.3)
        
    last_state = current_state
    time.sleep(0.05)
