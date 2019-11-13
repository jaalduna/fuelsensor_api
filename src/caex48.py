import MySQLdb
import time
from Fuelsensor_interface import Fuelsensor_interface

fs = Fuelsensor_interface('192.168.148.1',5000)
#fs.create_table()

while True:
    try:
        fs.connect(verbose=False)
        height = fs.get_height(verbose=False)
        fs.insert_data(height)
        time.sleep(60)
    except Exception as e:
        print e
    finally:
        fs.close_socket()
