"""
Temperature Sensors supported by the "dht" micropython module
"""
#import logging
import time
import Tool
import Device
import dht
import machine


###################################################################################################
# Globals:

DUID = 'DHTTempHumSensorDevice'
NAME = 'DHT / AM Temperature and Humidity Sensor Device'
INFO = 'Measurement device for the common DHT11 / DHT22 / DHT12 & AM2301 / AM2302 /  AM2320 / AM2321 / AM2322 .. Temperature and Humidity Sensors.'

###################################################################################################


class PluginDevice(Device.PluginDeviceBase):

    def __init__(self, module): # FIXME in base class, everywhere: shadowing of "module"
        super().__init__(module)
        self.param = {'name': 'DHT / AM Temperature and Humidity Sensor Device', 'machine_pin': 4, 'type': 'DHT11'} # TODO Allowed values / Lists / ...?
        self.timer_period = 3 # must be at least 1 (DHT11 type) or 2 (DHT22 type)
        self._sensor = None # TODO There should be a better way. (Device.setup(..) or whatever)

    def timer(self):
        if self._sensor is None:
            if self.param['type'] == "DHT11":
                # TODO try: Error reporting?
                self._sensor = dht.DHT11(machine.Pin(self.param['machine_pin']))
            elif self.param['type'] == "DHT22":
                self._sensor = dht.DHT22(machine.Pin(self.param['machine_pin']))

        self._sensor.measure()
        temp = self._sensor.temperature()
        hum = self._sensor.humidity()
        # TODO Where to go from here?


###################################################################################################
###################################################################################################
###################################################################################################

