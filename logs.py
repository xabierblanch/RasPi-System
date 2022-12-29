import os
import dropbox
import shutil

#DROPBOX USER INFORMATION

app_key = 'so8ksun3q9jq9ob'
app_secret = 'arssteb8pv6blxb'
refresh_token = 'Kpm3y-06pRcAAAAAAAAAAWzz07NrxAkpHOLQmy6QwyAeVKyhwQk-VAeXZXtCExcD'

#############################################################

def dropbox_upload(app_key, app_secret, refresh_token, path):
	for file in os.listdir(path):
        	f=open(os.path.join(path,file), 'rb')
        	try:
           		dbx = dropbox.Dropbox(app_key=app_key, app_secret=app_secret, oauth2_refresh_token=refresh_token)
           		res=dbx.files_upload(f.read(),'/log/' + file, mode=dropbox.files.WriteMode.overwrite)
           		print('log', res.name, 'loaded to Dropbox')
        	except dropbox.exceptions.ApiError as err:
           		print('*** API error', err)
           		return none

def copylogs(path):
	try:
		shutil.copyfile('/home/pi/wittypi/wittyPi.log', os.path.join(path, 'wittyPi.log'))
		print('WittyPi log moved to log folder')
	except:
		print('ERROR: WittyPi log files')

path = '/home/pi/logs'
copylogs(path)
dropbox_upload(app_key, app_secret, refresh_token, path)
