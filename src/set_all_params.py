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
    #print "data_vector_type: ", params.data_vector_type.value
	#params.data_vector_offset.set_value(0)
    #print "data_vector_offset: ", params.data_vector_offset.value
    params.pga_gain.set_value(1)
    print "pga_gain: ", params.pga_gain.value
    params.num_pulses.set_value(4)
    print "num_pulses: ", params.num_pulses.value
    params.pulse_period.set_value(87)
    print "pulse_period: ", params.pulse_period.value
    params.pulse_width.set_value(40)
    print "pulse_width: ", params.pulse_width.value
	#params.res_hv.set_value(40)
    print "res_hv: ", params.res_hv.value

    #params.sdft_min_peak_value_th.set_value(0.5)
    print "\nsdft_min_peak_value_th: ", params.sdft_min_peak_value_th.value
    #params.sdft_k.set_value(39)
    print "sdft_k: ", params.sdft_k.value
	#params.sdft_n.set_value(107)
    print "sdft_n: ", params.sdft_n.value
    #params.sdft_i_min.set_value(450)
    print "sdft_i_min: ", params.sdft_i_min.value
	#params.sdft_min_eco_limit.set_value(30)
    print "sdft_min_eco_limit: ", params.sdft_min_eco_limit.value
	#params.sdft_max_eco_limit.set_value(80)
    print "sdft_max_eco_limit: ", params.sdft_max_eco_limit.value
	#params.sdft_var_norm.set_value(50000)
    print "sdft_var_norm: ", params.sdft_var_norm.value
    #params.sdft_peak.set_value(10)
    print "sdft_peak: ", params.sdft_peak.value
	#params.sdft_sound_speed.set_value(1495)
    print "sdft_sound_speed: ", params.sdft_sound_speed.value
	#params.sdft_sample_rate.set_value(2981)
    print "sdft_sample_rate: ", params.sdft_sample_rate.value
    #params.sdft_n_samples_one_valid.set_value(1)
    print "sdft_n_samples_one_valid: ", params.sdft_n_samples_one_valid.value
	#params.skip_param.set_value(20000)
    print "skip_param: ", params.skip_param.value

except KeyboardInterrupt:
	print "Keyboard Interrupt"

except Exception as e:
	print e

finally:
	print "closing socket"
	params.sdft_i_min.interface.close_socket()
