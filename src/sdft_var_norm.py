import sys
import json
from Bootloader import Bootloader
from Fuelsensor_interface import Fuelsensor_interface
from Fuelsensor_interface import Params
import time

#print sys.argv[1]

y = json.loads(sys.argv[1])
ip= y['ip']
sdft_var_norm = y["sdft_var_norm"]
#num_pulses=y["num_pulses"]
#port = y["port"]


print "ip: " + y["ip"]
print "sdft_var_norm " + str(y["sdft_var_norm"])
# #print "arg 2: " + sys.argv[2]

b = Bootloader(ip,5000)
fs = Fuelsensor_interface(ip,5000)
params = Params(fs)
params.sdft_i_min.interface.connect()


params.sdft_var_norm.set_value(sdft_var_norm)
print "sdft_var_norm", params.sdft_var_norm.value
