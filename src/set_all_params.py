import sys
from Fuelsensor_interface import Fuelsensor_interface
from Fuelsensor_interface import Params

if len(sys.argv) == 3:
    fs = Fuelsensor_interface(str(sys.argv[1]), int(sys.argv[2]))
else:
    fs = Fuelsensor_interface('192.168.100.187', 5000)

params = Params(fs)
params.sdft_i_min.interface.connect()

try:
	#params.data_vector_type.set_value(0)
	#params.data_vector_offset.set_value(0)
	params.pga_gain.set_value(4)
	params.num_pulses.set_value(10)
	#params.pulse_period.set_value(87)
	#params.pulse_width.set_value(30)
	#params.res_hv.set_value(40)

	#params.sdft_min_peak_value_th.set_value(0.2)
	#params.sdft_k.set_value(39)
	#params.sdft_n.set_value(107)
	#params.sdft_i_min.set_value(450)
	#params.sdft_min_eco_limit.set_value(30)
	#params.sdft_max_eco_limit.set_value(80)
	#params.sdft_var_norm.set_value(50000)
	#params.sdft_peak.set_value(10)
	#params.sdft_sound_speed.set_value(1495)
	#params.sdft_sample_rate.set_value(2981)
	#params.sdft_n_samples_one_valid.set_value(20)
	#params.skip_param.set_value(20000)
except KeyboardInterrupt:
	print "Keyboard Interrupt"

except Exception as e:
	print e

finally:
	print "closing socket"
	params.sdft_i_min.interface.close_socket()


print "data_vector_type: ", params.data_vector_type.value
print "data_vector_offset: ", params.data_vector_offset.value
print "pga_gain: ", params.pga_gain.value
print "num_pulses: ", params.num_pulses.value
print "pulse_period: ", params.pulse_period.value
print "pulse_width: ", params.pulse_width.value
print "res_hv: ", params.res_hv.value

print "\nsdft_min_peak_value_th: ", params.sdft_min_peak_value_th.value
print "sdft_k: ", params.sdft_k.value
print "sdft_n: ", params.sdft_n.value
print "sdft_i_min: ", params.sdft_i_min.value
print "sdft_min_eco_limit: ", params.sdft_min_eco_limit.value
print "sdft_max_eco_limit: ", params.sdft_max_eco_limit.value
print "sdft_var_norm: ", params.sdft_var_norm.value
print "sdft_peak: ", params.sdft_peak.value
print "sdft_sound_speed: ", params.sdft_sound_speed.value
print "sdft_sample_rate: ", params.sdft_sample_rate.value
print "sdft_n_samples_one_valid: ", params.sdft_n_samples_one_valid.value
print "skip_param: ", params.skip_param.value




 