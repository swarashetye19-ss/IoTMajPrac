import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led1 = 17
led2 = 18
led3 = 27

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

while True:
    GPIO.output(led1, True)
    time.sleep(1)
    GPIO.output(led1, False)

    GPIO.output(led2, True)
    time.sleep(1)
    GPIO.output(led2, False)

    GPIO.output(led3, True)
    time.sleep(1)
    GPIO.output(led3, False)