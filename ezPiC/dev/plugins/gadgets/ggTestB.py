"""
Gadget Plugin for Testing
"""
import time
import dev.Gadget as Gadget
import dev.Reading as Reading
import random

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
            'enable':False,
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

# -----

    def exit(self):
        super().exit()

# -----

    def timer(self, prepare:bool):
        print('B' + str(time.time()))
        Reading.set('Ipsum.'+self.param['name'], random.random())

#######
