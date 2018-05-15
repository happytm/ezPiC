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

PLUGINDIR = 'dev/plugins/gadgets'
GADGETPLUGINS = {}
GADGETS = []
GADGETLOCK = RLock()
GADGETTIMER = 0

###################################################################################################

def gadget_time_handler():
    global GADGETS, GADGETTIMER

    GADGETTIMER += 0.1
    Scheduler.add_event(GADGETTIMER, gadget_time_handler)

    with GADGETLOCK:
        t = time.time()

        for idx, gadget in enumerate(GADGETS):
            if gadget.timer_next and (t >= gadget.timer_next):
                if gadget.timer_period:
                    gadget.timer_next += gadget.timer_period
                    if gadget.timer_next < t:
                        gadget.timer_next = t + gadget.timer_period
                gadget.timer()

###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    global GADGETPLUGINS

    plugins = Tool.load_plugins(PLUGINDIR, 'gg')
    for plugin in plugins:
        try:
            GADGETPLUGINS[plugin.DUID] = plugin
        except:
            pass

def load(config_all: dict):
    if not "gadgets" in config_all:
        return
    for config in config_all["gadgets"]:
        duid = config["duid"]
        loaded_version = config["version"]
        params = config["params"]
        err, idx = add(duid, params)
        running_version = GADGETS[idx].version

        if not err and loaded_version != running_version:
            logging.warn("task " +  duid + " has change version form " + loaded_version + " to " + running_version)

def save(append: dict = None):
    err = None
    ret = []
    with GADGETLOCK:
        for gadget in GADGETS:
            try:
                config = {}
                config["duid"] = gadget.module.DUID
                config["version"] = gadget.version
                config["params"] = gadget.get_param()
                ret.append(config)
            except Exception as e:
                err = -1
                ret = str(e)

    if not append is None:
        append["gadgets"] = ret
        return (err, append)
    
    return (err, {"gadgets": ret})

###################################################################################################

def run():
    """ TODO """
    global GADGETPLUGINS, GADGETTIMER

    GADGETTIMER = int(time.time() + 3)
    print(GADGETTIMER)
    Scheduler.add_event(GADGETTIMER, gadget_time_handler)

###################################################################################################
###################################################################################################
###################################################################################################

def add(plugin_id: str, params: dict = None) -> tuple:
    """ TODO """
    err = None
    ret = None

    with GADGETLOCK:
        try:
            module = GADGETPLUGINS.get(plugin_id, None)
            if module:
                gadget = module.PluginGadget(module)
                GADGETS.append(gadget)
                ret = len(GADGETS) - 1
                if params:
                    gadget.set_param(params)
                if gadget.timer_period:
                    gadget.timer_next = time.time() + gadget.timer_period
                gadget.init()
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

    with GADGETLOCK:
        try:
            gadget = GADGETS[idx]
            gadget.exit()
            del GADGETS[idx]
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

###################################################################################################

def clear() -> tuple:
    """ TODO """
    global GADGETS
    err = None
    ret = None

    with GADGETLOCK:
        for gadget in GADGETS:
            try:
                gadget.exit()
            except Exception as e:
                err = -1
                ret = str(e)
        GADGETS = []

    return (err, ret)

###################################################################################################

def get_plugin_list() -> tuple:
    """ TODO """
    pl = []
    err = None

    with GADGETLOCK:
        for duid, module in GADGETPLUGINS.items():
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

    with GADGETLOCK:
        for idx, gadget in enumerate(GADGETS):
            d = {}
            d['idx'] = idx
            d['DUID'] = gadget.module.DUID
            d['NAME'] = gadget.module.NAME
            d['name'] = gadget.get_name()
            d['info'] = gadget.get_info()
            dl.append(d)

    return (err, dl)

###################################################################################################

def get_param(idx: int, key: str=None) -> tuple:
    """ TODO """
    err = None
    ret = None

    with GADGETLOCK:
        try:
            gadget = GADGETS[idx]
            ret = gadget.get_param(key)
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

###################################################################################################

def set_param(idx: int, params: dict) -> tuple:
    """ TODO """
    err = None
    ret = None

    with GADGETLOCK:
        try:
            gadget = GADGETS[idx]
            ret = gadget.set_param(params)
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

###################################################################################################

def get_html(idx: int) -> tuple:
    """ TODO """
    err = None
    ret = 'None'

    with GADGETLOCK:
        try:
            gadget = GADGETS[idx]
            ret = gadget.get_html()
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

###################################################################################################
###################################################################################################
###################################################################################################

class PluginGadgetBase():
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
        return 'web/www/gadgets/{}.html'.format(self.module.DUID)

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
