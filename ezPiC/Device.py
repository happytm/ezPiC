"""
...TODO
"""
try:   # CPython
    import os
    import re
    import json
    import random
except:   # MicroPython
    import uos as os
    import ure as re
    import ujson as json
    import urandom as random

import logging
from collections import namedtuple
import time

try:
    from threading import RLock
except:
    from _thread import allocate_lock as RLock

import Tool
import Scheduler

###################################################################################################
# Globals:

DEVICEPLUGINS = {}
DEVICES = []
DEVICELOCK = RLock()
DEVICETIMER = 0

DEVICETUPLE = namedtuple('Device', 'DUID NAME INFO module')
DEVICETASKTUPLE = namedtuple('DeviceTask', 'idx DUID NAME instname info inst')

###################################################################################################

def device_time_handler():
    global DEVICES, DEVICETIMER

    DEVICETIMER += 0.1
    Scheduler.add_event(DEVICETIMER, device_time_handler)

    with DEVICELOCK:
        t = time.time()

        for idx, task in enumerate(DEVICES):
            inst = task['inst']
            if inst.timer_next and (t >= inst.timer_next):
                if inst.timer_period:
                    inst.timer_next += inst.timer_period
                    if inst.timer_next < t:
                        inst.timer_next = t + inst.timer_period
                inst.timer()

###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    global DEVICEPLUGINS

    plugins = Tool.load_plugins('devices', 'dev')
    for plugin in plugins:
        try:
            DEVICEPLUGINS[plugin.DUID] = plugin
        except:
            pass

def load(config_all: dict):
    if not "devices" in config_all:
        return
    for config in config_all["devices"]:
        duid = config["duid"]
        loaded_version = config["version"]
        params = config["params"]
        err, idx = add(duid, params)
        running_version = DEVICES[idx]['inst'].version

        if not err and loaded_version != running_version:
            logging.warn("task " +  duid + " has change version form " + loaded_version + " to " + running_version)

def save(append: dict = None):
    err = None
    ret = []
    with DEVICELOCK:
        for task in DEVICES:
            try:
                inst = task['inst']
                config = {}
                config["duid"] = inst.module.DUID
                config["version"] = inst.version
                config["params"] = inst.get_param()
                ret.append(config)
            except Exception as e:
                err = e
                print(e)

    if not append is None:
        append["devices"] = ret
        return (err, append)
    
    return (err, {"devices": ret})

###################################################################################################

def run():
    """ TODO """
    global DEVICEPLUGINS, DEVICETIMER

    DEVICETIMER = int(time.time() + 3)
    print(DEVICETIMER)
    Scheduler.add_event(DEVICETIMER, device_time_handler)

###################################################################################################
###################################################################################################
###################################################################################################

def add(plugin_id: str, params: dict = None) -> tuple:
    """ TODO """
    err = None
    ret = None

    with DEVICELOCK:
        try:
            module = DEVICEPLUGINS.get(plugin_id, None)
            if module:
                task = {}
                inst = module.PluginDevice(module)
                task['inst'] = inst
                DEVICES.append(task)
                ret = len(DEVICES) - 1
                if params:
                    inst.set_param(params)
                if inst.timer_period:
                    inst.timer_next = time.time() + inst.timer_period
                inst.init()
            else:
                err = 'Unknown DUID'
        except Exception as e:
            err = e

    return (err, ret)

###################################################################################################

def delete(idx: int) -> tuple:
    """ TODO """
    err = None
    ret = None

    with DEVICELOCK:
        try:
            inst = DEVICES[idx]['inst']
            inst.exit()
            del DEVICES[idx]
        except Exception as e:
            err = e

    return (err, ret)

###################################################################################################

def clear() -> tuple:
    """ TODO """
    global DEVICES
    err = None
    ret = None

    with DEVICELOCK:
        for task in DEVICES:
            try:
                inst = task['inst']
                inst.exit()
            except Exception as e:
                err = e
        DEVICES = []

    return (err, ret)

###################################################################################################

def get_plugin_list() -> tuple:
    """ TODO """
    dl = []
    err = None

    with DEVICELOCK:
        for duid, module in DEVICEPLUGINS.items():
            dl.append(DEVICETUPLE(module.DUID, module.NAME, module.INFO, module.__name__))

    return (err, dl)

###################################################################################################

def get_list() -> tuple:
    """ TODO """
    dtl = []
    err = None

    with DEVICELOCK:
        for idx, task in enumerate(DEVICES):
            inst = task['inst']
            dtl.append(DEVICETASKTUPLE(idx, inst.module.DUID, inst.module.NAME, inst.get_name(), inst.get_info(), None))

    return (err, dtl)

###################################################################################################

def get_param(idx: int, key: str=None) -> tuple:
    """ TODO """
    err = None
    ret = None

    with DEVICELOCK:
        try:
            inst = DEVICES[idx]['inst']
            ret = inst.get_param(key)
        except Exception as e:
            err = e

    return (err, ret)

###################################################################################################

def set_param(idx: int, params: dict) -> tuple:
    """ TODO """
    err = None
    ret = None

    with DEVICELOCK:
        try:
            inst = DEVICES[idx]['inst']
            ret = inst.set_param(params)
        except Exception as e:
            err = e

    return (err, ret)

###################################################################################################

def get_html(idx: int) -> tuple:
    """ TODO """
    err = None
    ret = 'None'

    with DEVICELOCK:
        try:
            inst = DEVICES[idx]['inst']
            ret = inst.get_html()
        except Exception as e:
            err = e

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

    def get_name(self) -> str:
        """ get the name from the module """
        return self.param.get('name', 'Unknown')

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
        return 'www/devices/{}.html'.format(self.module.DUID)

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
