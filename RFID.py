import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Scan RFID card")
    id, text = reader.read()
    print("ID:", id)
    print("Text:", text)

finally:
    GPIO.cleanup()