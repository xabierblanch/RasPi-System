import os
import dropbox

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
           print('log', res.name, 'loaded')
        except dropbox.exceptions.ApiError as err:
           print('*** API error', err)
           return none
    return res

dropbox_upload(token, path)
