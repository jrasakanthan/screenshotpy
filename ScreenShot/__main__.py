#__main__.py
from ScreenShot import capture_save_sequence
import sys

def main(args=None):
	if args is None:
		args = sys.argv[1:]
	capture_save_sequence()

if __name__ == '__main__':
	main()