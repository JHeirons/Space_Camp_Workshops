import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

button = 4
GPIO.setup(button, GPIO.IN)

prev_input = 0

while True:
    input = (GPIO.input(button))
    if ((not prev_input) and input):
        print ('Button Pressed')
        
    prev_input = input
    time.sleep(0.05)