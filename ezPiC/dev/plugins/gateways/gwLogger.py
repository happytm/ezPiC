"""
Gateway Plugin for Testing
"""
import time
from datetime import datetime

import dev.Gateway as Gateway
import dev.Reading as Reading
import com.G as G

#######
# Globals:

GWPID = 'FileLogger'
PNAME = 'Data Logger to File'
PINFO = 'Lorem ipsum dolor sit amet.'

#######

class PluginGateway(Gateway.PluginGatewayBase):
    """ TODO """

    def __init__(self, module):
        super().__init__(module)
        self.param = {
            # must be params
            'name':'Logger',
            'enable':False,
            'timer':0,
            # instance specific params
            'file_name':'Logger.log',
            'separator':',',
            }
        self.timer_period = 0
        self._reading_tick = 0

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
        separator = ', '
        try:
            if Reading.is_new(self._reading_tick):
                self._reading_tick, _news = Reading.get_news_full(self._reading_tick)
                with open(self.param['file_name'], 'a') as f:
                    for key, data in _news.items():
                        t = data['time']
                        str_log = G.time_to_str(t)
                        str_log += separator
                        str_log += key
                        str_log += separator
                        str_log += str(data['value'])
                        G.log(G.LOG_DEBUG, 'Logger: {}', str_log)

                        str_log += '\n'
                        b = f.write(str_log)
            pass
        except:
            pass

#######
