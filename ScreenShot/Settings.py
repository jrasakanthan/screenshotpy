#Settings.py
import os, sys

# module_path = os.path.abspath(os.path.join('..'))
# if module_path not in sys.path:
#     sys.path.append(module_path)

# try: 
# 	from local_settings import *
# except ImportError as e:
# 	print("something went wrong")
# 	pass

# DURATION = '1m'
# INTERVAL = '20s'
# DIRECTORY = 'Images'
# FILENAME_FORMAT = ''
# FORMAT = 'jpg'
# DISPLAYS = [1]

import configparser
config = configparser.ConfigParser()
config.read('local_settings.cfg')

DURATION = config.get('local settings', 'DURATION')
INTERVAL = config.get('local settings', 'INTERVAL')
#DIRECTORY = config.get('local settings', 'DIRECTORY')
#FILENAME_FORMAT = config.get('local settings', 'FILENAME_FORMAT')
IMAGE_FORMAT = config.get('local settings', 'IMAGE_FORMAT')
DISPLAYS = [int(i) for i in config.get('local settings', 'DISPLAYS').split(',')]