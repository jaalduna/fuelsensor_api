import sys
from Fuelsensor_interface import Fuelsensor_interface
import time
import matplotlib.pyplot as plt
import numpy as np

if len(sys.argv) == 3:
    fs = Fuelsensor_interface(str(sys.argv[1]), int(sys.argv[2]))
else:
    fs = Fuelsensor_interface()

class grafic_echo_fs(Fuelsensor_interface):
		"""docstring for ClassName"""
		def __init__(self):
			super(Fuelsensor_interface, self).__init__()
			self.arg = arg
				
def grafic_echo(Fuelsensor_interface):
	super
	x=np.linspace(0,100,100)


fs.grafic_echo()




