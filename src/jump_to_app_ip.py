import sys

from Bootloader import Bootloader
from Fuelsensor_interface import Fuelsensor_interface
from Fuelsensor_interface import Params
import time
import json

#print sys.argv[1]
y = json.loads(sys.argv[1])
ip= y['ip']
#num_pulses=y["num_pulses"]
#port = y["port"]


#print "ip: " + y["ip"]


fs = Fuelsensor_interface(ip,5000)
b = Bootloader(ip,5000)


b.connect()
#b.read_version()
b.jump_to_app()
#print "Jump to app"

b.close_socket()
