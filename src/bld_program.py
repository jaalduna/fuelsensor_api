from Bootloader import Bootloader
import sys
print sys.argv[0]
print 'number', len(sys.argv)
b = Bootloader()
b.read_version()
b.connect()
if len(sys.argv) == 1:
    b.program_file('aiko1_marzo.hex')
else:
    b.program_file(str(sys.argv[1]))
b.close_socket()
b.connect()
b.jump_to_app()
b.close_socket()
