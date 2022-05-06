#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import datetime
import paho.mqtt.client as mqtt

SERVEUR = '192.168.1.61'
pin = 26

def alerte_flamme(channel):

    if GPIO.input(pin):
        now = datetime.datetime.now()
        client = mqtt.Client()
        client.connect(SERVEUR, 1883, 60)
        client.loop_start()
        insertline = '{"alerte": {"type": "incendie", "info": {"type": "Flamme detectée", "emplacement": "garage", "equipement": "imprimante 3D", "timestamp": "\'%s\'", "ack_alerte": false } }}'
        new_line = insertline % now
        topic = ("capteur/incendie/alerte")
        client.publish(topic, new_line, 1)
        client.loop_stop()
        client.disconnect()

    else:
        now = datetime.datetime.now()
        client = mqtt.Client()
        client.connect(SERVEUR, 1883, 60)
        client.loop_start()
        insertline = '{"alerte": {"type": "incendie", "info": {"type": "Acquittement flamme detectée", "emplacement": "garage", "equipement": "imprimante 3D", "timestamp": "\'%s\'", "ack_alerte": true } }}'
        new_line = insertline % now
        topic = ("capteur/incendie/alerte")
        client.publish(topic, new_line, 1)
        client.loop_stop()
        client.disconnect()

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(pin, GPIO.BOTH, callback=alerte_flamme, bouncetime=500)



while True:
    time.sleep(1)
