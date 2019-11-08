from Fuelsensor_interface import Fuelsensor_interface
import MySQLdb
import time

while True:
    try:
        fs = Fuelsensor_interface('192.168.148.1',5000)

        fs.create_table()

        fs.connect()
        height = fs.get_height()
        fs.insert_data(height)

    except Exception as e:
        print e
    finally:
        fs.close_socket()
        time.sleep(60)
