from Bootloader import Bootloader
b = Bootloader()
b.read_version()
b.connect()
b.program_file('aiko1_enero.hex')
b.close_socket()
b.connect()
b.jump_to_app()
b.close_socket()
