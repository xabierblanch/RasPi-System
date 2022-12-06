#!/bin/bash
# file: afterStartup.sh
#
# This script will be executed in background after Witty Pi 3 gets initialized.
# If you want to run your commands after boot, you can place them here.
#
#python3 /home/pi/raspi.py >> /media/usb/raspi.log
python3 /home/pi/main.py
