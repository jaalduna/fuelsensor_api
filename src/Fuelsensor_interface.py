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
GET_PARAM = 7
SET_PARAM = 8
RESTORE_DEFAULT_PARAMS_TO_FLASH = 9
BACKUP_PARAMS_TO_FLASH = 10


#TODO: create a list of PARAMS constants using fields "PARAM_ID" and "nombre" from
# the table "lista de parametros" located at
#https://fuelsensor.readthedocs.io/en/latest/low_level_interface.html
PARAM_DATA_VECTOR_TYPE = 0x00
PARAM_DATA_VECTOR_OFFSET = 0x02
PARAM_PGA_GAIN = 0x04
PARAM_NUM_PULSES = 0x05
PARAM_PULSE_PERIOD = 0x06
PARAM_PULSE_WIDTH = 0x07
PARAM_RES_HV = 0x08
PARAM_SDFT_MIN_PEAK_VALUE_TH = 0x09
PARAM_SDFT_K = 0x0D
PARAM_SDFT_N = 0x0F
PARAM_SDFT_I_MIN = 0x11
PARAM_SDFT_MIN_ECO_LIMIT = 0x13
PARAM_SDFT_MAX_ECO_LIMIT = 0x14
PARAM_SDFT_VAR_NORM = 0x15
PARAM_SDFT_PEAK = 0x19
PARAM_SDFT_SOUND_SPEED = 0x1D
PARAM_SDFT_SAMPLE_RATE = 0x1F
PARAM_SDFT_N_SAMPLES_ONE_VALID = 0x21
PARAM_SKIP_PARAM = 0x23


crc16 = crcmod.predefined.mkPredefinedCrcFun("xmodem")

class Param(object):
    def __init__(self,interface, param_id, num_bytes):
        super(Param, self).__init__()
        self.param_id = param_id 
        self.num_bytes = num_bytes
        self.value = 0
        self.interface = interface
    def get_value(self):
        if(self.num_bytes == 1):
            self.value = self.interface.get_param_byte(self.param_id)
        elif self.num_bytes == 2:
            self.value = self.interface.get_param_unsigned_short(self.param_id)
        elif self.num_bytes ==4:
            self.value = self.interface.get_param_float_32(self.param_id)
            
    def set_value(self,value):
        if(self.num_bytes ==1):
            self.interface.set_param_byte(self.param_id, 8, value)
            self.value = self.interface.get_param_byte(self.param_id)
        elif (self.num_bytes == 2):
            self.interface.set_param_unsigned_short(self.param_id, 8, value)
            self.value = self.interface.get_param_unsigned_short(self.param_id)
        elif (self.num_bytes == 4):
            self.interface.set_param_float_32(self.param_id, 8, value)
            self.value = self.interface.get_param_float_32(self.param_id)



class Params(object):
    PARAM_DATA_VECTOR_TYPE = 0x00
    PARAM_DATA_VECTOR_OFFSET = 0x04
    PARAM_PGA_GAIN = 0x08
    PARAM_NUM_PULSES = 0x09
    PARAM_PULSE_PERIOD = 0x0a
    PARAM_PULSE_WIDTH = 0x0b
    PARAM_RES_HV = 0x0c
    PARAM_SDFT_MIN_PEAK_VALUE_TH = 0x0d
    PARAM_SDFT_K = 0x11
    PARAM_SDFT_N = 0x13
    PARAM_SDFT_I_MIN = 0x15
    PARAM_SDFT_MIN_ECO_LIMIT = 0x17
    PARAM_SDFT_MAX_ECO_LIMIT = 0x18
    PARAM_SDFT_VAR_NORM = 0x19
    PARAM_SDFT_PEAK = 0x1d
    PARAM_SDFT_SOUND_SPEED = 0x21
    PARAM_SDFT_SAMPLE_RATE = 0x23
    PARAM_SDFT_N_SAMPLES_ONE_VALID = 0x25
    PARAM_SKIP_PARAM = 0x27

    def __init__(self, interface):
        super(Params, self).__init__()
        self.data_vector_type = Param(interface,PARAM_DATA_VECTOR_TYPE,2)
        self.data_vector_offset = Param(interface,PARAM_DATA_VECTOR_OFFSET,2)
        self.pga_gain = Param(interface, PARAM_PGA_GAIN,1)
        self.num_pulses = Param(interface, PARAM_NUM_PULSES,1)
        self.pulse_period = Param(interface, PARAM_PULSE_PERIOD,1)
        self.pulse_width = Param(interface, PARAM_PULSE_WIDTH,1)
        self.res_hv = Param(interface, PARAM_RES_HV,1)
        self.sdft_min_peak_value_th = Param(interface, PARAM_SDFT_MIN_PEAK_VALUE_TH,4)
        self.sdft_k = Param(interface, PARAM_SDFT_K,2)
        self.sdft_n = Param(interface, PARAM_SDFT_N,2)
        self.sdft_i_min = Param(interface,PARAM_SDFT_I_MIN,2)
        self.sdft_min_eco_limit = Param(interface, PARAM_SDFT_MIN_ECO_LIMIT,1)
        self.sdft_max_eco_limit = Param(interface, PARAM_SDFT_MAX_ECO_LIMIT,1)
        self.sdft_var_norm = Param(interface, PARAM_SDFT_VAR_NORM,4)
        self.sdft_peak = Param(interface, PARAM_SDFT_PEAK,4)
        self.sdft_sound_speed = Param(interface, PARAM_SDFT_SOUND_SPEED,2)
        self.sdft_sample_rate = Param(interface, PARAM_SDFT_SAMPLE_RATE,2)
        self.sdft_n_samples_one_valid = Param(interface, PARAM_SDFT_N_SAMPLES_ONE_VALID,2)
        self.skip_param = Param(interface, PARAM_SKIP_PARAM,2)

class Node(object):
    def __init__(self):
        super(Node,self).__init__()
        self.fs_interface = Fuelsensor_interface()
        self.params = Params(self.fs_interface)


class Fuelsensor_interface(object):
    """Fuelsensor_interface class """

    #command constants
    BK_TIMESERIES = 1
    GET_NORM_ECHO = 2
    GET_SDFT_ECHO = 3
    RESET = 4
    GET_HEIGHT = 5
    GET_POS = 6
    GET_PARAM = 7
    SET_PARAM = 8
    RESTORE_DEFAULT_PARAMS_TO_FLASH = 9
    BACKUP_PARAMS_TO_FLASH = 10

    def __init__(self):
        super(Fuelsensor_interface, self).__init__()
        self.TCP_IP = '192.168.0.10'
        self.TCP_PORT = 5000
        self.BUFFER_SIZE  = 2048
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.timeout =0.1
        self.socket.settimeout(self.timeout)


    def __del__(self):
        self.socket.close()

    def send_cmd(self, cmd, params,rx_len):
        packet = bytearray()
        packet += struct.pack(">H", cmd) # 2 bytes

        #fill with zeros so 4 bytes filled on the params field. 
        #for i in range(4 - len(params)):
        #        packet.append(0)

        #fill with params values #4 bytes
        for i in range(len(params)):
            packet.append(params[i])

        #crc, not implemented yet
        packet.append(0)
        packet.append(0)
        #packet = bytearray()
        #for i in range(12):
        #    packet.append(i)

        while(True):
            if(rx_len > 0):
                data = self.receive_retry(packet, rx_len + 2, verbose=False, connect=False)
                if(len(data) >= rx_len + 2):
                    data = data[0:rx_len + 2] #chunk garbage bytes
                    crc = str(data[len(data) - 2:])
                    calculated_crc = struct.pack('>H', crc16(str(data[4:len(data)- 2])))
                    if crc == calculated_crc:
                        break
                    else:
                        raise Exception("bad crc")
                else:
                    # print len(data)
                    #self.print_modbus(data)
                    raise Exception("not enougth rx bytes")
                    break
            else:
                self.socket.send(packet)
                return
        return data

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
        data = self.send_cmd_without_params(GET_HEIGHT, 8)

        height = struct.unpack('<f', data[4:8])[0]
        print "height: " + str(height) + " [m]"

    def get_pos(self):
        """ get variable pos, an int value proportional to hight"""
        data = self.send_cmd_without_params(GET_POS, 4)
        self.print_modbus(data)
        pos = struct.unpack('<f', data)[0]
        print "pos: " + str(pos) + " [samples]"    
    def reset(self):
        """ reset fuelsensor and enter into Bootloader mode"""
        self.send_cmd_without_params(RESET, 0)

    def send_cmd_without_params(self, name, num_bytes):
        """ send command name, filling params with 4 zeros"""
        params_field = bytearray()
        params_field = struct.pack('>BBBBBBBB',0,0,0,0,0,0,0,0) 
        return self.send_cmd(name, params_field,num_bytes)
        

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
                    #self.print_modbus(str(packet))
                start_time = (time.time()*1000)
                #self.print_modbus(str(packet))

                #self.socket.send(packet)
                packet_size = 4 
                for i in range(len(packet)/packet_size):
                    self.socket.send(packet[i*packet_size:i*packet_size+packet_size])
                    time.sleep(0.05)
                #self.socket.send(bytearray(range(1)))
                
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

    def get_param(self, param_id, num_bytes_response):
        #TODO: Implement get_param function. get_param should query, print and return the parameter given by param_id. 
        # using the command self.send_cmd. Return value should be converted from bytearray to type described at
        #table "Lista de parametros " located at https://fuelsensor.readthedocs.io/en/latest/low_level_interface.html. Use , using struct.unpack() function for that.
        #second argument from send_cmd should be 4 bytes. Add them at the end. 

        #lets transform param_id into a 4 bytes bytearra() with the last byte
        param_field = struct.pack('>BBBBBBBB', 0,0,0,param_id,0,0,0,0)
        param_value_bytearray = self.send_cmd(GET_PARAM, param_field, num_bytes_response) 
        #check number of bytes returned, it seems that answer is always 4 bytes ??


        #complete for other param_id values, struct.unpack format should be
        # ''
        return param_value_bytearray

    def get_param_byte(self,param_id):
        param_value_bytearray = self.get_param(param_id,1)
        return param_value_bytearray

    def get_param_unsigned_short(self,param_id):
        param_value_bytearray = self.get_param(param_id,2)
        return struct.unpack('>H',param_value_bytearray)[0]

    def get_param_float_32(self, param_id):
        param_value_bytearray = self.get_param(param_id,4)
        return struct.unpack('<f', param_value_bytearray)[0]

    def set_param(self, param_id, num_bytes_response, value):
        param_field = struct.pack('>BBBB',0,0,0,param_id)
        param_field += value
        #update param on the remote node
        response = self.send_cmd(SET_PARAM, param_field, num_bytes_response)
        #update param on the local representation of the node
        self.print_modbus(response)
        return response

    def set_param_byte(self, param_id,value):
        value_field =  struct.pack('>BBBB',0,0,0,value)
        response =  self.set_param(param_id, 1, value)
        return response

    def set_param_unsigned_short(self, param_id,value):
        value_field =  struct.pack('>HH',0,value)
        response = self.set_param(param_id, 1, value)    
        return response
    def set_param_float_32(self, param_id,value):
        value_field =  struct.pack('<f',value)
        response = self.set_param(param_id, 1, value)  
        return response





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



