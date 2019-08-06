import sys
import json
from Bootloader import Bootloader
from Fuelsensor_interface import Fuelsensor_interface
from Fuelsensor_interface import Params
import time

#print sys.argv[1]

y = json.loads(sys.argv[1])
ip= y['ip']
sdft_i_min = y["sdft_i_min"]
#num_pulses=y["num_pulses"]
#port = y["port"]


print "ip: " + y["ip"]
print "sdft_i_min " + str(y["sdft_i_min"])
# #print "arg 2: " + sys.argv[2]

b = Bootloader(ip,5000)
fs = Fuelsensor_interface(ip,5000)
params = Params(fs)
params.sdft_i_min.interface.connect()


params.sdft_i_min.set_value(sdft_i_min)
print "sdft_i_min", params.sdft_i_min.value
