import sys
from Fuelsensor_interface import Fuelsensor_interface
import time
if len(sys.argv) == 3:
    fs = Fuelsensor_interface(str(sys.argv[1]), int(sys.argv[2]))
else:
    fs = Fuelsensor_interface('192.168.100.187',5000)
#print "conectando"
fs.connect()
#print "solicitando altura"
fs.get_height()
#fs.get_temp()
#fs.get_id()
fs.get_app_version()
#fs.get_timestamp()
#fs.set_timestamp(00,42,19,0,28,7,19)
#time.sleep(1)
#fs.get_timestamp()
#for i in range(1,100):
#    fs.get_imu_accel_var()
#    time.sleep(0.5)
#fs.backup_timeseries() # ver porque se pega la respuesta aqui, ver que hay en la interfaz serial o bien debugear el codigo, programando con el pickit 2.
fs.get_pos()
fs.close_socket()


