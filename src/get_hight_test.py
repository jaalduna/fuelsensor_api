import sys
from Fuelsensor_interface import Fuelsensor_interface
import time
if len(sys.argv) == 3:
    fs = Fuelsensor_interface(str(sys.argv[1]), int(sys.argv[2]))
elif len(sys.argv) == 2:
    fs = Fuelsensor_interface(str(sys.argv[1]), 5000)
else:
    fs = Fuelsensor_interface('192.168.148.1',5000)
#print "conectando"
fs.connect()
fs.get_app_version()
fs.get_height()
fs.get_pos()
fs.close_socket()


