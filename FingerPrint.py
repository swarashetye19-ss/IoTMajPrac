import time
import adafruit_fingerprint
import serial

uart = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=1)

finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

print("Place your finger on the sensor")

while True:
    if finger.get_image() == adafruit_fingerprint.OK:
        print("Image taken")

        if finger.image_2_tz(1) == adafruit_fingerprint.OK:
            print("Image converted")

            if finger.finger_search() == adafruit_fingerprint.OK:
                print("Fingerprint matched!")
            else:
                print("Fingerprint not found")

        time.sleep(2)