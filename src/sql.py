from Fuelsensor_interface import Fuelsensor_interface
import MySQLdb
import time

fs = Fuelsensor_interface('172.16.0.2',5000)
fs.create_table(table='test', drop_table=True)
for i in range(1,10):
    fs.insert_row(5)
    fs.fetch_table()
    fs.delete_row(i)

#while True:
#    try:
#        fs.connect(verbose=False)
#        height = fs.get_height(verbose=False)
#        fs.insert_data(height)
#    except Exception as e:
#        print e
#    finally:
#        fs.close_socket()
#        time.sleep(60)