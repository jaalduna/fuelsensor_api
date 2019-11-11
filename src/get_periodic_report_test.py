import sys
from Fuelsensor_interface import Fuelsensor_interface
import time
import logging

NUM_BYTES_TO_RECEIVE = 8
logging.basicConfig(filename='periodic_report.log',level=logging.DEBUG,format='%(asctime)s  -  hight: %(message)s')
if len(sys.argv) == 2:
    fs = Fuelsensor_interface(str(sys.argv[1]), 5000)
else:
    fs = Fuelsensor_interface('192.168.100.187',5000)

while(True):
    height = fs.get_periodic_report(NUM_BYTES_TO_RECEIVE, logging)
    logging.info(height)




