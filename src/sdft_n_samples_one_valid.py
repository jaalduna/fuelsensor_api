import sys
import json
from Bootloader import Bootloader
from Fuelsensor_interface import Fuelsensor_interface
from Fuelsensor_interface import Params
import time

#print sys.argv[1]

y = json.loads(sys.argv[1])
ip= y['ip']
sdft_n_samples_one_valid = y["sdft_n_samples_one_valid"]
#num_pulses=y["num_pulses"]
#port = y["port"]


print "ip: " + y["ip"]
print "sdft_n_samples_one_valid " + str(y["sdft_n_samples_one_valid"])
# #print "arg 2: " + sys.argv[2]

b = Bootloader(ip,5000)
fs = Fuelsensor_interface(ip,5000)
params = Params(fs)
params.sdft_i_min.interface.connect()


params.sdft_n_samples_one_valid.set_value(sdft_n_samples_one_valid)
print "sdft_n_samples_one_valid", params.sdft_n_samples_one_valid.value
