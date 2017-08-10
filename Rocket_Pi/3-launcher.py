import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

launch_button = 26
arm_switch = 19

GPIO.setup(launch_button, GPIO.IN)
GPIO.setup(arm_switch, GPIO.IN)

led1 = 17
led2 = 27
led3 = 22

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

ignition = 4

GPIO.setup(ignition, GPIO.OUT)



arm_prev_input = 0
launch_prev_input = 0

armed = False

while True:
    GPIO.output(led1, GPIO.LOW)
    GPIO.output(led2, GPIO.LOW)
    GPIO.output(led3, GPIO.LOW)
    GPIO.output(ignition, GPIO.LOW)
    
    input = (GPIO.input(arm_switch))
    if ((not arm_prev_input) and input):
        armed = True
        if (armed == True):
            GPIO.output(led1, GPIO.HIGH)
            GPIO.output(led2, GPIO.HIGH)
            GPIO.output(led3, GPIO.HIGH)
            print ("Circuit armed")
            input = (GPIO.input(launch_button))
            if ((not launch_prev_input) and input):
                GPIO.output(led1, GPIO.LOW)
                GPIO.output(led2, GPIO.LOW)
                GPIO.output(led3, GPIO.LOW)
                sleep(0.5)
                GPIO.output(led1, GPIO.HIGH)
                print("3")
                sleep(1)
                GPIO.output(led2, GPIO.HIGH)
                print("2")
                sleep(1)
                GPIO.output(led3, GPIO.HIGH)
                print("1")
                sleep(1)
                GPIO.output(ignition, GPIO.HIGH)
                print('ignition')
                sleep(10)
            launch_prev_input = input
            sleep(0.05)
              
    arm_prev_input = input
    sleep(0.05)
