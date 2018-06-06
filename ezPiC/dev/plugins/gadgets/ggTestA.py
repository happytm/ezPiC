"""
Gadget Plugin for Testing
"""
from com.Globals import *

import random

import dev.Gadget as Gadget
import dev.Reading as Reading

#######
# Globals:

GGPID = 'TestA'
PNAME = 'Readable Name A'
PINFO = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

#######

class PluginGadget(Gadget.PluginGadgetBase):
    """ TODO """

    def __init__(self, module):
        super().__init__(module)
        self.param = {
            # must be params
            'name':'A',
            'enable':True,
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

# -----

    def init(self):
        t = float(self.param['timer'])
        if t>0:
            self.timer_period = t
        else:
            self.timer_period = None
        super().init()
        key = Reading.make_key(self.param['name'], self.param['name_t'])
        Reading.set_meta(key, '°C', '{:.3f}')

# -----

    def exit(self):
        super().exit()

# -----

    def timer(self, prepare:bool):
        log(5, 'ggTestA Timer')
        key = Reading.make_key(self.param['name'], self.param['name_t'])
        Reading.set(key, random.random())

#######
