#!/usr/bin/python

import RPi.GPIO as GPIO
import time

btnOffPin = 20
btnOnPin = 21


def shutdown(channel):
    GPIO.output(btnOnPin, GPIO.LOW)



GPIO.setmode(GPIO.BCM)
GPIO.setup(btnOffPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btnOnPin, GPIO.OUT)
GPIO.add_event_detect(btnOffPin, GPIO.RISING, callback=shutdown, bouncetime=200)
GPIO.output(btnOnPin, GPIO.HIGH)


while True:
    time.sleep(0.1)
