from Fuelsensor_interface import Fuelsensor_interface
import time
import pyodbc

fs = Fuelsensor_interface('1.1.1.1',5000)
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WIN-KA4LQK6DGPJ\SQLEXPRESS;'
                      'Trusted_Connection=yes;')
if conn:
    cursor = conn.cursor()

    cursor.execute("select id, volumen_normalizado, volumen_raw from [aiko_desarrollo].[dbo].[estanque_lecturas] where id between 10765 and 10896")
    result = cursor.fetchall()
    for rows in result:
        vol = rows[1]/55.06
        query = "update [aiko_desarrollo].[dbo].[estanque_lecturas] set volumen_normalizado = {0}, volumen_raw = {0} where id = {1}".format(vol,rows[0])
        cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    print 'Done.'