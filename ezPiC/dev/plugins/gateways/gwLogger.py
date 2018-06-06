"""
Gateway Plugin for Testing
"""
from com.Globals import *

import com.Tool as Tool
import dev.Gateway as Gateway
import dev.Reading as Reading

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
            'enable':True,
            'timer':0,
            'filter':'',
            # instance specific params
            'file_name':'Logger.log',
            'separator':',',
            }
        self.timer_period = 0
        self._reading_tick = 0
        self._reading_filter = Reading.Filter()

# -----

    def init(self):
        t = float(self.param['timer'])
        if t>0:
            self.timer_period = t
        else:
            self.timer_period = None
        super().init()

        self._reading_filter.init(self.param['filter'])

# -----

    def exit(self):
        super().exit()

# -----

    def timer(self):
        log(5, 'gwLogger Timer')

# -----

    def readings(self, news:dict):
        separator = self.param['separator']
        try:
            if Reading.is_new(self._reading_tick):
                self._reading_tick, _news = Reading.get_news_full(self._reading_tick)
                with open(self.param['file_name'], 'a') as f:
                    for key, data in _news.items():
                        if not self._reading_filter.fits(key):
                            continue

                        t = data['time']
                        str_log = G.time_to_str(t)
                        str_log += separator
                        str_log += key
                        str_log += separator
                        str_log += str(data['value'])
                        log(LOG_DEBUG, 'Logger: {}', str_log)

                        str_log += '\n'
                        b = f.write(str_log)
            pass
        except:
            pass

#######
