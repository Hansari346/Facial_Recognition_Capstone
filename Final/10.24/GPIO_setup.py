#GPIO setup

import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

#LED_RED = 7
#LED_GREEN = 13
Relay_GPIO = 37


#GPIO.setup(LED_RED,GPIO.OUT, initial = GPIO.LOW)
#GPIO.setup(LED_GREEN, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Relay_GPIO, GPIO.OUT, initial = GPIO.HIGH)



def Lock_Door():
    GPIO.output(Relay_GPIO, GPIO.LOW)

def Unlock_Door():
    GPIO.output(Relay_GPIO, GPIO.HIGH)
