from Fuelsensor_interface import Fuelsensor_interface
import time

fs = Fuelsensor_interface('192.168.148.1',5000)
while True:
    fs.connect()
    h = fs.get_height()
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    fs.close_socket()
    if(h>0):
        percent = h/0.0225
        fs.sql_server_insert(t,h,percent)
        fs.sql_server_update_estanques(1,t,percent)
        break