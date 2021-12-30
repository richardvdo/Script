#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os


btnOnPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(btnOnPin, GPIO.OUT)


while True:
    time.sleep(0.1)
    GPIO.output(btnOnPin, GPIO.LOW)
