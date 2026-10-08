from datetime import datetime
import time
import adafruit_dht
import board
import digitalio

# Initialize the DHT11 sensor
sensor = adafruit_dht.DHT11(board.D16)

# Initialize LEDs using digitalio
red_led = digitalio.DigitalInOut(board.D12)
red_led.direction = digitalio.Direction.OUTPUT

blue_led = digitalio.DigitalInOut(board.D21)  # Fixed incomplete initialization
blue_led.direction = digitalio.Direction.OUTPUT


def to_fahrenheit(c):
    return (c * 9 / 5) + 32


# Initialize the CSV file with headers
with open("temperature.csv", "w") as file:
    file.write("time,temperature\n")

while True:
    try:
        celsius = sensor.temperature

        # Check if the sensor returned a valid reading
        if celsius is not None:
            fahrenheit = to_fahrenheit(celsius)
            current_time = datetime.now()
            time_str = current_time.strftime("%H:%M:%S")  # Fixed typo

            output_line = f"{time_str},{fahrenheit:0.1f}\n"

            # Append data to CSV
            with open("temperature.csv", "a") as file:
                file.write(output_line)

            # LED logic (Fixed mixed spaces/tabs and indentation)
            if fahrenheit > 72:
                red_led.value = True
                blue_led.value = False
            elif fahrenheit < 72:
                red_led.value = False
                blue_led.value = True
            else:
                red_led.value = False
                blue_led.value = False

        time.sleep(2)

    except RuntimeError as error:
        # DHT sensors often fail to read; print warning and retry
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
