#!/bin/sh

PROCESS_NUM=$(ps -ef | grep gpio_on-off | grep -v "grep" | wc -l)

if [ $PROCESS_NUM -eq 1 ]
then 
	exit 1
else
	python /home/pi/Dev/scripts/gpio_on-off.py
fi
	exit 0
