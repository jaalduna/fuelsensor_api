from Bootloader import Bootloader
import sys

b = Bootloader()
b.read_version()
b.connect()
if len(sys.argv) == 1:
    b.program_file('aiko1_enero.hex')
else
    b.program_file(sys.argv[1])
b.close_socket()
b.connect()
b.jump_to_app()
b.close_socket()
