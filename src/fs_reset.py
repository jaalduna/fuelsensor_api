import sys
from Fuelsensor_interface import Fuelsensor_interface
<<<<<<< HEAD
fs = Fuelsensor_interface('172.19.6.187',5000)
=======


if len(sys.argv) == 3:
    fs = Fuelsensor_interface(str(sys.argv[1]), int(sys.argv[2]))
else:
    fs = Fuelsensor_interface()
>>>>>>> 06f9cbbc17af44e520c304c4856eeb3107e4fb0e
fs.connect()
fs.reset()
#fs.backup_timeseries() # ver porque se pega la respuesta aqui, ver que hay en la interfaz serial o bien debugear el codigo, programando con el pickit 2.
#fs.get_pos()
fs.close_socket()
