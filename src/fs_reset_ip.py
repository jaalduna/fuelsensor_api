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

fs.connect()
fs.reset()
print "Reset sucessfull"
time.sleep(0.1)
#fs.send_raw_byte(1)
#fs.backup_timeseries() # ver porque se pega la respuesta aqui, ver que hay en la interfaz serial o bien debugear el codigo, programando con el pickit 2.
#fs.get_pos()
fs.close_socket()
