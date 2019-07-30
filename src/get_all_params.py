import sys
from Fuelsensor_interface import Fuelsensor_interface
from Fuelsensor_interface import Params

if len(sys.argv) == 3:
    fs = Fuelsensor_interface(str(sys.argv[1]), int(sys.argv[2]))
else:
    fs = Fuelsensor_interface('192.168.1.20', 5000)

params = Params(fs)

params.sdft_i_min.interface.connect()
params.data_vector_type.get_value()
params.data_vector_offset.get_value()
params.pga_gain.get_value()
params.num_pulses.get_value()
params.pulse_period.get_value()
params.pulse_width.get_value()
params.res_hv.get_value()

params.sdft_min_peak_value_th.get_value()
params.sdft_k.get_value()
params.sdft_n.get_value()
params.sdft_i_min.get_value()
params.sdft_min_eco_limit.get_value()
params.sdft_max_eco_limit.get_value()
params.sdft_var_norm.get_value()
params.sdft_peak.get_value()
params.sdft_sound_speed.get_value()
params.sdft_sample_rate.get_value()
params.sdft_n_samples_one_valid.get_value()
params.skip_param.get_value()

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

params.sdft_i_min.interface.close_socket()


 