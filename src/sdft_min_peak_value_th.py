import sys
import json
from Bootloader import Bootloader
from Fuelsensor_interface import Fuelsensor_interface
from Fuelsensor_interface import Params
import time

#print sys.argv[1]

y = json.loads(sys.argv[1])
ip= y['ip']
sdft_min_peak_value_th = y["sdft_min_peak_value_th"]
#num_pulses=y["num_pulses"]
#port = y["port"]


print "ip: " + y["ip"]
print "sdft_min_peak_value_th " + str(y["sdft_min_peak_value_th"])
# #print "arg 2: " + sys.argv[2]

b = Bootloader(ip,5000)
fs = Fuelsensor_interface(ip,5000)
params = Params(fs)
params.sdft_i_min.interface.connect()


params.sdft_min_peak_value_th.set_value(sdft_min_peak_value_th)

print "sdft_min_peak_value_th", params.sdft_min_peak_value_th.value
