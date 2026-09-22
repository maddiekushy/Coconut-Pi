from gpiozero import PWMLED
from time import sleep
from gpiozero import RotaryEncoder

led = PWMLED(18)
rotor = RotaryEncoder(16, 20, wrap=True, max_steps=180) # DT goes to 16, CLK goes to 20
rotor.steps = -180

while True:
    led.value = (rotor.steps + 180) / 360

while True:
	print(rotor.steps) # the value of rotor.steps will change as you rotate the device
