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

GATEWAYS = {}
GATEWAYTASKS = []
GATEWAYLOCK = RLock()
GATEWAYTIMER = 0

GATEWAYTUPLE = namedtuple('Gateway', 'GUID NAME INFO module')
GATEWAYTASKTUPLE = namedtuple('GatewayTask', 'idx GUID NAME instname info inst')

###################################################################################################

def gateway_time_handler():
    global GATEWAYTASKS, GATEWAYTIMER

    GATEWAYTIMER += 0.1
    Scheduler.add_event(GATEWAYTIMER, gateway_time_handler)

    with GATEWAYLOCK:
        t = time.time()

        for idx, task in enumerate(GATEWAYTASKS):
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
    global GATEWAYS

    plugins = Tool.load_plugins('gateways', 'gtw')
    for plugin in plugins:
        try:
            GATEWAYS[plugin.GUID] = plugin
        except:
            pass

def load(config_all: dict):
    if not "gateways" in config_all:
        return
    for config in config_all["gateways"]:
        guid = config["guid"]
        loaded_version = config["version"]
        params = config["params"]
        err, idx = task_add(guid, params)
        running_version = GATEWAYTASKS[idx]['inst'].version

        if not err and loaded_version != running_version:
            logging.warn("task " +  guid + " has change version form " + loaded_version + " to " + running_version)

def save(append: dict = None):
    err = None
    ret = []
    with GATEWAYLOCK:
        for task in GATEWAYTASKS:
            try:
                inst = task['inst']
                config = {}
                config["guid"] = inst.module.GUID
                config["version"] = inst.version
                config["params"] = inst.get_param()
                ret.append(config)
            except Exception as e:
                err = e
                print(e)

    if not append is None:
        append["gateways"] = ret
        return (err, append)
    
    return (err, {"gateways": ret})

###################################################################################################

def run():
    """ TODO """
    global GATEWAYS, GATEWAYTIMER

    GATEWAYTIMER = int(time.time() + 3)
    print(GATEWAYTIMER)
    Scheduler.add_event(GATEWAYTIMER, gateway_time_handler)

###################################################################################################
###################################################################################################
###################################################################################################

def task_add(plugin_id: str, params: dict = None) -> tuple:
    """ TODO """
    err = None
    ret = None

    with GATEWAYLOCK:
        try:
            module = GATEWAYS.get(plugin_id, None)
            if module:
                task = {}
                inst = module.PluginGateway(module)
                task['inst'] = inst
                GATEWAYTASKS.append(task)
                ret = len(GATEWAYTASKS) - 1
                if params:
                    inst.set_param(params)
                if inst.timer_period:
                    inst.timer_next = time.time() + inst.timer_period
                inst.init()
            else:
                err = 'Unknown GUID'
        except Exception as e:
            err = e

    return (err, ret)

###################################################################################################

def task_del(idx: int) -> tuple:
    """ TODO """
    err = None
    ret = None

    with GATEWAYLOCK:
        try:
            inst = GATEWAYTASKS[idx]['inst']
            inst.exit()
            del GATEWAYTASKS[idx]
        except Exception as e:
            err = e

    return (err, ret)

###################################################################################################

def task_del_all() -> tuple:
    """ TODO """
    global GATEWAYTASKS
    err = None
    ret = None

    with GATEWAYLOCK:
        for task in GATEWAYTASKS:
            try:
                inst = task['inst']
                inst.exit()
            except Exception as e:
                err = e
        GATEWAYTASKS = []

    return (err, ret)

###################################################################################################

def get_gateway_list() -> tuple:
    """ TODO """
    dl = []
    err = None

    with GATEWAYLOCK:
        for guid, module in GATEWAYS.items():
            dl.append(GATEWAYTUPLE(module.GUID, module.NAME, module.INFO, module.__name__))

    return (err, dl)

###################################################################################################

def get_gateway_task_list() -> tuple:
    """ TODO """
    dtl = []
    err = None

    with GATEWAYLOCK:
        for idx, task in enumerate(GATEWAYTASKS):
            inst = task['inst']
            dtl.append(GATEWAYTASKTUPLE(idx, inst.module.GUID, inst.module.NAME, inst.get_name(), inst.get_info(), None))

    return (err, dtl)

###################################################################################################

def task_get_param(idx: int, key: str=None) -> tuple:
    """ TODO """
    err = None
    ret = None

    with GATEWAYLOCK:
        try:
            inst = GATEWAYTASKS[idx]['inst']
            ret = inst.get_param(key)
        except Exception as e:
            err = e

    return (err, ret)

###################################################################################################

def task_set_param(idx: int, params: dict) -> tuple:
    """ TODO """
    err = None
    ret = None

    with GATEWAYLOCK:
        try:
            inst = GATEWAYTASKS[idx]['inst']
            ret = inst.set_param(params)
        except Exception as e:
            err = e

    return (err, ret)

###################################################################################################

def task_get_html(idx: int) -> tuple:
    """ TODO """
    err = None
    ret = 'None'

    with GATEWAYLOCK:
        try:
            inst = GATEWAYTASKS[idx]['inst']
            ret = inst.get_html()
        except Exception as e:
            err = e

    return (err, ret)

###################################################################################################
###################################################################################################
###################################################################################################

class PluginGatewayBase():
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
        return 'www/gateways/{}.html'.format(self.module.GUID)

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
