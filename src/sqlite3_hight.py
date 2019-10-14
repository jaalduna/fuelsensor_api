import sqlite3
import time 






#localtime = time.asctime( time.localtime(time.time()))
#cursor.execute("CREATE TABLE DatosFs(altura_raw REAL NOT NULL, fecha_hora_lectura_sensor VARCHAR(50) NOT NULL,  fecha_hora_recepcion VARCHAR(50) NOT NULL)")
def CrearTabla():
	conn = sqlite3.connect("DatosFs")
	if conn:
	    print "Connectado a la BBDD"
	    cursor = conn.cursor()
	    cursor.execute('''CREATE TABLE DatosFs(
	    	altura_raw REAL NOT NULL,
	    	fecha_hora_lectura_sensor VARCHAR(50) NOT NULL,
	    	fecha_hora_recepcion VARCHAR(50) NOT NULL)''')
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
		    localtime = time.asctime( time.localtime(time.time()))
		    
		    consulta ='''INSERT INTO DatosFs(
		    altura_raw,
		    fecha_hora_lectura_sensor,
		    fecha_hora_recepcion)
		    VALUES (?,?,?);'''
		    cursor.execute(consulta,(altura_raw,localtime,localtime))
		    print "datos insertados con exito"
	except Exception as e:
		print ("ocurrio un error al conectar a la BBDD",e)
	finally:
		conn.commit()
		cursor.close()
		conn.close()

def sql_fetch():
	conn = sqlite3.connect("DatosFs")
	cursor = conn.cursor()


	cursor.execute("SELECT * FROM DatosFs")
	rows= cursor.fetchall()
	for row in rows:
		print row
	cursor.close()

	conn.close()


altura_raw = 18.9
insertBBDD(altura_raw)

sql_fetch()

