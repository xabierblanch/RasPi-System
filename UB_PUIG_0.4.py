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

ID = "RasPi04_"

#PARÀMETRE CAPTURA (NUMERO DE CAPTURES A FER INSTANTANEAMENT)

captures = 15

#########################################################################
#########################################################################

print(datetime.datetime.now().strftime("Hora: %H:%M Data: %d/%m/%Y"))
print()

# assignacio de variables
camera = PiCamera()

# propietats de la captura fotografica
camera.resolution = (3280, 2464)
camera.meter_mode = 'spot'
camera.iso = 100
sleep(3)
camera.exposure_mode = 'off'
camera.awb_mode = 'auto'
sleep(3)
camera.sharpness = 50

arrel_directori_directe = "/home/pi/" + ID + "Puigcercos_filetransfer/"
path_directe = "/home/pi/" + ID + "Puigcercos_filetransfer"
arrel_directori_final = "/home/pi/" + ID + "Puigcercos/"
path_final = "/home/pi/" + ID + "Puigcercos"

def directori():
	try:
		os.makedirs(arrel_directori_directe)
		os.makedirs(arrel_directori_final)
	except:
		print("Les carpetes  " + ID + "Puigcercos i " + ID + "Puigecercos_filetransfer ja existeixen")
	os.chdir(arrel_directori_directe)

def fotografia(count):
	data = datetime.datetime.now().strftime('%Y%m%d_%H%M')
	try:
		camera.capture(arrel_directori_directe + ID + data + '_' + str(count) + '.jpg', format='jpeg', quality=100)
		print ('Captura ' + data + '_' + str(count) + ' realitzada amb exit')
	except:
		print ('Error de PiCAMERA')

def dropbox_upload():
	if os.listdir(path_directe) == []:
		print("No hi ha fitxers a la carpeta " + ID + "_Puigcercos_filetransfer per pujar al Dropbox")
	else:
		for file in os.listdir(path_directe):
			f=open(arrel_directori_directe + file, 'rb')
			try:
				dbx = dropbox.Dropbox("TOKEN")
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

directori()
print()
borrar_fitxers()
print()
count=1
for count in range (1, captures+1):
	fotografia(count)
	sleep(1)
	count=count + 1
print()
sleep(5)
try:
	dropbox_upload()
except:
	print("Error DROPBOX - Error en la càrrega de fitxers a Dropbox")
print()
print("Codi finalitzat")
print("******************************************************************")
