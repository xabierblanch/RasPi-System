import os
import dropbox

arrel_directori = '/home/pi/logs/'

def dropbox_upload():
    
    for file in os.listdir('/home/pi/logs'):
        f=open(arrel_directori + file, 'rb')
        try:
           dbx = dropbox.Dropbox("XAM6jFayu0AAAAAAAAAr3FYBgoNjm8t1dYX3olkB6YLMxnEbJhnfUvpLF0zhd7YN")
           res=dbx.files_upload(f.read(),'/log/' + file, mode=dropbox.files.WriteMode.overwrite)
           print('log', res.name, 'penjat correctament')
        except dropbox.exceptions.ApiError as err:
           print('*** API error', err)
           return none
    return res

dropbox_upload()
    
