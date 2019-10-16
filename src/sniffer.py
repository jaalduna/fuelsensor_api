from Fuelsensor_interface import Fuelsensor_interface

fs = Fuelsensor_interface('172.19.6.187',5000)

while True:
	try:
		fs.connect()
		data = fs.socket.recv(1024)
		fs.print_modbus(data)
	except Exception as e:
		print e
	finally:
		fs.close_socket()
