import sys
from Fuelsensor_interface import Fuelsensor_interface
import time
import matplotlib.pyplot as plt
import struct
import pickle

#Default parameters
ip = '192.168.100.1'
port = 5000
length = 1200
packet_size = 50
data_file = 'data'

if len(sys.argv) >= 2:
    ip = str(sys.argv[1])
    if len(sys.argv) >= 3:
        length = int(sys.argv[2])

fs = Fuelsensor_interface(ip,port)
fs.connect()
print "backup_timeseries"
fs.bk_timeseries()
time.sleep(1)
print "get_complete_fifo_buffer"
data = fs.get_complete_fifo_buffer(length,packet_size)
fs.close_socket()

data_norm = []
for i in range(0,length/2):
    new_data = struct.unpack('<H', data[i*2:(i+1)*2])
    # if (new_data[0] > 1 or new_data[0] < -1):
    #print "new_data:" + str(new_data)
    #     pass
    #     new_data = (0.5,1)
    data_norm.append(new_data[0])
#print len(data_norm)

#for i in range(1,len(data_norm)):
#    print data_norm[i]

plt.plot(data_norm)
plt.grid(True)
plt.title('sdft histo')
plt.ylabel('Counts')
plt.show()


with open(data_file, 'w') as f:  # Python 3: open(..., 'wb')
    pickle.dump([data_norm], f) 