
import os
import sys
import time
from Fuelsensor_interface import Fuelsensor_interface
from Bootloader import Bootloader
b = Bootloader('192.168.100.187',5000)

if len(sys.argv) == 3:
    fs = Fuelsensor_interface(str(sys.argv[1]), int(sys.argv[2]))
else:
    fs = Fuelsensor_interface("192.168.100.187",5000)
print "conectando"
#fs.connect()
print "solicitando altura"
#fs.get_height()
#fs.backup_timeseries() # ver porque se pega la respuesta aqui, ver que hay en la interfaz serial o bien debugear el codigo, programando con el pickit 2.
#fs.get_pos()
#data_heigth= []
#data=[]
#ahora = time.strftime("%c")

#for i in range(1,50):
while True:
	try:
		print "conectando...."
		fs.connect() 
		print "conectado."
		f = open("archivo.txt", "a+")
		print "archivo abierto"
		localtime = time.asctime( time.localtime(time.time()))
		#data.append(fs.get_height)
	
		f.write(str(fs.get_height())+" "+localtime+ "\n")
		print "altura correcta"
	except:
		print "except"
		time.sleep(3)

		b.connect()

		b.jump_to_app()
		print "saltando a api FS"
#print "Jump to app"

		b.close_socket()
		print "close socket b"


	print "close socket..."
	f.close()
	fs.close_socket()
	time.sleep(2)

	

