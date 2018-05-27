"""
Global Properties and Functions
"""
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
    from time import time
except:   # CPython
    MICROPYTHON = False
    from datetime import datetime

MWS = None

#######

def log(level:int, msg:str, *args):
    global LOGLEVEL

    if level>LOGLEVEL:
        return

    if args:
        msg = msg.format(*args)

    if MICROPYTHON:
        localtime = time()
    else:
        localtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = '{0} [{1}] {2}'.format(localtime, level, msg)
    print(msg)

#######

def time_to_str(t):
    if MICROPYTHON:
        time_str = str(t)
    else:
        #time_str = datetime(t).strftime('%Y-%m-%d %H:%M:%S')
        time_str = datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
        #datetime.fromtimestamp()
    
    return time_str
    