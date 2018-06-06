"""
Gadget Plugin for Testing
"""
from com.Globals import *

import random

import dev.Gadget as Gadget
import dev.Reading as Reading

#######
# Globals:

GGPID = 'TestB'
PNAME = 'Readable Name B'
PINFO = 'Fusce dolor leo, ornare vitae dolor nec, varius aliquam tellus.'

#######

class PluginGadget(Gadget.PluginGadgetBase):
    """ TODO """
    global _reading_tick

    def __init__(self, module):
        super().__init__(module)
        self.param = {
            # must be params
            'name':'B', 
            'enable':True,
            'timer':5,
            # instance specific params
            'abc':12345, 
            'xyz':67890
            }
        self.timer_period = 8.7654321

# -----

    def init(self):
        t = float(self.param['timer'])
        if t>0:
            self.timer_period = t
        else:
            self.timer_period = None
        super().init()
        key = Reading.make_key(self.param['name'], 'Voltage')
        Reading.set_meta(key, 'Volt', '{:.1f}')

# -----

    def exit(self):
        super().exit()

# -----

    def timer(self, prepare:bool):
        log(5, 'ggTestB Timer')
        key = Reading.make_key(self.param['name'], 'Voltage')
        Reading.set(key, random.random()*23.0)

#######
