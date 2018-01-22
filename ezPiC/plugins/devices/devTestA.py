"""
...TestA...
"""
#import logging
import time
import Tool
import Device

###################################################################################################
# Globals:

DUID = 'TestA'
NAME = 'Readable Name A'
INFO = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vitae neque nisi. Vivamus consectetur sapien eget venenatis faucibus. Quisque elementum, neque ut accumsan scelerisque, sapien augue dictum nibh, id porttitor ex felis sed neque. Aenean imperdiet venenatis arcu nec hendrerit. Suspendisse ultricies massa elementum ligula vehicula, ut tristique leo dignissim. Sed sed urna fringilla, tempor mi quis, efficitur quam. Etiam ut enim purus. Donec convallis pretium nibh vel gravida.'

AAA = 1

###################################################################################################

class PluginDevice(Device.PluginDeviceBase):
    CID = 'TestA'
    address = 123
    param = {'abc':123, 'xyz':456}
    timer_period = 3.1415

    def __init__(self, module):
        super().__init__(module)

    def init(self):
        pass

    def exit(self):
        pass

    def meas(self) -> (dict, float):
        return ({}, 0.0)

    def cmd(self, cmd:str) -> str:
        pass

    def timer(self):
        print('A' + str(time.time()))

###################################################################################################
###################################################################################################
###################################################################################################
