from Fuelsensor_interface import Fuelsensor_interface
import sys
if len(sys.argv) == 2:
    fs = Fuelsensor_interface(str(sys.argv[1]), 5000)
else:
    fs = Fuelsensor_interface('192.168.0.100',5000)

fs.use_serial('COM5')
while True:
	try:
		fs.connect()
		data = fs.receive()
		fs.print_modbus(data)
	except Exception as e:
		print "Exception: ",e
	finally:
		fs.close_socket()
