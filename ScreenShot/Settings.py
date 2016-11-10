#Settings.py
try: 
	from local_settings import *
except ImportError as e:
	pass

DURATION = '1m'
INTERVAL = '20s'
DIRECTORY = 'Images'
FILENAME_FORMAT = ''
FORMAT = 'jpg'
DISPLAYS = [1]

# import configparser
# config = configparser.ConfigParser()
# config.read('screenshot_settings.cfg')