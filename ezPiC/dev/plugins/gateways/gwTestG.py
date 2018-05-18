"""
Gateway Plugin for Testing
"""
import time

import dev.Gateway as Gateway
import dev.Reading as Reading
import G

###################################################################################################
# Globals:

GWPID = 'TestGatewayG'
PNAME = 'Readable Name G'
PINFO = 'Lorem ipsum dolor sit amet.'

###################################################################################################

class PluginGateway(Gateway.PluginGatewayBase):
    """ TODO """

    def __init__(self, module):
        super().__init__(module)
        self.param = {
            # must be params
            'name':'G',
            'enable':False,
            'timer':3,
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

    def init(self):
        pass

    def exit(self):
        pass

    def cmd(self, cmd:str) -> str:
        pass

    def timer(self):
        print('G' + str(time.time()))

    def readings(self, news:dict):
        G.log(G.LOG_INFO, 'Readings in gwTestG: {}', news)

###################################################################################################
