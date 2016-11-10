from __future__ import print_function

from Settings import *

from ParseTime.ParseTime import parse_time

#creatre a zero based display index
DISPLAYS = [D-1 for D in DISPLAYS]
print (DISPLAYS) 

# from desktopmagic.screengrab_win32 import (
# 	getDisplayRects, saveScreenToBmp, 
# 	saveRectToBmp, getScreenAsImage,
# 	getRectAsImage, getDisplaysAsImages)

from desktopmagic import screengrab_win32 as SGw32 
from operator import itemgetter 
from PIL import Image
import datetime
import time

#entireScreen = getScreenAsImage()
#entireScreen.save('screencapture_entire.png', format='png')

# getDisplayRects()
# returns a list containing tuples with coordinates of each display 
# example (x-ul, y-ul, x-lr, y-lr) where ul and lr refers to upper
# left and lower-right respectively.

#these lambda functions are already in another file :S
time_now = lambda: datetime.datetime.now()
time_end = lambda dt: time_now()+dt
time_str = lambda t: t.strftime('%Y%m%d%H%M%S')

def getDisplayRects(displays):
	monitors = SGw32.getDisplayRects()	# enumerate all displays
	#print(monitors)
	#return itemgetter(*displays)(monitors)
	return [monitors[i] for i in displays]

# return PIL image?
def snap(rect):
	return SGw32.getRectAsImage(rect)

def save(data, filename, format='png'):
	data.save(filename, format)

#filename format to use
def capture_save(displays):
	monitors = getDisplayRects(displays)
	for m, d in zip(monitors, displays):
		image = snap(m)
		filename = 'screenshot_display-%02d_%s.%s'%(d, time_str(time_now()), IMAGE_FORMAT)
		save(image, filename)

#'screenshot_display-%02d_%s.png'%(d, time_str(time_now()))
def capture_save_sequence():
	tend = time_end(parse_time(DURATION))
	print(tend)
	while time_now() < tend:
		capture_save(DISPLAYS)
		time.sleep(parse_time(INTERVAL).total_seconds())

if __name__ == '__main__':
	capture_save_sequence()