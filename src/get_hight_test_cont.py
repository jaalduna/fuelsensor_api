from Fuelsensor_interface import Fuelsensor_interface
fs = Fuelsensor_interface()

while(1):
	fs.connect()
	fs.get_height()
	#fs.backup_timeseries() # ver porque se pega la respuesta aqui, ver que hay en la interfaz serial o bien debugear el codigo, programando con el pickit 2.
	#fs.get_pos()
	fs.close_socket()
