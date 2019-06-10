from Bootloader import Bootloader
b = Bootloader('172.19.6.187',1024) #config conversor planet  
#b = Bootloader('192.168.0.10',5000) 
print b.TCP_IP
b.read_version()

