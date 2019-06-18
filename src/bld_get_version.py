from Bootloader import Bootloader
b = Bootloader('192.168.0.100',5000) #config conversor planet  
#b = Bootloader('192.168.0.10',5000) 
print b.TCP_IP
b.read_version()


