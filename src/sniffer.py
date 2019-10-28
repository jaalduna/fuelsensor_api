from Fuelsensor_interface import Fuelsensor_interface
import sys
if len(sys.argv) == 2:
    fs = Fuelsensor_interface(str(sys.argv[1]), 5000)
else:
	print "ingrese una ip"
	exit()

while True:
	try:
		fs.connect()
		data = fs.socket.recv(1024)
		fs.print_modbus(data)
	except Exception as e:
		print e
	finally:
		fs.close_socket()
