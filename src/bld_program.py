from Bootloader import Bootloader
import sys
<<<<<<< HEAD
print sys.argv[0]
print 'number', len(sys.argv)
b = Bootloader('172.19.6.187',5000)
=======
if len(sys.argv) == 3:
    b = Bootloader(str(sys.argv[1]), int(sys.argv[2]))
else:
    b = Bootloader()
>>>>>>> 06f9cbbc17af44e520c304c4856eeb3107e4fb0e
b.read_version()
b.connect()
if len(sys.argv) > 3:
    b.program_file(str(sys.argv[3]))
else:
    b.program_file('./firmware/aiko1.X.production.hex')
    
b.close_socket()
b.connect()
b.jump_to_app()
b.close_socket()
