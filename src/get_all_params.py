import sys
from Fuelsensor_interface import Fuelsensor_interface
from Fuelsensor_interface import Params

if len(sys.argv) == 3:
    fs = Fuelsensor_interface(str(sys.argv[1]), int(sys.argv[2]))
elif len(sys.argv) == 2:
    fs = Fuelsensor_interface(str(sys.argv[1]), 5000)
else:
    fs = Fuelsensor_interface('192.168.100.187',5000)

params = Params(fs)

try:
    params.sdft_i_min.interface.connect()

    params.pga_gain.get_value()
    params.num_pulses.get_value()
    params.pulse_period.get_value()
    params.pulse_width.get_value()

    params.res_hv.get_value()
    #params.data_vector_type.get_value()
    #params.data_vector_offset.get_value()

    params.sdft_k.get_value()
    params.sdft_n.get_value()
    params.sdft_var_norm.get_value()
    params.sdft_i_min.get_value()
    params.sdft_peak.get_value()
    params.sdft_min_peak_value_th.get_value()
    params.sdft_min_eco_limit.get_value()
    params.sdft_max_eco_limit.get_value()
    params.sdft_n_samples_one_valid.get_value()
    params.sdft_sound_speed.get_value()
    params.sdft_sample_rate.get_value()

    params.skip_param.get_value()

finally:
	params.sdft_i_min.interface.close_socket()
