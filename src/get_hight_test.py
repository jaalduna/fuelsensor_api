# from Fuelsensor_interface import Fuelsensor_interface
# fs = Fuelsensor_interface()
# fs.connect()
# fs.reset()
# fs.close_socket()

# from Bootloader import Bootloader
# b = Bootloader()
# b.read_version()
# b.connect()
# b.program_file('aiko1_enero.hex')
# b.close_socket()
# b.connect()
# b.jump_to_app()
# b.close_socket()

from Fuelsensor_interface import Fuelsensor_interface
fs = Fuelsensor_interface()
fs.connect()
fs.get_height()
#fs.backup_timeseries() # ver porque se pega la respuesta aqui, ver que hay en la interfaz serial o bien debugear el codigo, programando con el pickit 2.
fs.get_pos()
fs.close_socket()
