import time
from time import sleep
from gpiozero import LED
from gpiozero import OutputDevice
    
led1 = LED(18)
led2 = LED(23)
led3 = LED(24)
led4 = LED(25)
led5 = LED(12)
led6 = LED(16)
led7 = LED(21)
led8 = LED(6)

def d_binary(n):
n = input("Enter and integer between 1 and 225 inclusive:")

    if n == 0:
        return 0
    else:
        return (n % 2 + 10 * d_binary(n // 2))

def display:
    binary = ({d_binary(n)}: 08d)
    digits = [int(d) for d in str(binary)]
    return(digits)

    lights = {led1: digits[0], led2: digits[1], led3: digits[2] led4: digits[3], led5: digits[4], led6: digits[5], led7: digits[6], led8: digits[7]}

    for light, number in lights:
        if number = 0:
            light.value = False
        
        else:
            light.value = True
