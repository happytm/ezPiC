"""
Command Plugin for Gateway handling
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
import Gateway
import Cmd
import Tool

###################################################################################################

@Cmd.route('plugin.gateway.list')
@Cmd.route('pgl')
def cmd_gateway_list(cmd:dict) -> dict:
    """
    Handle command 'plugin.gateway.list'.
    Returns a list of dicts with information about availabe gateway modules 
    """
    err, ret = Gateway.get_plugin_list()

    return Cmd.ret(err, ret)

###################################################################################################

@Cmd.route('gateway.list')
@Cmd.route('gl')
def cmd_gateway_task_list(cmd:dict) -> dict:
    """ Handle command 'gateway[] list' """
    err, ret = Gateway.get_list()

    return Cmd.ret(err, ret)

###################################################################################################

@Cmd.route('plugin.gateway.info', 'guid')
def cmd_gateway_info(cmd:dict) -> dict:
    """ Handle command 'gateway info <guid>' """
    ids = list(cmd.keys())

    return Cmd.ret(0, ids)

###################################################################################################

@Cmd.route('gateway.add', 'duid')
def cmd_gateway_add(cmd:dict) -> dict:
    """ Handle command 'gateway[] add <guid>' """
    err, ret = Gateway.add(cmd.get('guid', None))

    return Cmd.ret(err, ret)

###################################################################################################

@Cmd.route('gateway.clear')
@Cmd.route('gateway.del.all')
def cmd_gateway_del_all(cmd:dict) -> dict:
    """ Handle command 'gateway[] del all' """
    err, ret = Gateway.clear()

    return Cmd.ret(err, ret)

###################################################################################################

@Cmd.route('gateway.del.#')
def cmd_gateway_del(cmd:dict) -> dict:
    """ Handle command 'gateway[#] del' """
    index = cmd['IDX']
    err, ret = Gateway.delete(index)

    return Cmd.ret(err, ret)

###################################################################################################

@Cmd.route('gateway.getparam.#', 'key')
def cmd_gateway_get(cmd:dict) -> dict:
    """ Handle command 'gateway[#] get <param> (no <param> for all)' """
    index = cmd['IDX']
    key = cmd.get('key', None)
    err, ret = Gateway.get_param(index, key)

    return Cmd.ret(err, ret)

###################################################################################################

@Cmd.route('gateway.setparam.#', 'params')
def cmd_gateway_set(cmd:dict) -> dict:
    """ Handle command 'gateway[#] set <param>:<value> ...' """
    index = cmd['IDX']
    params = cmd.get('params', None)
    if params and type(params) is str:
        params = json.loads(params)
    err, ret = Gateway.set_param(index, params)

    return Cmd.ret(err, ret)

###################################################################################################

@Cmd.route('gateway.cmd.#')
def cmd_gateway_cmd(cmd:dict) -> dict:
    """ Handle command 'gateway[#] cmd <command>' """
    index = cmd['IDX']

    return Cmd.ret()

###################################################################################################

@Cmd.route('gateway.gethtml.#')
def cmd_gateway_html(cmd:dict) -> dict:
    """ Handle command 'gateway[#] html' """
    index = cmd['IDX']
    err, ret = Gateway.get_html(index)

    return Cmd.ret(err, ret)

###################################################################################################

@Cmd.route('gateway.event.#')
def cmd_gateway_event(cmd:dict) -> dict:
    """ Handle command 'gateway[#] event' """
    index = cmd['IDX']

    return Cmd.ret()

###################################################################################################

@Cmd.route('gateway.help')
def cmd_gateway_help(cmd:dict) -> dict:
    """ Handle command 'gateway help' """
    return Cmd.ret(0, 'Help?!?')

###################################################################################################

@Cmd.route('gateway')
def cmd_gateway__(cmd:dict) -> dict:
    """ Handle command 'gateway help' """
    return Cmd.ret(0, 'Häh? Type "gateway help" for help on gateway commands')

###################################################################################################
###################################################################################################
