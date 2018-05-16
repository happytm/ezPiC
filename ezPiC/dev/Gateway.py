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
import dev.Timer as Timer

###################################################################################################
# Globals:

PLUGINDIR = 'dev/plugins/gateways'
GATEWAYPLUGINS = {}
GATEWAYS = []
GATEWAYLOCK = RLock()
GATEWAYTIMER = 0

###################################################################################################

def gateway_timer_handler(args):
    global GATEWAYS, GATEWAYTIMER

    with GATEWAYLOCK:
        t = time.time()

        for idx, gateway in enumerate(GATEWAYS):
            if gateway.timer_next and (t >= gateway.timer_next):
                if gateway.timer_period:
                    gateway.timer_next += gateway.timer_period
                    if gateway.timer_next < t:
                        gateway.timer_next = t + gateway.timer_period
                gateway.timer()

###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    global GATEWAYPLUGINS

    plugins = Tool.load_plugins(PLUGINDIR, 'gw')
    for plugin in plugins:
        try:
            GATEWAYPLUGINS[plugin.GWPID] = plugin
        except:
            pass

###################################################################################################

def run():
    """ TODO """
    global GATEWAYPLUGINS, GATEWAYTIMER

    Timer.register_cyclic_hnadler(gateway_timer_handler)

###################################################################################################

def load(config_all: dict):
    if not "gateways" in config_all:
        return
    for config in config_all["gateways"]:
        gwpid = config["GWPID"]
        loaded_version = config["version"]
        params = config["params"]
        err, idx = add(gwpid, params)
        running_version = GATEWAYS[idx].version

        if not err and loaded_version != running_version:
            logging.warn("task " +  gwpid + " has change version form " + loaded_version + " to " + running_version)

###################################################################################################

def save(append: dict = None):
    err = None
    ret = []
    with GATEWAYLOCK:
        for gateway in GATEWAYS:
            try:
                config = {}
                config["GWPID"] = gateway.module.GWPID
                config["version"] = gateway.version
                config["params"] = gateway.get_param()
                ret.append(config)
            except Exception as e:
                err = -1
                ret = str(e)

    if not append is None:
        append["gateways"] = ret
        return (err, append)
    
    return (err, {"gateways": ret})

###################################################################################################
###################################################################################################
###################################################################################################

def add(plugin_id: str, params: dict = None) -> tuple:
    """ TODO """
    err = None
    ret = None

    with GATEWAYLOCK:
        try:
            module = GATEWAYPLUGINS.get(plugin_id, None)
            if module:
                gateway = module.PluginGateway(module)
                GATEWAYS.append(gateway)
                ret = len(GATEWAYS) - 1
                if params:
                    gateway.set_param(params)
                if gateway.timer_period:
                    gateway.timer_next = time.time() + gateway.timer_period
                gateway.init()
            else:
                err = 'Unknown GWPID'
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

###################################################################################################

def delete(idx: int) -> tuple:
    """ TODO """
    err = None
    ret = None

    with GATEWAYLOCK:
        try:
            gateway = GATEWAYS[idx]
            gateway.exit()
            del GATEWAYS[idx]
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

###################################################################################################

def clear() -> tuple:
    """ TODO """
    global GATEWAYS
    err = None
    ret = None

    with GATEWAYLOCK:
        for gateway in GATEWAYS:
            try:
                gateway.exit()
            except Exception as e:
                err = -1
                ret = str(e)
        GATEWAYS = []

    return (err, ret)

###################################################################################################

def get_plugin_list() -> tuple:
    """ TODO """
    pl = []
    err = None

    with GATEWAYLOCK:
        for gwpid, module in GATEWAYPLUGINS.items():
            p = {}
            p['GWPID'] = module.GWPID
            p['PNAME'] = module.PNAME
            p['PINFO'] = module.PINFO
            p['PFILE'] = module.__name__
            pl.append(p)

    return (err, pl)

###################################################################################################

def get_list() -> tuple:
    """ TODO """
    gl = []
    err = None

    with GATEWAYLOCK:
        for idx, gateway in enumerate(GATEWAYS):
            g = {}
            g['idx'] = idx
            g['GWPID'] = gateway.module.GWPID
            g['PNAME'] = gateway.module.PNAME
            g['name'] = gateway.get_name()
            g['info'] = gateway.get_info()
            gl.append(g)

    return (err, gl)

###################################################################################################

def get_param(idx: int, key: str=None) -> tuple:
    """ TODO """
    err = None
    ret = None

    with GATEWAYLOCK:
        try:
            gateway = GATEWAYS[idx]
            ret = gateway.get_param(key)
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

###################################################################################################

def set_param(idx: int, params: dict) -> tuple:
    """ TODO """
    err = None
    ret = None

    with GATEWAYLOCK:
        try:
            gateway = GATEWAYS[idx]
            ret = gateway.set_param(params)
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

###################################################################################################

def get_html(idx: int) -> tuple:
    """ TODO """
    err = None
    ret = 'None'

    with GATEWAYLOCK:
        try:
            gateway = GATEWAYS[idx]
            ret = gateway.get_html()
        except Exception as e:
            err = -1
            ret = str(e)

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
        return str(self.param)

    def get_param(self, key:str=None):
        """ get the value for a given param key or get all key-value pairs as dict """
        if key:
            return self.param.get(key, None)
        else:
            return self.param

    def set_param(self, param_new:dict):
        """ updates the param key-value pairs with given dict """
        self.param.update(param_new)

    def get_html(self) -> str:
        """ get the html template name from the module """
        return 'web/www/gateways/{}.html'.format(self.module.GWPID)

    def meas(self) -> (dict, float):
        return ({}, 0.0)

    def cmd(self, cmd: str) -> str:
        return None

    def timer(self):
        return None

###################################################################################################
###################################################################################################
###################################################################################################
