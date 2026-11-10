import random
import time
from time import sleep
import tm1637
from gpiozero import LED
from gpiozero import Button
from gpiozero import OutputDevice


led = LED(12)
button1 = Button(4)
button2 = Button(22)
display = tm1637.TM1637(clk=18, dio=17)

button1.when_pressed = led.on
button1.when_released = led.off

def rig_display():
        digit = random.choice("123456789")
        same_digit_number = int(digit * 4)
        formatted_rig = (f"{same_digit_number}")
        print(f"Generated Number: {same_digit_number})
        display.show(same_digit_number)
        
def generate_and_display():
        random_number = random.randint(0, 9999)
        formatted_str = (f"{random_number:04d}")
        print(f"Generated Number: {formatted_str}")
        display.show(formatted_str)

button1.when_pressed = generate_and_display
button2.when_pressed = rig_display

pause()
