import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

segments = [2,3,4,17,27,22,10]

for pin in segments:
    GPIO.setup(pin, GPIO.OUT)

while True:
    for pin in segments:
        GPIO.output(pin, True)
    time.sleep(1)

    for pin in segments:
        GPIO.output(pin, False)
    time.sleep(1)