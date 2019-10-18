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

reset=0
cont=0
while True:
	cont=cont+1
	try:
		
		time.sleep(2)
		#cont=cont+1
		fs.connect()
		f = open("archivo.txt", "a+")
		print "archivo abierto"
		localtime = time.asctime( time.localtime(time.time()))
	#data.append(fs.get_height)
		
		print "obteniendo altura"
		altura=fs.get_height()

		print "copiando altura en archivo de texto..."
		
		f.write(str(cont)+" "+str(altura)+" "+localtime+" "+str(reset)+"\n")

	except:
		print "except"
		reset=reset+1
		#cont=cont+1

		localtime = time.asctime( time.localtime(time.time()))
		time.sleep(5)
		fs.reset()
		#cont=cont+1
		print "espera 5s ...."
		time.sleep(1)

		f.write(str(cont)+" -------------- "+localtime+" "+str(reset)+"\n")

		#f.write("----------------------------\n")
		


		
	

		#b.jump_to_app()
		#b.close_socket()



	#print "close socket..."
	f.close()
	fs.close_socket()
	time.sleep(2)
	
