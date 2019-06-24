import sys
from Fuelsensor_interface import Fuelsensor_interface
import time
if len(sys.argv) == 4:
    fs = Fuelsensor_interface(str(sys.argv[1]), int(sys.argv[2]))
else:
    fs = Fuelsensor_interface()
print "conectando"
fs.connect()
print "backup_timeseries"
fs.bk_timeseries()
time.sleep(1)
print "get norm echo"
offset = 0
length = int(sys.argv[3])
#data = fs.get_norm_echo(offset, length)
data = fs.get_complete_norm_echo(length)
fs.print_modbus(str(data))
#fs.backup_timeseries() # ver porque se pega la respuesta aqui, ver que hay en la interfaz serial o bien debugear el codigo, programando con el pickit 2.
#fs.get_pos()
fs.close_socket()
