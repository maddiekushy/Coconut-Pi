from datetime import datetime
import time
import adafruit_dht
import board
import digitalio

sensor = adafruit_dht.DHT11(board.D16)

red_led = digitalio.DigitalInOut(board.D12)
red_led.direction = digitalio.Direction.OUTPUT

blue_led = digitalio.DigitalInOut(board.D21)
blue_led.direction = digitalio.Direction.OUTPUT


def to_fahrenheit(c):
    return (c * 9 / 5) + 32


with open("temperature.csv", "w") as file:
    file.write("time,temperature\n")

while True:
    try:
        celsius = sensor.temperature

        if celsius is not None:
            fahrenheit = to_fahrenheit(celsius)
            current_time = datetime.now()
            time_str = current_time.strftime("%H:%M:%S")
            
            output_line = f"{time_str},{fahrenheit:0.1f}\n"

            with open("temperature.csv", "a") as file:
                file.write(output_line)

            if fahrenheit > 72:
                red_led.value = True
                blue_led.value = False
            elif fahrenheit < 72:
                red_led.value = False
                blue_led.value = True
            else:
                red_led.value = False
                blue_led.value = False

        time.sleep(2.0)

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
