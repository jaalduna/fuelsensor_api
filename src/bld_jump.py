from Bootloader import Bootloader
b = Bootloader('192.168.0.100',5000)
b.read_version()
b.connect()
b.jump_to_app()
b.close_socket()
