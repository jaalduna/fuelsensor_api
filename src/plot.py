import sys
import pyodbc  
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt 
from Fuelsensor_interface import Fuelsensor_interface

def sql_server_plot(table='estanque_lecturas', db='aiko_desarrollo', days = 1):
    conn = pyodbc.connect('Driver={0};Server=WIN-KA4LQK6DGPJ\SQLEXPRESS;Database={1};Trusted_Connection=yes;'.format('SQL Server',db))
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT TOP 1 fecha_hora_lectura_sensor FROM {0} ORDER BY id DESC'.format(table))
        element = cursor.fetchone()[0]
        lenght = timedelta(days=days)
        cursor.execute('select fecha_hora_lectura_sensor, altura_raw from {0} where fecha_hora_lectura_sensor > \'{1}\''.format(table,'1900-01-01 00:00:00'))#element - lenght))
        rows = cursor.fetchall()
        x = []
        y = []
        for row in rows:
            x.append(row.fecha_hora_lectura_sensor)
            y.append(row.altura_raw)
        plt.plot(x,y)
        plt.grid(True)
        plt.title('Altura de combustible')
        plt.ylabel('Altura [m]')
        plt.xlabel('Fecha Hora lectura')
        plt.show()
        cursor.close()
        conn.close()

if len(sys.argv) > 1: 
    days = int(sys.argv[1])
else:
    days = 1

sql_server_plot(days=days)
