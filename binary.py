from time import sleep
from gpiozero import LED

leds = [
    LED(18),
    LED(23),
    LED(24),
    LED(25),
    LED(12),
    LED(16),
    LED(20),
    LED(21),
]


def d_binary(n):
  if n == 0:
    return 0
  else:
    return n % 2 + 10 * d_binary(n // 2)


def display():
  n = int(input("Enter an integer between 1 and 255 inclusive: "))

  binary_str = f"{d_binary(n):08d}"
  print(binary_str)
  digits = [int(d) for d in binary_str]

  for light, number in zip(leds, digits):
    if number == 1:
      light.on()
    else:
      light.off()


display()
sleep(5)

