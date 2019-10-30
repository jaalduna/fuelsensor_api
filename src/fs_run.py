from Fuelsensor_interface import Fuelsensor_interface
import time
fs = Fuelsensor_interface('192.168.100.1',5000)
fs.create_table()
while True:
    try:
        time.sleep(5)
        fs.connect()
        height = fs.get_height()
        fs.insert_data(height)
    except Exception as e:
        print e
    finally:
        fs.close_socket()