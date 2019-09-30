import sys
from Fuelsensor_interface import Fuelsensor_interface
import time
import logging

NUM_BYTES_TO_RECEIVE = 8
logging.basicConfig(filename='periodic_report.log',level=logging.DEBUG,format='%(asctime)s  -  hight: %(message)s')
if len(sys.argv) == 3:
    fs = Fuelsensor_interface(str(sys.argv[1]), int(sys.argv[2]))
else:
    fs = Fuelsensor_interface()

while(True):
    height = fs.get_periodic_report(NUM_BYTES_TO_RECEIVE, logging)
    logging.info(height)




