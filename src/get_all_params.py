import sys
from Fuelsensor_interface import Fuelsensor_interface
from Fuelsensor_interface import Params

if len(sys.argv) == 3:
    fs = Fuelsensor_interface(str(sys.argv[1]), int(sys.argv[2]))
else:
    fs = Fuelsensor_interface('192.168.100.187', 5000)

params = Params(fs)

try:
    params.sdft_i_min.interface.connect()
    params.data_vector_type.get_value()
    print "data_vector_type: ", params.data_vector_type.value
    params.data_vector_offset.get_value()
    print "data_vector_offset: ", params.data_vector_offset.value
    params.pga_gain.get_value()
    print "pga_gain: ", params.pga_gain.value
    params.num_pulses.get_value()
    print "num_pulses: ", params.num_pulses.value
    params.pulse_period.get_value()
    print "pulse_period: ", params.pulse_period.value
    params.pulse_width.get_value()
    print "pulse_width: ", params.pulse_width.value
    params.res_hv.get_value()
    print "res_hv: ", params.res_hv.value


    params.sdft_min_peak_value_th.get_value()
    print "\nsdft_min_peak_value_th: ", params.sdft_min_peak_value_th.value
    params.sdft_k.get_value()
    print "sdft_k: ", params.sdft_k.value
    params.sdft_n.get_value()
    print "sdft_n: ", params.sdft_n.value
    params.sdft_i_min.get_value()
    print "sdft_i_min: ", params.sdft_i_min.value
    params.sdft_min_eco_limit.get_value()
    print "sdft_min_eco_limit: ", params.sdft_min_eco_limit.value
    params.sdft_max_eco_limit.get_value()
    print "sdft_max_eco_limit: ", params.sdft_max_eco_limit.value
    params.sdft_var_norm.get_value()
    print "sdft_var_norm: ", params.sdft_var_norm.value
    params.sdft_peak.get_value()
    print "sdft_peak: ", params.sdft_peak.value
    params.sdft_sound_speed.get_value()
    print "sdft_sound_speed: ", params.sdft_sound_speed.value
    params.sdft_sample_rate.get_value()
    print "sdft_sample_rate: ", params.sdft_sample_rate.value
    params.sdft_n_samples_one_valid.get_value()
    print "sdft_n_samples_one_valid: ", params.sdft_n_samples_one_valid.value
    params.skip_param.get_value()
    print "skip_param: ", params.skip_param.value

finally:
	params.sdft_i_min.interface.close_socket()
