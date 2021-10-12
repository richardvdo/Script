#!/bin/sh
sshpass -p 66446644 sudo ssh pi@192.168.1.54 /home/pi/scripts/update.sh &
sshpass -p 66446644 sudo ssh pi@192.168.1.55 /home/pi/scripts/update.sh &
sshpass -p 66446644 sudo ssh pi@192.168.1.58 /home/pi/scripts/update.sh &
sshpass -p 66446644 sudo ssh pi@192.168.1.92 /home/pi/scripts/update.sh &
pihole
