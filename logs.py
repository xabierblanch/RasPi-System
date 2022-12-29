import os
import dropbox
import shutil

#DROPBOX USER INFORMATION

app_key = 'so8ksun3q9jq9ob'
app_secret = 'arssteb8pv6blxb'

#############################################################

def dropbox_token(app_key, app_secret):

	# Create a new instance of the WebAuth class
	web_auth = dropbox.oauth2.WebAuthNoRedirect(app_key, app_secret)

        # Use the app key and secret to get a long-lived access token
        try:
            token, user_id, url_state = web_auth.finish(authorization_code)
        except Exception as e:
            print(f'Error: {e}')

	return token

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

def copylogs(path):
	try:
		shutil.copyfile('/home/pi/wittypi/wittyPi.log', os.path.join(path, 'wittyPi.log'))
		print('WittyPi log moved to log folder')
	except:
		print('ERROR: WittyPi log files')

path = '/home/pi/logs'
token = dropbox_token(app_key, app_secret)
copylogs(path)
dropbox_upload(token, path)
