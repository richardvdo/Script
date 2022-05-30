#!/usr/bin/python

from datetime import datetime
from sqlite3 import Timestamp
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

SERVEUR = '192.168.1.61'
compteur_principal = 0.0
compteur = 0



def cb_compteur_principal(channel):
    global compteur
    client = mqtt.Client()
    client.connect(SERVEUR, 1883, 60)
    client.loop_start()
    insertline = '{{"timestamp": "\'%s\'" , "watt": 1, "total": "\'%s\'" }}'
    var = (datetime.timestamp(datetime.now()), compteur)
    new_line = insertline % var
    topic = ("capteur/electrique/solaire/puissance")
    client.publish(topic, new_line, 1)
    client.loop_stop()
    client.disconnect()
    compteur = compteur + 1


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18, GPIO.FALLING, callback=cb_compteur_principal, bouncetime=70)

while True:
    time.sleep(0.1)
