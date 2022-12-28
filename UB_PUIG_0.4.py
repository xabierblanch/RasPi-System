#! /usr/bin/python

## PROGRAMA DE CAPTURA DE FOTOGRAFIES AUTOMATICA ##
##########  GRUP DE RECERCA RISKNAT  ##############
########## UNIVERSITAT DE  BARCELONA  #############
###############  XABIER BLANCH  ###################

# importacio de la llibreria de control de la camara
from picamera import PiCamera
from time import sleep
import datetime
import shutil
import dropbox
import os
import time

print('\nEXECUCIO DEL SCRIPT UB_PUIG_0.4 DE LA UNIVERSITAT DE BARCELONA\n')
print('Grup de Recerca RISKNAT. Departament de Dinamica de la Terra i de lOcea')
print('Desenvolupat per: Xabier Blanch Gorriz\n')

#########################################################################
#########################################################################

#IDENTIFICADOR DEL SISTEMA -> IMPORTANT CANVIAR-HO CORRECTAMENT

ID = "RPi_00_"

#PARÀMETRE CAPTURA (NUMERO DE CAPTURES A FER INSTANTANEAMENT)

captures = 5

#TOKEN (DROPBOX)

token = ""

#########################################################################
#########################################################################

print(datetime.datetime.now().strftime("Hora: %H:%M Data: %d/%m/%Y"))
print()

arrel_directori_directe = "/home/pi/" + ID + "Puigcercos_filetransfer/"
path_directe = "/home/pi/" + ID + "Puigcercos_filetransfer"
arrel_directori_final = "/home/pi/" + ID + "Puigcercos/"
path_final = "/home/pi/" + ID + "Puigcercos"

def setup_camera():
	try:
		camera = PiCamera()
		camera.meter_mode = 'average'
		camera.awb_mode = 'auto'
		camera.iso = 100
		sleep(3)

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

def directori():
	try:
		os.makedirs(arrel_directori_directe)
		os.makedirs(arrel_directori_final)
	except:
		print("Les carpetes  " + ID + "Puigcercos i " + ID + "Puigecercos_filetransfer ja existeixen")
	os.chdir(arrel_directori_directe)

def fotografia(count, camera):
	data = datetime.datetime.now().strftime('%Y%m%d_%H%M')
	try:
		camera.capture(arrel_directori_directe + ID + data + '_' + str(count) + '.jpg', format='jpeg', quality=100)
		print ('Captura ' + data + '_' + str(count) + ' realitzada amb exit')
	except:
		print ('Error de PiCAMERA')

def dropbox_upload(token):
	if os.listdir(path_directe) == []:
		print("No hi ha fitxers a la carpeta " + ID + "_Puigcercos_filetransfer per pujar al Dropbox")
	else:
		for file in os.listdir(path_directe):
			f=open(arrel_directori_directe + file, 'rb')
			try:
				dbx = dropbox.Dropbox(token)
				res=dbx.files_upload(f.read(),'/' + file)
				shutil.move(arrel_directori_directe + file, arrel_directori_final + file)
				print('fitxer', res.name, 'penjat correctament i mogut a la carpeta ' + ID + 'Puigcercos')
			except dropbox.exceptions.ApiError as err:
				print('*** API error', err)
				return none
		return res

def borrar_fitxers():
	data_actual = time.time()
	eliminats = 0
	for fitxer in os.listdir(path_final):
		data_fitxer = os.path.getmtime(arrel_directori_final + fitxer)
		if ((data_actual - data_fitxer) / (24*3600)) >= 15:
			os.unlink(arrel_directori_final + fitxer)
			eliminats = eliminats + 1
	print("S'han eliminat " + str(eliminats) + " fitxers per alliberar espai a la targeta de memòria")

# SEQUENCIA DE FUNCIONS - PROGRAMA PRINCIPAL

camera = setup_camera()
directori()
borrar_fitxers()
count=1
for count in range (1, captures+1):
	fotografia(count, camera)
	sleep(1)
	count=count + 1
print()
sleep(3)
try:
	dropbox_upload(token)
except:
	print("Error DROPBOX - Error en la càrrega de fitxers a Dropbox")
print()
print("Codi finalitzat")
print("******************************************************************")
