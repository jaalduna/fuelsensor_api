from Bootloader import Bootloader
import sys
if len(sys.argv) == 3:
    ip = str(sys.argv[1])
    file = str(sys.argv[2])
else:
    ip = '192.168.148.1'
    file = './firmware/aiko1.X.production.hex'

b = Bootloader(ip, 5000)
b.read_version()
print "programming ",file,"into",ip
b.program_file(file)
b.connect()
b.jump_to_app()
b.close_socket()
