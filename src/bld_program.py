from Bootloader import Bootloader
import sys
if len(sys.argv) >= 3:
    b = Bootloader(str(sys.argv[1]), int(sys.argv[2]))
else:
    b = Bootloader('192.168.100.187',5000)
b.read_version()
b.connect()
if len(sys.argv) == 4:
    b.program_file(str(sys.argv[3]))
else:
    print "programming default .hex file"
    b.program_file('./firmware/aiko1.X.production.hex')
    
b.close_socket()
b.connect()
b.jump_to_app()
b.close_socket()
