import time 

#from Bootloader import Bootloader
import sys
from Fuelsensor_interface import Fuelsensor_interface
from Bootloader import Bootloader
fs = Fuelsensor_interface('192.168.100.187',5000)
b = Bootloader('192.168.100.187',5000)


#print "conectando"
#fs.connect()
#print "solicitando altura"
#fs.get_height()
#fs.backup_timeseries() # ver porque se pega la respuesta aqui, ver que hay en la interfaz serial o bien debugear el codigo, programando con el pickit 2.
#fs.get_pos()
#data_heigth= []
#data=[]
#ahora = time.strftime("%c")

#for i in range(1,50):

while True:
	time.sleep(35)
	fs.connect()
	f = open("archivo.txt", "a+")
	print "archivo abierto"
	localtime = time.asctime( time.localtime(time.time()))
	#data.append(fs.get_height)
		
	print "obteniendo altura"
	altura=fs.get_height()
	print "copiando altura en archivo de texto..."
	f.write(str(altura)+" "+localtime+ "\n")

	#print "close socket..."
	f.close()
	fs.close_socket()
	time.sleep(2)
