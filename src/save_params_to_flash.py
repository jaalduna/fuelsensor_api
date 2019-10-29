import sys
from Fuelsensor_interface import Fuelsensor_interface
from Fuelsensor_interface import Params

if len(sys.argv) == 2:
    ip = str(sys.argv[1])
else:
    ip = '192.168.100.187'

fs = Fuelsensor_interface(ip, 5000)
fs.connect()

try:
    print "saving params to flash"
    fs.backup_params_to_flash()

except KeyboardInterrupt:
	print "Keyboard Interrupt"

except Exception as e:
    print e

finally:
    print "closing socket...",
    fs.close_socket()
    print "done!"