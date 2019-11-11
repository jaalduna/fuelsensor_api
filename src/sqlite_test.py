from Fuelsensor_interface import Fuelsensor_interface

fs = Fuelsensor_interface()
fs.create_table()
fs.insert_data(12.0)
fs.insert_data(13.2)
fs.insert_data(8.4)

fs.fetch_table()
