import sys
from Bootloader import Bootloader
if len(sys.argv) == 3:
    b = Bootloader(str(sys.argv[1]), int(sys.argv[2]))
else:
    b = Bootloader('192.168.100.187',5000)
b.read_version()
b.connect()
b.jump_to_app()
b.close_socket()
