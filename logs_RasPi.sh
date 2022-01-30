#!/bin/bash

echo "************** XBG RasPi PUIGCERCOS logs **************" >> /home/pi/logs/log_RasPi_RasPi04.log
echo >> /home/pi/logs/log_RasPi_RasPi04.log
echo "$(date) @ $(hostname)" >> /home/pi/logs/log_RasPi_RasPi04.log
echo >> /home/pi/logs/log_RasPi_RasPi04.log
cat /proc/net/wireless >> /home/pi/logs/log_RasPi_RasPi04.log 
echo >> /home/pi/logs/log_RasPi_RasPi04.log
iwconfig wlan0 >> /home/pi/logs/log_RasPi_RasPi04.log
cpu=$(cat /sys/class/thermal/thermal_zone0/temp)
echo "Temp.CPU => $((cpu/1000))'Cº" >> /home/pi/logs/log_RasPi_RasPi04.log
echo "Temp GPU => $(/opt/vc/bin/vcgencmd measure_temp)" >> /home/pi/logs/log_RasPi_RasPi04.log
echo "CPU $(vcgencmd measure_volts core)'Hz" >> /home/pi/logs/log_RasPi_RasPi04.log
echo "CPU $(vcgencmd measure_clock arm)'Hz" >> /home/pi/logs/log_RasPi_RasPi04.log
echo >> /home/pi/logs/log_RasPi_RasPi04.log >> /home/pi/logs/log_RasPi_RasPi04.log
echo "Us memoria RAM" >> /home/pi/logs/log_RasPi_RasPi04.log 
echo "$(free --mega -t)" >> /home/pi/logs/log_RasPi_RasPi04.log
echo >> /home/pi/logs/log_RasPi_RasPi04.log >> /home/pi/logs/log_RasPi_RasPi04.log
echo "Memoria total disponible" >> /home/pi/logs/log_RasPi_RasPi04.log 
echo "$(df -P --total -Bg -h)" >> /home/pi/logs/log_RasPi_RasPi04.log
echo >> /home/pi/logs/log_RasPi_RasPi04.log
echo "*******************************************************"

cp /home/pi/wittyPi/schedule.log /home/pi/wittyPi/wittyPi.log /home/pi/logs

