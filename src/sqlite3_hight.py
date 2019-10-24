import sqlite3
import time 
import sys
from Fuelsensor_interface import Fuelsensor_interface
import datetime 



today = datetime.datetime.today()
fechaHoraActual= today.today()
print type(fechaHoraActual)



#localtime = time.asctime( time.localtime(time.time()))
#cursor.execute("CREATE TABLE DatosFs(altura_raw REAL NOT NULL, fecha_hora_lectura_sensor VARCHAR(50) NOT NULL,  fecha_hora_recepcion VARCHAR(50) NOT NULL)")
def CrearTabla():
	conn = sqlite3.connect("DatosFs")
	if conn:
	    print "Connectado a la BBDD"
	    cursor = conn.cursor()
	    cursor.execute('''CREATE TABLE DatosFs(
	    	altura_raw REAL NOT NULL,
	    	fecha_hora_lectura_sensor DATETIME NOT NULL,
	    	fecha_hora_recepcion DATETIME NOT NULL)''')
	    print "tabla creada "

	    
	    
def insertBBDD(altura_raw):
	try:
		conn = sqlite3.connect("DatosFs")
		if conn:
		    print "Connectado a la BBDD"
		    
		    cursor = conn.cursor()
		    
			
		            #angulo_roll = 20.6
		            #hora = (CURRENT_TIMESTAMP) 
		    print "insertando datos a la base de datos de lipigas"
		   #localtime = time.asctime( time.localtime(time.time()))
		    today = datetime.datetime.today()
		    fechaHoraActual= today.today()
		    consulta ='''INSERT INTO DatosFs(
		    altura_raw,
		    fecha_hora_lectura_sensor,
		    fecha_hora_recepcion)
		    VALUES (?,?,?);'''
		    cursor.execute(consulta,(altura_raw,fechaHoraActual,fechaHoraActual))
		    print "datos insertados con exito"
	except Exception as e:
		print ("ocurrio un error al conectar a la BBDD",e)
	finally:
		conn.commit()
		cursor.close()
		conn.close()

def sql_fetch():
	try:
		conn = sqlite3.connect("DatosFs")
		cursor = conn.cursor()


		cursor.execute("SELECT * FROM DatosFs")
		rows= cursor.fetchall()
		for row in rows:
			print row
		cursor.close()

		conn.close()
	except:
		print "Can't connet to BBDD"
		cursor.close()
		conn.close()


altura_raw = 18.9
fs = Fuelsensor_interface('192.168.100.187',5000)
fs.connect()
fs.get_app_version()
altura_raw = fs.get_height()
fs.get_pos()
fs.close_socket()

altura_raw = 18.9
# # #type(altura_raw)
insertBBDD(altura_raw)

sql_fetch()

