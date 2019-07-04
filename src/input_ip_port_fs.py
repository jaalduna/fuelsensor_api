import paho.mqtt.client as mqtt
import random
import time
import json 
import sys
from Fuelsensor_interface import Fuelsensor_interface


class FuelMqtt(mqtt.Client,Fuelsensor_interface):
    def __init__(self,cname):
        super(FuelMqtt, self).__init__(cname)
        #super(FuelMqtt, self).__init__()
        #self.client = mqtt.Client(client_id='seba-pub', clean_session=False)
        if len(sys.argv) == 3:
            fs_interface = Fuelsensor_interface(str(sys.argv[1]),int(sys.argv[2]))
            self.fs_interface = fs_interface
        else:
             fs_interface = Fuelsensor_interface()

           
        
            #fs_interface = Fuelsensor_interface(str(sys.argv[1]), int(sys.argv[2]))
           
        #self.altura = self.get_height()
        self.altura = self.fs_interface.get_height()
        self.connect(host='127.0.0.1', port=1883)

    def on_connect(self, mqttc, obj, flags, rc):
        print "subscribing"
        print('connected (%s)' % self.client_id)
        self.subscribe(topic='camion/sensor', qos=2)

    def on_message(client, userdata, msg):
    	topic=msg.topic





fs_mqtt = FuelMqtt(cname='seba-pub')

#fs_mqtt.fs_interface.Fuelsensor_interface('192.168.100.187',5000)
#fs_mqtt.client.connect(host='127.0.0.1', port=1883)
#altura=fs_mqtt.altura()
#altura=float(fs_mqtt.altura())
print "publicando"
fs_mqtt.publish("camion/sensor",fs_mqtt.altura)
print 
time.sleep(1)

