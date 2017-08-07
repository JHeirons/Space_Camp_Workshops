import RPi.GPIO as GPIO
import time

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

launch = 4

GPIO.setup(launch, GPIO.OUT)



arm_prev_input = 0
launch_prev_input = 0

armed = False

while True:
    GPIO.output(led1, GPIO.LOW)
    GPIO.output(led2, GPIO.LOW)
    GPIO.output(led3, GPIO.LOW)
    GPIO.output(launch, GPIO.LOW)
    
    input = (GPIO.input(arm_switch))
    if ((not arm_prev_input) and input):
        armed = True
        if (armed == True):
            GPIO.output(led1, GPIO.HIGH)
            GPIO.output(led2, GPIO.HIGH)
            GPIO.output(led3, GPIO.HIGH)
            print (armed)
            input = (GPIO.input(launch_button))
            if ((not launch_prev_input) and input):
                GPIO.output(led1, GPIO.LOW)
                GPIO.output(led2, GPIO.LOW)
                GPIO.output(led3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led1, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(led2, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(led3, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(launch, GPIO.HIGH)
                time.sleep(10)
                print('launch')
            launch_prev_input = input
            time.sleep(0.05)
              
    arm_prev_input = input
    time.sleep(0.05)
