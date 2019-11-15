import sys
from Bootloader import Bootloader

if len(sys.argv) == 3:
    b = Bootloader(str(sys.argv[1]), int(sys.argv[2]))
elif len(sys.argv) == 2:
    b = Bootloader(str(sys.argv[1]), 5000)
else:
    b = Bootloader('192.168.100.1', 5000)
#b.read_version()
b.connect()
b.jump_to_app()
b.close_socket()

