import sys
from Fuelsensor_interface import Fuelsensor_interface
from Bootloader import Bootloader
import time

if len(sys.argv) == 3:
    fs = Fuelsensor_interface(str(sys.argv[1]), int(sys.argv[2]))
elif len(sys.argv) == 2:
    fs = Fuelsensor_interface(str(sys.argv[1]), 5000)
else:
    fs = Fuelsensor_interface('192.168.100.187',5000)

fs.connect()
fs.reset()
time.sleep(0.2)

fs.jump_to_bld()

fs.close_socket()
