from Bootloader import Bootloader
import sys
print sys.argv[0]
print 'number', len(sys.argv)
b = Bootloader('172.19.6.187',1024)
b.read_version()
b.connect()
if len(sys.argv) == 1:
    b.program_file('./firmware/aiko1.X.production.hex')
else:
    b.program_file(str(sys.argv[1]))
b.close_socket()
b.connect()
b.jump_to_app()
b.close_socket()
