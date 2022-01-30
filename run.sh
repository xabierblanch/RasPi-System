#! /bin/bash

sudo sh /home/pi/wittyPi/temp.sh

sudo python3 /home/pi/Scripts/UB_PUIG_0.4.py >> /home/pi/logs/log_Script_RasPi04.log

sh /home/pi/Scripts/logs_RasPi.sh

sudo python3 /home/pi/Scripts/upload_logs.py

gpio -g mode 4 out
gpio -g write 4 0

# Final de l'escript



