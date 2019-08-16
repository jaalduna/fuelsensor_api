import sys
import time
from Bootloader import Bootloader

b = Bootloader('172.19.6.188',5000) #config conversor wiznet CDH48 

while True:
	b.connect()
	try:
		b.read_version(False)
	except Exception as e:
		print "Hi"
		print type(e)
	finally:
		b.close_socket()
	time.sleep(5)

