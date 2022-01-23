#!/bin/sh

PROCESS_NUM=$(systemctl status solaired.service *sensor.service teleinfo.service | grep active | wc -l)

if [ $PROCESS_NUM -ne 4 ]
then 
        /bin/false
        echo "erreur service arrete"
	exit 1
fi
       	exit 0
