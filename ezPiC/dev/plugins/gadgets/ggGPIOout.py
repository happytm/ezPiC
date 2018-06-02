"""
Gadget Plugin for GPIO output
"""
from com.modules import *

import dev.Gadget as Gadget
import dev.Reading as Reading

#######
# Globals:

GGPID = 'GPIOout'
PNAME = 'GPIO output'
PINFO = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

#######

class PluginGadget(Gadget.PluginGadgetBase):
    """ TODO """

    def __init__(self, module):
        super().__init__(module)
        self.param = {
            # must be params
            'name':'A',
            'enable':False,
            'timer':0,
            # instance specific params
            'out_key':'TimeSwitchOut',
            'out_val_0':'0 off OFF',
            'out_val_1':'1 on ON',
            'gpio':'',
            
            }

# -----

    def init(self):
        super().init()

        key = self.param['out_key']
        out = self._get_reading(key)

# -----

    def exit(self):
        super().exit()

# -----

    def readings(self, news:dict):
        try:
            key = self.param['out_key']
            if key in news:
                out = self._get_reading(key)
        except:
            pass

# =====

    def _get_reading(self, key):
        out = 0
        val = str(Reading.get(key))

        if self.param['out_val_0'] and self.param['out_val_0'].find(val) >= 0:
            out = 0
        if self.param['out_val_1'] and self.param['out_val_1'].find(val) >= 0:
            out = 1

        return out

#######
