import sys
import time
from Bootloader import Bootloader

b = Bootloader('172.19.6.188',5000) #config conversor wiznet CDH48 

while True:
	try:
		b.read_version()
	except Exception as e:
		print e, type(e)
	finally:
		time.sleep(5)

