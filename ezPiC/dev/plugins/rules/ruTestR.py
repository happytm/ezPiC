"""
Rule Plugin for Testing
"""
from com.modules import *

import dev.Rule as Rule
import dev.Reading as Reading

#######
# Globals:

RUPID = 'TestRuleR'
PNAME = 'Readable Name R'
PINFO = 'Lorem ipsum dolor sit amet.'

#######

class PluginRule(Rule.PluginRuleBase):
    """ TODO """

    def __init__(self, module):
        super().__init__(module)
        self.param = {
            # must be params
            'name':'G',
            'enable':True,
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
        G.log(5, 'rugTestR Timer')

# -----

    def readings(self, news:dict):
        G.log(G.LOG_INFO, 'Readings in ruTestR: {}', news)

#######
