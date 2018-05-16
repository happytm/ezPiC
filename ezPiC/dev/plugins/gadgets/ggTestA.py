"""
Gadget Plugin for Testing
"""
#import logging
import time

import dev.Gadget as Gadget
import dev.Reading as Reading
import Tool
import random

###################################################################################################
# Globals:

GGPID = 'TestA'
PNAME = 'Readable Name A'
PINFO = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vitae neque nisi. Vivamus consectetur sapien eget venenatis faucibus. Quisque elementum, neque ut accumsan scelerisque, sapien augue dictum nibh, id porttitor ex felis sed neque. Aenean imperdiet venenatis arcu nec hendrerit. Suspendisse ultricies massa elementum ligula vehicula, ut tristique leo dignissim. Sed sed urna fringilla, tempor mi quis, efficitur quam. Etiam ut enim purus. Donec convallis pretium nibh vel gravida.'

###################################################################################################

class PluginGadget(Gadget.PluginGadgetBase):
    """ TODO """

    def __init__(self, module):
        super().__init__(module)
        self.param = {
            # must be params
            'name':'A',
            'enable':False,
            'timer':10,
            # instance specific params
            'name_t':'T',
            'name_h':'H',
            'name_p':'P',
            'abc':123,
            'xyz':456,
            'sel':2,
            'qwe':'Lorem ipsum',
            'asd':[1,2,3,4,5],
            }
        self.timer_period = 3.1415

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
        Reading.set('Lorem.'+self.param['name'], random.random())

###################################################################################################
###################################################################################################
###################################################################################################
