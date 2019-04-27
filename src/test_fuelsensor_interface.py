import unittest
from mock import patch
from fuelsensor_interface import Fuelsensor_interface
import struct
from fuelsensor_interface import Params
import crcmod



crc16 = crcmod.predefined.mkPredefinedCrcFun("xmodem")

class TestFuelsensor_interface(unittest.TestCase):

    def setUp(self):
        #print 'setUp'
        self.int_1 = Fuelsensor_interface()
        self.params = Params(self.int_1)
    def tearDown(self):
        #print 'tearDown\n'
        pass

    def test_send_cmd(self):
        with patch('fuelsensor_interface.Fuelsensor_interface.receive_retry') as mocked_receive_retry, \
             patch('fuelsensor_interface.socket.socket.send') as mocked_send:
            rtrn = bytearray()
            data = struct.pack('>B',10)
            crc = struct.pack('>H', crc16(str(data)))
            rtrn.append(data)
            rtrn +=crc

            mocked_receive_retry.return_value = rtrn

            params_field = bytearray()
            params_field = struct.pack('>HH', 0,self.params.PARAM_PGA_GAIN)

            result =  self.int_1.send_cmd(self.int_1.GET_PARAM,params_field, self.params.pga_gain.num_bytes)
            #mocked_receive_retry.assert_called_with()
            self.assertEqual(result, data)

    def test_get_param(self):
        with patch('fuelsensor_interface.Fuelsensor_interface.send_cmd') as mocked_send_cmd, \
             patch('fuelsensor_interface.socket.socket.send') as mocked_send:

             data = struct.pack('>B', 10)
             mocked_send_cmd.return_value = data

             result = self.int_1.get_param(self.params.pga_gain.param_id, self.params.pga_gain.num_bytes)
             self.assertEqual(result, data)
             #mocked_send_cmd.assert_called_with('')

             #send_cmd(GET_PARAM, param_field, num_bytes_response) 

    def test_get_param_byte(self):
        with patch('fuelsensor_interface.Fuelsensor_interface.get_param') as mocked_get_param, \
             patch('fuelsensor_interface.socket.socket.send') as mocked_send:     

             data = struct.pack('>B', 10)
             mocked_get_param.return_value =  data

             result = self.int_1.get_param_byte(self.params.pga_gain.param_id)
             mocked_get_param.assert_called_with(self.params.pga_gain.param_id,1)
             self.assertEqual(result, data)
    def test_get_param_unsigned_short(self):
        with patch('fuelsensor_interface.Fuelsensor_interface.get_param') as mocked_get_param:   

             source_data = 1000;
             data = struct.pack('>H', source_data)
             mocked_get_param.return_value =  data

             result = self.int_1.get_param_unsigned_short(self.params.sdft_sound_speed.param_id)
             mocked_get_param.assert_called_with(self.params.sdft_sound_speed.param_id,2)
             self.assertEqual(result, source_data)

    def test_get_param_float_32(self):
        with patch('fuelsensor_interface.Fuelsensor_interface.get_param') as mocked_get_param:   

             source_data = 3.14161;
             data = struct.pack('<f', source_data)
             mocked_get_param.return_value =  data

             result = self.int_1.get_param_float_32(self.params.sdft_min_peak_value_th.param_id)
             mocked_get_param.assert_called_with(self.params.sdft_min_peak_value_th.param_id,4)
             self.assertAlmostEqual(result, source_data,places=5)

    def test_set_param(self):
        with patch('fuelsensor_interface.Fuelsensor_interface.send_cmd') as mocked_send_cmd:
             #print('test set_param')
             data = struct.pack('>B', 1)
             mocked_send_cmd.return_value = data
             value = struct.pack('>B',10)
             result = self.int_1.set_param(self.params.pga_gain.param_id, self.params.pga_gain.num_bytes, value)
             self.assertEqual(result, data)

    def test_set_param_byte(self):
        with patch('fuelsensor_interface.Fuelsensor_interface.set_param') as mocked_set_param:    
             data = 10
             mocked_set_param.return_value =  struct.pack('>B', 1)

             result = self.int_1.set_param_byte(self.params.pga_gain.param_id,data)
             mocked_set_param.assert_called_with(self.params.pga_gain.param_id,1,data)
             self.assertEqual(result, struct.pack('>B', 1))  

    def test_set_param_unsigned_short(self):    
        with patch('fuelsensor_interface.Fuelsensor_interface.set_param') as mocked_set_param:    
             data = 1000
             mocked_set_param.return_value =  struct.pack('>B', 1)

             result = self.int_1.set_param_unsigned_short(self.params.sdft_sound_speed.param_id,data)
             mocked_set_param.assert_called_with(self.params.sdft_sound_speed.param_id,1,data)
             self.assertEqual(result, struct.pack('>B', 1))  
    def test_set_param_float_32(self):    
        with patch('fuelsensor_interface.Fuelsensor_interface.set_param') as mocked_set_param:    
             data = 3.1416
             mocked_set_param.return_value =  struct.pack('>B', 1)

             result = self.int_1.set_param_float_32(self.params.sdft_sound_speed.param_id,data)
             mocked_set_param.assert_called_with(self.params.sdft_sound_speed.param_id,1,data)
             self.assertEqual(result, struct.pack('>B', 1))  

if __name__ == '__main__':
    unittest.main()