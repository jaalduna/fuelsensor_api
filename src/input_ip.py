import paho.mqtt.client as mqtt
import random
import time
import json 
import sys
from Fuelsensor_interface import Fuelsensor_interface


class FuelMqtt(mqtt.Client,Fuelsensor_interface):
    def __init__(self,cname,ip,puerto):
        super(FuelMqtt, self).__init__(cname,ip,puerto)
        #super(FuelMqtt, self).__init__()
        #self.client = mqtt.Client(client_id='seba-pub', clean_session=False)
        self.fs_interface = Fuelsensor_interface(ip,puerto)
        self.altura = self.fs_interface.get_height()
        self.connect(host='127.0.0.1', port=1883)

    def on_connect(self, mqttc, obj, flags, rc):
        print "subscribing"
        print('connected (%s)' % self.client_id)
        self.subscribe(topic='camion/sensor', qos=2)

    def on_message(client, userdata, msg):
    	topic=msg.topic


fs_mqtt = FuelMqtt(cname='seba-pub',ip='192.168.100.187',puerto=5000)
fs_mqtt.publish("camion/sensor",fs_mqtt.altura)
time.sleep(1)
