"""
Command Plugin for Device handling
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
import Device
import Cmd
import Tool

###################################################################################################

@Cmd.route('plugin.device.list')
@Cmd.route('pdl')
def cmd_device_list(cmd: dict) -> dict:
    """
    Handle command 'plugin.device.list'.
    Returns a list of dicts with information about availabe device modules
    """
    err, ret = Device.get_plugin_list()

    return Cmd.ret(ret, err)

###################################################################################################

@Cmd.route('device.list')
@Cmd.route('dl')
def cmd_device_task_list(cmd: dict) -> dict:
    """ Handle command 'device[] list' """
    err, ret = Device.get_list()

    return Cmd.ret(ret, err)

###################################################################################################

@Cmd.route('plugin.device.info', 'duid')
def cmd_device_info(cmd: dict) -> dict:
    """ Handle command 'device info <duid>' """
    return Cmd.ret()

###################################################################################################

@Cmd.route('device.add', 'duid')
def cmd_device_add(cmd: dict) -> dict:
    """ Handle command 'device[] add <duid>' """
    err, ret = Device.add(cmd.get('duid', None))
    return Cmd.ret(ret, err)

###################################################################################################

@Cmd.route('device.clear')
@Cmd.route('device.del.all')
def cmd_device_del_all(cmd: dict) -> dict:
    """ Handle command 'device[] del all' """
    err, ret = Device.clear()
    return Cmd.ret(ret, err)

###################################################################################################

@Cmd.route('device.del.#')
def cmd_device_del(cmd: dict) -> dict:
    """ Handle command 'device.del.<index>' """
    index = cmd['IDX']
    err, ret = Device.delete(index)
    return Cmd.ret(ret, err)

###################################################################################################

@Cmd.route('device.getparam.#', 'key')
def cmd_device_get(cmd: dict) -> dict:
    """ Handle command 'device[#] get <param> (no <param> for all)' """
    index = cmd['IDX']
    key = cmd.get('key', None)
    err, ret = Device.get_param(index, key)
    return Cmd.ret(ret, err)

###################################################################################################

@Cmd.route('device.setparam.#', 'params')
def cmd_device_set(cmd: dict) -> dict:
    """ Handle command 'device[#] set <param>:<value> ...' """
    index = cmd['IDX']
    params = cmd.get('params', None)
    if params:
        params = json.loads(params)
    err, ret = Device.set_param(index, params)
    return Cmd.ret(ret, err)

###################################################################################################

@Cmd.route('device.cmd.#', 'cmd')
def cmd_device_cmd(cmd: dict) -> dict:
    """ Handle command 'device[#] cmd <command>' """
    index = cmd['IDX']
    return Cmd.ret(None, None)

###################################################################################################

@Cmd.route('device.gethtml.#')
def cmd_device_html(cmd: dict) -> dict:
    """ Handle command 'device[#] html' """
    err, ret = Device.get_html(index)
    return Cmd.ret(ret, err)

###################################################################################################

@Cmd.route('device.event.#')
def cmd_device_event(cmd: dict) -> dict:
    """ Handle command 'device[#] event' """
    index = cmd['IDX']
    return Cmd.ret(None, None)

###################################################################################################

@Cmd.route('device.help')
def cmd_device_help(cmd: dict) -> dict:
    """ Handle command 'device help' """
    return Cmd.ret(None, 'Help?!?')

###################################################################################################
###################################################################################################
