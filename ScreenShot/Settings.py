#Settings.py
try: 
	from local_settings import *
except ImportError as e:
	pass

# import configparser
# config = configparser.ConfigParser()
# config.read('screenshot_settings.cfg')