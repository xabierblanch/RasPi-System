#! /usr/bin/python

### LIGHT TIME-LAPSE RASPBERRY PI CAMERA SYSTEM ###
############ RISKNAT RESEARCH GROUP ###############
############ UNIVERSITY OF BARCELONA ##############
################ XABIER BLANCH ####################

from picamera import PiCamera
from time import sleep
import datetime
import shutil
import dropbox
import os
import time

#########################################################################
#########################################################################

#SYSTEM IDENTIFIER

ID = "RPi_test"

#NUMBER OF CAPTURES (BURST MODE)

burst_num = 5

#DROPBOX USER INFORMATION (check official Dropbox API)

app_key = ''
app_secret = ''
refresh_token = '' #https://github.com/dropbox/dropbox-sdk-python/blob/main/example/oauth/commandline-oauth.py

#BACKUP DAYS

backup_days = 30

#########################################################################
#########################################################################

def setup_camera():
	try:
		camera = PiCamera()
		camera.meter_mode = 'average'
		camera.awb_mode = 'auto'
		camera.iso = 100
		sleep(2)

		if camera.revision == 'imx477':
			camera.resolution = (4056,3040)
			print(get_time() + f'Camera RPi HQ detected. Resolution: {camera.resolution}')
		elif camera.revision == 'imx219':
			camera.resolution = (3280, 2464)
			print(get_time() + f'Camera RPi V2 detected. Resolution: {camera.resolution}')
		else:
			camera.resolution = (2592, 1944)
			print(get_time() + f'Camera RPi V1 detected. Resolution: {camera.resolution}')
	except:
		print(get_time() + 'ERROR: Camera module not found')
	return camera

def paths():
	os.makedirs(path_temp, exist_ok=True)
	os.makedirs(path_backup, exist_ok=True)
	print(get_time() + f"The {path_temp} and {path_backup} folders were succesfuly created")

def image_capture(count, camera, path_temp):	
	date = datetime.datetime.now().strftime('%Y%m%d_%H%M')
	try:
		save_file = os.path.join(path_temp, ID + '_' + date + '_' + str(count) + '.jpg')
		camera.capture(save_file, format='jpeg', quality=100)
		print(get_time() + 'Image ' + ID + '_' + date + '_' + str(count) + '.jpg' + ' successfully captured')
	except:
		print(get_time() + 'ERROR: Image capture fail')	
		
def dropbox_upload(refresh_token, app_key, app_secret, path_temp, path_backup):
	try:
		if os.listdir(path_temp) == []:
			print(get_time() + f"There are no files in the {path_temp} folder to upload to Dropbox")
		else:
			for file in os.listdir(path_temp):
				f=open(os.path.join(path_temp,file), 'rb')
				try:
					dbx = dropbox.Dropbox(app_key=app_key, app_secret=app_secret, oauth2_refresh_token=refresh_token)
					res=dbx.files_upload(f.read(),'/' + file)
					shutil.move(os.path.join(path_temp, file), os.path.join(path_backup, file))
					print(get_time() + f'{res.name} successfully uploaded to Dropbox')
				except dropbox.exceptions.ApiError as err:
					print(get_time() + '*** API error', err)
					return none
			return res
	except:
		print(get_time() + "Error DROPBOX - Error in the transfer of files to Dropbox")

def delete_backup(path_backup, backup_days):
	today = time.time()
	deleted = 0
	for file in os.listdir(path_backup):
		data_file = os.path.getmtime(os.path.join(path_backup, file))
		if ((today - data_file) / (24*3600)) >= backup_days:
			os.unlink(os.path.join(path_backup, file))
			deleted = deleted + 1
	print(get_time() + f"{deleted} files have been deleted from backup folder ({backup_days} days backup)")

def get_time():
	date = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S] ')
	return date

# MAIN CODE
path_temp = "/home/pi/" + ID + "_filetransfer"
path_backup = "/home/pi/" + ID + "_backup"
camera = setup_camera()
paths()
delete_backup(path_backup, backup_days)
count=1
for count in range (1, burst_num+1):
	image_capture(count, camera, path_temp)
	sleep(1)
	count=count + 1
sleep(1)
res = dropbox_upload(refresh_token, app_key, app_secret, path_temp, path_backup)
print()
