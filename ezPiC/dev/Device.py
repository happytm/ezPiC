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
import time

try:
    from threading import RLock
except:
    from _thread import allocate_lock as RLock

import Tool
import dev.Scheduler as Scheduler

###################################################################################################
# Globals:

PLUGINDIR = 'dev/plugins/devices'
DEVICEPLUGINS = {}
DEVICES = []
DEVICELOCK = RLock()
DEVICETIMER = 0

###################################################################################################

def device_time_handler():
    global DEVICES, DEVICETIMER

    DEVICETIMER += 0.1
    Scheduler.add_event(DEVICETIMER, device_time_handler)

    with DEVICELOCK:
        t = time.time()

        for idx, device in enumerate(DEVICES):
            if device.timer_next and (t >= device.timer_next):
                if device.timer_period:
                    device.timer_next += device.timer_period
                    if device.timer_next < t:
                        device.timer_next = t + device.timer_period
                device.timer()

###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    global DEVICEPLUGINS

    plugins = Tool.load_plugins(PLUGINDIR, 'dev')
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
        running_version = DEVICES[idx].version

        if not err and loaded_version != running_version:
            logging.warn("task " +  duid + " has change version form " + loaded_version + " to " + running_version)

def save(append: dict = None):
    err = None
    ret = []
    with DEVICELOCK:
        for device in DEVICES:
            try:
                config = {}
                config["duid"] = device.module.DUID
                config["version"] = device.version
                config["params"] = device.get_param()
                ret.append(config)
            except Exception as e:
                err = -1
                ret = str(e)

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
                device = module.PluginDevice(module)
                DEVICES.append(device)
                ret = len(DEVICES) - 1
                if params:
                    device.set_param(params)
                if device.timer_period:
                    device.timer_next = time.time() + device.timer_period
                device.init()
            else:
                err = 'Unknown DUID'
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

###################################################################################################

def delete(idx: int) -> tuple:
    """ TODO """
    err = None
    ret = None

    with DEVICELOCK:
        try:
            device = DEVICES[idx]
            device.exit()
            del DEVICES[idx]
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

###################################################################################################

def clear() -> tuple:
    """ TODO """
    global DEVICES
    err = None
    ret = None

    with DEVICELOCK:
        for device in DEVICES:
            try:
                device.exit()
            except Exception as e:
                err = -1
                ret = str(e)
        DEVICES = []

    return (err, ret)

###################################################################################################

def get_plugin_list() -> tuple:
    """ TODO """
    pl = []
    err = None

    with DEVICELOCK:
        for duid, module in DEVICEPLUGINS.items():
            p = {}
            p['DUID'] = module.DUID
            p['NAME'] = module.NAME
            p['INFO'] = module.INFO
            p['MODULE'] = module.__name__
            pl.append(p)

    return (err, pl)

###################################################################################################

def get_list() -> tuple:
    """ TODO """
    dl = []
    err = None

    with DEVICELOCK:
        for idx, device in enumerate(DEVICES):
            d = {}
            d['idx'] = idx
            d['DUID'] = device.module.DUID
            d['NAME'] = device.module.NAME
            d['name'] = device.get_name()
            d['info'] = device.get_info()
            dl.append(d)

    return (err, dl)

###################################################################################################

def get_param(idx: int, key: str=None) -> tuple:
    """ TODO """
    err = None
    ret = None

    with DEVICELOCK:
        try:
            device = DEVICES[idx]
            ret = device.get_param(key)
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

###################################################################################################

def set_param(idx: int, params: dict) -> tuple:
    """ TODO """
    err = None
    ret = None

    with DEVICELOCK:
        try:
            device = DEVICES[idx]
            ret = device.set_param(params)
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

###################################################################################################

def get_html(idx: int) -> tuple:
    """ TODO """
    err = None
    ret = 'None'

    with DEVICELOCK:
        try:
            device = DEVICES[idx]
            ret = device.get_html()
        except Exception as e:
            err = -1
            ret = str(e)

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
        return 'web/www/devices/{}.html'.format(self.module.DUID)

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
