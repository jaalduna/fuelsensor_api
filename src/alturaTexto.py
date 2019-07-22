import time 

#from Bootloader import Bootloader
import sys
from Fuelsensor_interface import Fuelsensor_interface
from Fuelsensor_interface import Params
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
params = Params(fs)
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
		print "espera 5s..."
		fs.reset()
		#cont=cont+1
		print "reset..."
		time.sleep(1)
		params.sdft_i_min.interface.connect()
		params.sdft_i_min.get_value()
		print params.sdft_i_min.value

		params.sdft_i_min.set_value(200)
		print params.sdft_i_min.value

		params.sdft_n.get_value()
		params.sdft_k.get_value()
		#params.sdft_k.set_value(49)
		params.sdft_peak.get_value()
		#params.pga_gain.set_value(4)
		#params.num_pulses.set_value(5)
		params.num_pulses.get_value()
		print "N:", params.sdft_n.value
		print "k:", params.sdft_k.value
		print "sdft paek: ", params.sdft_peak.value
		print "pga gain: ", params.pga_gain.value
		print "num_pulses", params.num_pulses.value
		params.sdft_i_min.interface.close_socket()
		#fs.backup_params_to_flash()

		f.write(str(cont)+" -------------- "+localtime+" "+str(reset)+"\n")

		#f.write("----------------------------\n")
		


		
	

		#b.jump_to_app()
		#b.close_socket()



	#print "close socket..."
	f.close()
	fs.close_socket()
	time.sleep(2)
	
