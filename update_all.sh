#!/bin/sh
sshpass -p 66446644 ssh pi@192.168.1.54 /home/pi/scripts/update.sh &
sshpass -p 66446644 ssh pi@192.168.1.55 /home/pi/scripts/update.sh &
sshpass -p 66446644 ssh pi@192.168.1.58 /home/pi/scripts/update.sh &
sshpass -p 66446644 ssh pi@192.168.1.232 /home/pi/scripts/update.sh &
sudo dnf -y distro-sync && sudo dnf -y update && sudo dnf -y upgrade && sudo dnf -y autoremove &
sshpass -p 66446644 ssh pi@192.168.1.92 /home/pi/scripts/update.sh &
sshpass -p 66446644 ssh pi@192.168.1.62 /home/pi/scripts/update.sh &
sshpass -p 66446644 ssh pi@192.168.1.65 /home/pi/scripts/update.sh &
sshpass -p 66446644 ssh pi@192.168.2.198 /home/pi/scripts/update.sh &

