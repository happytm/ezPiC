"""
Gateway Plugin for Testing
"""
from com.modules import *

import com.G as G
import dev.Gateway as Gateway
import dev.Reading as Reading

#######
# Globals:

GWPID = 'TestGatewayG'
PNAME = 'Readable Name G'
PINFO = 'Lorem ipsum dolor sit amet.'

#######

class PluginGateway(Gateway.PluginGatewayBase):
    """ TODO """

    def __init__(self, module):
        super().__init__(module)
        self.param = {
            # must be params
            'name':'G',
            'enable':False,
            'timer':3,
            'filter':'',
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
        self.timer_period = 2.7
        #self._reading_tick = 0

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

    def timer(self):
        print('G' + str(time.time()))

# -----

    def readings(self, news:dict):
        G.log(G.LOG_INFO, 'Readings in gwTestG: {}', news)

#######
