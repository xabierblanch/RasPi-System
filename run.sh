#! /bin/bash

#run main script
python3 /home/pi/scripts/main_v1.1.py >> /home/pi/logs/script.log

#move and upload logs
python3 /home/pi/scripts/logs.py

#shutdown RPi
gpio -g mode 4 out
gpio -g write 4 0
