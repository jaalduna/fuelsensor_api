from Bootloader import Bootloader
b = Bootloader()
b.read_version()
b.connect()
b.jump_to_app()
b.close_socket()