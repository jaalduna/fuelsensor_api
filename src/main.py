import sys
import json
from Bootloader import Bootloader

print sys.argv[1]

y = json.loads(sys.argv[1])
ip = y["ip"]
port = y["port"]


print "ip: " + y["ip"]
print "port: " + str(y["port"])
# #print "arg 2: " + sys.argv[2]
b = Bootloader(ip,port)
b.read_version()
# b.connect()
# b.jump_to_app()
# #print "Jump to app"

# b.close_socket()

