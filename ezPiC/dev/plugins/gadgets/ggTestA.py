"""
Gadget Plugin for Testing
"""
import time

import dev.Gadget as Gadget
import dev.Reading as Reading
import random

#####
# Globals:

GGPID = 'TestA'
PNAME = 'Readable Name A'
PINFO = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

#####

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

# ---

    def init(self):
        t = float(self.param['timer'])
        if t>0:
            self.timer_period = t
        else:
            self.timer_period = None
        super().init()

# ---

    def exit(self):
        super().exit()

# ---

    def timer(self, prepare:bool):
        print('A' + str(time.time()))
        Reading.set('Lorem.'+self.param['name'], random.random())

#####
