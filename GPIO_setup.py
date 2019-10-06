#GPIO setup

import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

LED_RED = 31
LED_GREEN = 37
Relay_GPIO = 13
D6T_SDA = 3
D6T_SCL = 5

GPIO.setup(LED_RED,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LED_GREEN, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Relay_GPIO, GPIO.OUT, initial = GPIO.LOW)


