import sys
import json
from Bootloader import Bootloader
from Fuelsensor_interface import Fuelsensor_interface
from Fuelsensor_interface import Params
import time

#print sys.argv[1]

y = json.loads(sys.argv[1])
ip= y['ip']
pulse_width = y["pulse_width"]
#num_pulses=y["num_pulses"]
#port = y["port"]


print "ip: " + y["ip"]
print "pulse_width " + str(y["pulse_width"])
# #print "arg 2: " + sys.argv[2]

b = Bootloader(ip,5000)
fs = Fuelsensor_interface(ip,5000)
params = Params(fs)
params.sdft_i_min.interface.connect()


params.pulse_width.set_value(pulse_width)

print "pulse_width", params.pulse_width.value
