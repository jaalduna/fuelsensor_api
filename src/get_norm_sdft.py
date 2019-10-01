import sys
from Fuelsensor_interface import Fuelsensor_interface
import time
import matplotlib.pyplot as plt
import struct
import pickle

if len(sys.argv) == 6:
    ip = str(sys.argv[1])
    port = int(sys.argv[2])
    length = int(sys.argv[3])
    packet_size = int(sys.argv[4])
    data_file = str(sys.argv[5])
else:
    print "not enought parameters, using default"
    ip = '192.168.100.187'
    port = 5000
    length = 10000
    packet_size = 50
    data_file = 'sdft_data'

fs = Fuelsensor_interface(ip,port)
fs.connect()
print "backup_timeseries"
fs.bk_timeseries()
time.sleep(1)
print "get_complete_norm_sdft"
data = fs.get_complete_sdft_echo(length,packet_size)
fs.close_socket()

data_norm = []
for i in range(0,length/4):
    new_data = struct.unpack('<f', data[i*4:(i+1)*4])
    # if (new_data[0] > 1 or new_data[0] < -1):
    #     print "new_data:" + str(new_data)
    #     pass
    #     new_data = (0.5,1)
    data_norm.append(new_data[0])
#print len(data_norm)

#for i in range(1,len(data_norm)):
#    print data_norm[i]

plt.plot(data_norm)
plt.grid(True)
plt.title('sdft vs time')
plt.ylabel('norm sdft')
plt.show()


with open(data_file, 'w') as f:  # Python 3: open(..., 'wb')
    pickle.dump([data_norm], f) 