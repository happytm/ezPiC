"""
...TODO
"""
import re
from threading import RLock
import time
#import logging
import Tool
import Scheduler

###################################################################################################
# Globals:

DEVICES = {}
DEVICETASKS = []
DEVICELOCK = RLock()
DEVICETIMER = 0

###################################################################################################

def device_time_handler():
    global DEVICETASKS, DEVICETIMER

    DEVICETIMER += 0.1
    Scheduler.add_event(DEVICETIMER, device_time_handler)

    DEVICELOCK.acquire()
    t = time.time()

    for idx, task in enumerate(DEVICETASKS):
        inst = task['inst']
        if inst.timer_next and (t >= inst.timer_next):
            if inst.timer_period:
                inst.timer_next += inst.timer_period
                if inst.timer_next < t:
                    inst.timer_next = t + inst.timer_period
            inst.timer()
    DEVICELOCK.release()

###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    global DEVICES

    plugins = Tool.load_plugins('devices', 'dev')
    #print(plugins)
    for plugin in plugins:
        try:
            DEVICES[plugin.DUID] = plugin
        except:
            pass

    #TEST
    module = DEVICES['TestA']
    dev = module.PluginDevice(module)
    x = dev.get_id()
    x = dev.get_info()
    x = dev.get_param('abc')
    x = dev.get_param()
    #DEVICETASKS.append(dev)
    #dev0 = DEVICETASKS[0]


    task_add('TestA')
    task_add('TestB')
    x = get_device_list()
    x = get_device_task_list()

    dev1 = DEVICETASKS[1]
    x = 0


###################################################################################################

def run():
    """ TODO """
    global DEVICES, DEVICETIMER

    DEVICETIMER = int(time.time() + 3)
    print(DEVICETIMER)
    Scheduler.add_event(DEVICETIMER, device_time_handler)

###################################################################################################
###################################################################################################
###################################################################################################

def task_add(plugin_id: str) -> tuple:
    """ TODO """
    err = None
    ret = None

    DEVICELOCK.acquire()
    try:
        module = DEVICES.get(plugin_id, None)
        if module:
            task = {}
            inst = module.PluginDevice(module)
            task['inst'] = inst
            DEVICETASKS.append(task)
            if inst.timer_period:
                inst.timer_next = time.time() + inst.timer_period
            inst.init()
        else:
            err = 'Unknown DUID'
    except Exception as e:
        err = e
    DEVICELOCK.release()

    return (err, ret)

###################################################################################################

def task_del(idx: int) -> tuple:
    """ TODO """
    err = None
    ret = None

    DEVICELOCK.acquire()
    try:
        inst = DEVICETASKS[idx]['inst']
        inst.exit()
        del DEVICETASKS[idx]
    except Exception as e:
        err = e
    DEVICELOCK.release()

    return (err, ret)

###################################################################################################

def get_device_list() -> tuple:
    """ TODO """
    dl = []
    err = None

    DEVICELOCK.acquire()
    for duid, module in DEVICES.items():
        dl.append((module.DUID, module.NAME, module.INFO, module))
    DEVICELOCK.release()

    return (err, dl)

###################################################################################################

def get_device_task_list() -> tuple:
    """ TODO """
    dtl = []
    err = None

    DEVICELOCK.acquire()
    for idx, task in enumerate(DEVICETASKS):
        inst = task['inst']
        dtl.append((idx, inst.get_id(), inst.get_name(), inst.get_info(), inst))
    DEVICELOCK.release()

    return (err, dtl)

###################################################################################################

def task_get_param(idx: int, key: str=None) -> tuple:
    """ TODO """
    err = None
    ret = None

    DEVICELOCK.acquire()
    try:
        inst = DEVICETASKS[idx]['inst']
        ret = inst.get_param(key)
    except Exception as e:
        err = e
    DEVICELOCK.release()

    return (err, ret)

###################################################################################################

def task_set_param(idx: int, params: dict) -> tuple:
    """ TODO """
    err = None
    ret = None

    DEVICELOCK.acquire()
    try:
        inst = DEVICETASKS[idx]['inst']
        ret = inst.set_param(params)
    except Exception as e:
        err = e
    DEVICELOCK.release()

    return (err, ret)

###################################################################################################

def task_get_html(idx: int) -> tuple:
    """ TODO """
    err = None
    ret = 'None'

    DEVICELOCK.acquire()
    try:
        inst = DEVICETASKS[idx]['inst']
        ret = inst.get_html()
    except Exception as e:
        err = e
    DEVICELOCK.release()

    return (err, ret)

###################################################################################################


###################################################################################################
###################################################################################################

class PluginDeviceBase():
    """ TODO """
    version = '1.0'

    def __init__(self, module):
        self.module = module
        self.param = {}
        self.timer_next = None
        self.timer_period = None

    def init(self):
        """ init a new instance after adding to task list or reinit an existing instance after loading/changing params """
        pass

    def exit(self):
        """ exit an existing instance after removing from task list """
        pass

    def get_id(self) -> str:
        """ get the unique device id from the module """
        return self.module.DUID

    def get_name(self) -> str:
        """ get the name from the module """
        return self.module.NAME

    def get_info(self) -> str:
        """ get the description from the module """
        return self.module.INFO

    def get_param(self, key: str=None):
        """ get the value for a given param key or get all key-value pairs as dict """
        if key:
            return self.param.get(key, None)
        else:
            return self.param

    def set_param(self, param_new: dict):
        """ updates the param key-value pairs with given dict """
        self.param.update(param_new)

    def get_html(self) -> str:
        """ get the html template name from the module """
        return 'devices/{}.html'.format(self.module.DUID)

    def meas(self) -> (dict, float):
        return ({}, 0.0)

    def cmd(self, cmd: str) -> str:
        return None

    def timer(self):
        return None

    def xxx(self):
        pass

###################################################################################################
###################################################################################################
###################################################################################################
