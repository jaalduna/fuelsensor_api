import sys
from Bootloader import Bootloader
if len(sys.argv) == 3:
    b = Bootloader(str(sys.argv[1]), int(sys.argv[2]))
else:
    b = Bootloader('192.168.100.1',5000) #config conversor planet  
#b = Bootloader('192.168.0.10',5000) 
#print b.TCP_IP
#print b.TCP_PORT
#b.jump_to_bld()
b.read_version()
#b.connect()
#b.jump_to_app()
#b.close_socket()
