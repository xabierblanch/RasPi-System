#! /bin/bash

python3 /home/pi/Scripts/UB_PUIG_0.4.py >> /home/pi/logs/script.log

python3 /home/pi/Scripts/upload_logs.py

gpio -g mode 4 out
gpio -g write 4 0

# Final de l'escript



