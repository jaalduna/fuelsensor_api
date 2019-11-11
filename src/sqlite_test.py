from Fuelsensor_interface import Fuelsensor_interface
import MySQLdb
import time

while True:
    fs = Fuelsensor_interface('192.168.100.1',5000)
    fs.create_table()
    try:
        fs.connect()
        height = fs.get_height()
    except Exception as e:
        print e
        height = -1
    finally:
        fs.close_socket()
    fs.insert_data(height)
    time.sleep(1)