from Fuelsensor_interface import Fuelsensor_interface
import sqlite3
fs = Fuelsensor_interface()
#print sqlite3.datetime()
fs.create_table()
fs.insert_data(12)
fs.insert_data(13)
fs.insert_data(8)

fs.sql_fetch()