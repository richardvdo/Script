#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os


while True:
    time.sleep(0.1)
    os.system("systemctl poweroff")
