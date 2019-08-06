import sys
import json
from Bootloader import Bootloader
from Fuelsensor_interface import Fuelsensor_interface
from Fuelsensor_interface import Params
import time
import matplotlib.pyplot as plt
import struct


#print sys.argv[1]

y = json.loads(sys.argv[1])
ip = y['ip']
length = y["length"]
packet_size = y["packet_size"]

#num_pulses=y["num_pulses"]
#port = y["port"]


print "ip: " + y["ip"]
print "length" + int(y["length"])
print "packet_size" + int(y["length"])
# #print "arg 2: " + sys.argv[2]

b = Bootloader(ip,5000)
fs = Fuelsensor_interface(ip,5000)
params = Params(fs)
params.sdft_i_min.interface.connect()

offset = 0
data = fs.get_complete_norm_echo(length,packet_size)
fs.print_modbus(str(data))



data_norm = []
for i in range(0,length/4):
    new_data = struct.unpack('<f', data[i*4:(i+1)*4])

    # if (new_data[0] > 1 or new_data[0] < -1):
    #     print "new_data:" + str(new_data)
    #     pass
    #     new_data = (0.5,1)
    data_norm.append(new_data[0])
print len(data_norm)

for i in range(1,len(data_norm)):
    print data_norm[i]


