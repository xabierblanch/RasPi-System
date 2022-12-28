import os
import dropbox
import shutil

##################### DROPBOX TOKEN ##########################

token = ''

#############################################################

path = '/home/pi/logs'

def dropbox_upload(token, path):
    for file in os.listdir(path):
        f=open(os.path.join(path,file), 'rb')
        try:
           dbx = dropbox.Dropbox(token)
           res=dbx.files_upload(f.read(),'/log/' + file, mode=dropbox.files.WriteMode.overwrite)
           print('log', res.name, 'loaded to Dropbox')
        except dropbox.exceptions.ApiError as err:
           print('*** API error', err)
           return none
    return res

def copylogs(path):
	try:
		shutil.copyfile('/home/pi/wittypi/wittyPi.log', os.path.join(path, 'wittyPi.log')
		print('WittyPi log moved to log folder')
	except:
		print('ERROR: WittyPi log files')

os.makedirs(path, exist_ok=True)
copylogs(path)
dropbox_upload(token, path)
