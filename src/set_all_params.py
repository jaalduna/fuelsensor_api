import sys
from Fuelsensor_interface import Fuelsensor_interface
from Fuelsensor_interface import Params

if len(sys.argv) == 2:
    fs = Fuelsensor_interface(str(sys.argv[1]), 5000)
else:
    fs = Fuelsensor_interface('192.168.148.1', 5000)

params = Params(fs)
params.sdft_i_min.interface.connect()

try:
    params.pga_gain.set_value(2)
    params.num_pulses.set_value(30)
    params.pulse_period.set_value(88)
    params.pulse_width.set_value(10)

    #params.res_hv.set_value(40)
	#params.data_vector_type.set_value(0)
	#params.data_vector_offset.set_value(0)

    params.sdft_peak.set_value(5)
    params.sdft_min_peak_value_th.set_value(0.5)
    params.sdft_n.set_value(107)
    params.sdft_i_min.set_value(400)
    params.sdft_min_eco_limit.set_value(30)
    params.sdft_max_eco_limit.set_value(80)
    params.sdft_var_norm.set_value(50000)
    
    params.sdft_sound_speed.set_value(1660)
    params.sdft_sample_rate.set_value(2981)
    params.sdft_n_samples_one_valid.set_value(10)
    params.skip_param.set_value(20000)

    #calculate SDFT K parameter value
    params.sdft_n.get_value(verbose=False)
    params.pulse_period.get_value(verbose=False)
    k = int(round(100.0*params.sdft_n.value/params.pulse_period.value/2.5))       #K = N/(Pp*Fm)
    params.sdft_k.set_value(k)   
    
except KeyboardInterrupt:
	print "Keyboard Interrupt"

except Exception as e:
	print e

finally:
	params.sdft_i_min.interface.close_socket()
