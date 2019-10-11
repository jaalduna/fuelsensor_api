import sqlite3
import time 


conn = sqlite3.connect("DatosFs")
cursor = conn.cursor()


cursor.execute("SELECT * FROM DatosFs")
cursor.close()

conn.close()