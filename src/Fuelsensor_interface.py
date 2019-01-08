import struct
import crcmod
import socket
import time
#import matplotlib.pyplot as plt
#AN1388 Microchip bootloader implementation

#constants declaration

##Command description
BK_TIMESERIES = 1
GET_NORM_ECHO = 2
GET_SDFT_ECHO = 3
RESET = 4
GET_HEIGHT = 5
GET_POS = 6

crc16 = crcmod.predefined.mkPredefinedCrcFun("xmodem")

class Fuelsensor_interface(object):
    """Fuelsensor_interface class """
    def __init__(self):
        super(Fuelsensor_interface, self).__init__()
        self.TCP_IP = '192.168.0.10'
        self.TCP_PORT = 5000
        self.BUFFER_SIZE  = 2048
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.timeout =1
        self.socket.settimeout(self.timeout)

    def __del__(self):
        self.socket.close()

    def send_cmd(self, cmd, params,rx_len):
        packet = bytearray()
        packet += struct.pack(">H", cmd)

        packet += params # append params bytearray

        #crc, not implemented yet
        packet.append(0)
        packet.append(0)

        while(True):
            if(rx_len > 0):
                data = self.receive_retry(packet, rx_len + 2, verbose=False, connect=False)
                if(len(data) >= rx_len + 2):
                    data = data[0:rx_len + 2]
                    crc = str(data[len(data) - 2:])
                    calculated_crc = struct.pack('>H', crc16(str(data[0:len(data)- 2])))
                    if crc == calculated_crc:
                        break
                else:
                    # print len(data)
                    #self.print_modbus(data)
                    pass
            else:
                self.socket.send(packet)
                return
        return data[0:len(data) - 2]

    def get_norm_echo(self,offset, length):
        """ Return normalized echo"""
        params = bytearray()
        params += struct.pack('>H', offset)
        params += struct.pack('>H', length)
        res = self.send_cmd(GET_NORM_ECHO, params, length)
        return res
    def get_sdft_echo(self,offset,length):
        """ returns sdft of echo"""
        params = bytearray()
        params += struct.pack('>H', offset)
        params += struct.pack('>H', length)
        res = self.send_cmd(GET_SDFT_ECHO, params, length)
        return res        

    def get_complete_norm_echo(self, length):
        """ get normalized echo timeseries of length 'length'"""
        truncated_len =  int(length / 50) + 1
        data = bytearray()
        for i in range (1,truncated_len):
            while(True):
                partial_data = self.get_norm_echo((i-1)*50,50)
                time.sleep(0.001)
                if len(partial_data) == 50: 
                    break;
            data +=partial_data
        print len(data)  
        return data  

    def get_complete_sdft_echo(self, length):
        """ get sdft echo timeseries of length 'length' """
        truncated_len =  int(length / 50) + 1
        data = bytearray()
        for i in range (1,truncated_len):
            while(True):
                partial_data = self.get_sdft_echo((i-1)*50,50)
                time.sleep(0.01)
                if len(partial_data) == 50: 
                    break;
            data +=partial_data
        print len(data)  
        return data  

    def get_height(self):
        """ get hight of liquid in meters."""
        data = self.send_cmd(GET_HEIGHT, bytearray(), 4)
        self.print_modbus(data)
        height = struct.unpack('<f', data)[0]
        print "height: " + str(height) + " [m]"

    def get_pos(self):
        """ get variable pos, an int value proportional to hight"""
        data = self.send_cmd(GET_POS, bytearray(), 4)
        self.print_modbus(data)
        pos = struct.unpack('<f', data)[0]
        print "pos: " + str(pos) + " [samples]"    
    def reset(self):
        """ reset fuelsensor and enter into Bootloader mode"""
        params = bytearray()
        params.append(0)
        params.append(0)
        params.append(0)
        params.append(0)

        self.send_cmd(RESET, params, 0)

    def check_crc(self, msg):
        calculated_crc = bytearray()
        calculated_crc += struct.pack("<H", crc16(str(msg[0:len(msg)- 2])))
        #self.print_modbus(str(calculated_crc))
        if(calculated_crc == msg[len(msg) -2 : len(msg)]):
            return True
        else:
            return False

        # print "packet content: ",
        # print(":".join("{:02x}".format(ord(c)) for c in str(packet)))


    def connect(self):
        """ Try to stablish a tcp/ip connection with fuelSensor device"""
        while True:
            try:
                print "connecting...",
                self.socket.settimeout(self.timeout)
                self.socket.connect((self.TCP_IP, self.TCP_PORT))
                #self.socket.settimeout(None)
                print "success!"
                return
            except:
                print "can't connect"
                self.close_socket()
                #return

    def receive_retry(self,packet,length,verbose = False,connect = True):
        start_time = 0
        stop_time = 0
        if(connect):
            self.connect() 
        while True:
            try:
                if(verbose):
                    print "sending: ",
                    self.print_modbus(str(packet))
                start_time = (time.time()*1000)
                #self.print_modbus(str(packet))

                self.socket.send(packet)
                counter = 5 
                data = ""
                while(counter >0):
                    counter -= 1
                    data += self.socket.recv(self.BUFFER_SIZE)
                    
                    # if(verbose):
                    #     print data
                        #self.print_modbus(data)
                     
                    if(len(data) >= length):
                        stop_time = (time.time()*1000)
                        if(connect):
                            self.close_socket()
                        if(verbose):
                            print "time elapsed: ",
                            print str(stop_time - start_time)
                            print "data received ok: ",
                            self.print_modbus(data)


                        return data
                
            except:
                self.print_modbus(data)
                print "no answer...",
                
                if(True):
                    self.close_socket()
                    self.connect()

    def close_socket(self):
        """ Try to close tcp/ip SOCKET with FuelSensor device"""
        #lets close socket
        self.socket.close()
        time.sleep(0.1)
        #lets reasign socket so it can be opened again
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(self.timeout)
        time.sleep(0.1)

    def print_modbus(self,res):
        print(":".join("{:02x}".format(ord(c)) for c in res))
    def backup_timeseries(self):
        params = bytearray()
        self.send_cmd(BK_TIMESERIES,params,8)


# fs_interface = Fuelsensor_interface()
# fs_interface.connect()
# fs_interface.reset()
# fs_interface.close_socket()
# for i in range(1,10):
#     fs_interface.connect()
#     params = bytearray()
#     #fs_interface.reset()
#     fs_interface.get_height()
#     # fs_interface.reset()
#     # fs_interface.reset()
#     fs_interface.close_socket()
#     time.sleep(0.5)
#fs_interface.send_cmd(BK_TIMESERIES, params, 8)
# time.sleep(0.5)

# num_of_samples = 16000;
# data_bytes_norm = fs_interface.get_complete_norm_echo(num_of_samples)
# #data_bytes_sdft = fs_interface.get_complete_sdft_echo(num_of_samples)
# #fs_interface.send_cmd(RESET, params, 0)
# fs_interface.get_height()
# fs_interface.get_pos()
# fs_interface.close_socket()


# # data_bytes_sdft = fs_interface.get_complete_sdft_echo(num_of_samples)
# # fs_interface.close_socket()

# data_norm = []
# for i in range(0,num_of_samples/4):
#     new_data = struct.unpack('<f', data_bytes_norm[i*4:(i+1)*4])

#     # if (new_data[0] > 1 or new_data[0] < -1):
#     #     print "new_data:" + str(new_data)
#     #     pass
#     #     new_data = (0.5,1)
#     data_norm.append(new_data[0])
# print len(data_norm)

# plt.plot(data_norm)
# plt.grid(True)
# plt.title('Echo vs time')
# plt.ylabel('norm echo')
# plt.show()

# data_sdft = []
# for i in range(0,num_of_samples/4):
#     new_data = struct.unpack('<f', data_bytes_sdft[i*4:(i+1)*4])
#     data_sdft.append(new_data[0])
# print len(data_sdft)


# plt.plot(data_sdft)
# plt.ylabel('norm echo')
# plt.show()



