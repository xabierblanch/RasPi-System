#! usr/bin/python

### LIGHT TIME-LAPSE RASPBERRY PI CAMERA SYSTEM ###
#####  Juniorprofessur fur Geosensorsysteme  ######
################## TU Dresden  ####################
################  XABIER BLANCH  ##################

from picamera import PiCamera
import datetime
import os
import shutil
import RPi.GPIO as GPIO

#########################################################################
#########################################################################

#DEVICE IDENTIFIER

ID = 'GSS01_'

#NUMBER OF IMAGES (IMAGES ACQUIRED AT EACH BURST)

burst_num = 5

#PATH TO SAVE IMAGES

path='/media/usb'

#########################################################################
#########################################################################

def setup_camera():
	try:
		camera = PiCamera()
		camera.meter_mode = 'average'
		camera.awb_mode = 'auto'
		camera.iso = 100

		if camera.revision == 'imx477':
			camera.resolution = (4056,3040)
			print(get_time() + f'Camera HQ detected. Resolution: {camera.resolution}')
		elif camera.revision == 'imx219':
			camera.resolution = (3280, 2464)
			print(get_time() + f'Camera V2 detected. Resolution: {camera.resolution}')
		else:
			camera.resolution = (2592, 1944)
			print(get_time() + f'Camera V1 detected. Resolution: {camera.resolution}')
	except:
		print(get_time() + 'ERROR: Camera module not found')
	return camera

def image_capture(count, camera):
	date = datetime.datetime.now().strftime('%Y%m%d_%H%M')
	try:
		save_file = os.path.join(path, ID+date+'_'+str(count)+'.jpg')
		camera.capture(save_file, format='jpeg', quality=100)
		print(get_time() + 'Image: ' + date + '_' + str(count) + ' successfully captured')
	except:
		print(get_time() + 'ERROR: Image capture fail')

def copylogs():
	try:
		shutil.copyfile('/home/pi/wittypi/wittyPi.log', '/media/usb/wittyPi.log')
		print(get_time() + 'WittyPi log files copied to USB')
	except:
		print(get_time() + 'ERROR: WittyPi log files')

def shutdown():
	try:
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(4, GPIO.OUT)
		print(get_time() + 'Shutdown command activated')
	except:
		print(get_time() + 'ERROR: Shutdown command')

def get_time():
	date = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S] ')
	return date


# MAIN CODE
print(get_time () + 'TIME-LAPSE LOW-COST SYSTEM')

try:
	camera = setup_camera()
	count=1
	for count in range (1, burst_num+1):
		image_capture(count, camera)
		count=count + 1
except:
	print(get_time() + 'ERROR: Camera and code fail')
camera.close()

copylogs()
shutdown()
