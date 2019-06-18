import sys
from Bootloader import Bootloader
<<<<<<< HEAD
b = Bootloader('192.168.0.100',5000)
=======
if len(sys.argv) == 3:
    b = Bootloader(str(sys.argv[1]), int(sys.argv[2]))
else:
    b = Bootloader()
>>>>>>> 06f9cbbc17af44e520c304c4856eeb3107e4fb0e
b.read_version()
b.connect()
b.jump_to_app()
b.close_socket()
