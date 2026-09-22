from gpiozero import PWMLED
from time import sleep
from gpiozero import RotaryEncoder

led = PWMLED(18)
rotor = RotaryEncoder(16, 20, wrap=True, max_steps=180) # DT goes to 16, CLK goes to 20

while True:
    led.value = 0  # off
    sleep(1)
    led.value = 0.5  # half brightness
    sleep(1)
    led.value = 1  # full brightness
    sleep(1)

while True:
	print(rotor.steps) # the value of rotor.steps will change as you rotate the device
