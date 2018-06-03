"""
Global Properties and Functions
"""
import time

RUN = True
WEBSERVER = True
IOTDEVICE = True
VERSION = '0.0.?'

LOGLEVEL = 4   # 0=NoOutput, 1=Error, 2=Warning, 3=Info, 4=Debug, 5=Ext.Debug

LOG_ERROR = 1
LOG_WARN = 2
LOG_INFO = 3
LOG_DEBUG = 4
LOG_EXT_DEBUG = 5

try:   # try MicroPython
    import uos as os
    MICROPYTHON = True
    WEBSERVER = False
except:   # CPython
    MICROPYTHON = False

######## 

def time_to_str(t:time) -> str:
    y, m, d, hh, mm, ss, _, _, _ = time.localtime(t)
    t_str = "%04d-%02d-%02d %02d:%02d:%02d" % (y, m, d, hh, mm, ss)
    return t_str

########

def log(level:int, msg:str, *args):
    global LOGLEVEL

    if level>LOGLEVEL:
        return

    if args:
        msg = msg.format(*args)

    now_str = time_to_str(time.time())
    msg = '{0} [{1}] {2}'.format(now_str, level, msg)
    print(msg)

#######
