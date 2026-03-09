import serial

gps = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

while True:
    data = gps.readline()
    print(data)