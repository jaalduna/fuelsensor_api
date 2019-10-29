import sys
from Fuelsensor_interface import Fuelsensor_interface
from Fuelsensor_interface import Params

if len(sys.argv) == 2:
    fs = Fuelsensor_interface(str(sys.argv[1]), 5000)
else:
    fs = Fuelsensor_interface('192.168.100.187', 5000)

params = Params(fs)

params.sdft_i_min.interface.connect()
params.pulse_period.get_value()
print "pulse_period: ", params.pulse_period.value

params.sdft_i_min.set_value(1000)
print params.sdft_i_min.value

params.sdft_n.get_value()
params.sdft_k.get_value()
params.sdft_k.set_value(49)
params.sdft_peak.set_value(10)
params.pga_gain.set_value(7)
params.num_pulses.set_value(10)
params.sdft_n_samples_one_valid.set_value(20)
params.sdft_min_peak_value_th.get_value()
params.sdft_min_peak_value_th.set_value(0.2)
print "N:", params.sdft_n.value
print "k:", params.sdft_k.value
print "sdft paek: ", params.sdft_peak.value
print "pga gain: ", params.pga_gain.value
print "num_pulses", params.num_pulses.value
print "min_peak_value_th: ", params.sdft_min_peak_value_th.value
fs.backup_params_to_flash()

params.sdft_i_min.interface.close_socket()


 