"""
Command Plugin for handling Gateways
"""
from com.Globals import *

import dev.Gateway as Gateway
import dev.Cmd as Cmd

#######

@Cmd.route('plugin.gateway.list')
@Cmd.route('pgyl')
def cmd_gateway_list(cmd:dict) -> tuple:
    """ gets a list of all available GATEWAY plugins """
    err, ret = Gateway.get_plugin_list()

    return (err, ret)

#######

@Cmd.route('gateway.list')
@Cmd.route('gyl')
def cmd_gateway_task_list(cmd:dict) -> tuple:
    """ gets a list of all GATEWAY instances """
    err, ret = Gateway.get_list()

    return (err, ret)

#######

@Cmd.route('plugin.gateway.info', 'gwpid')
def cmd_gateway_info(cmd:dict) -> tuple:
    """ gets information for a specific GATEWAY plugin """
    ids = list(cmd.keys())

    return (0, ids)

#######

@Cmd.route('gateway.add', 'ggpid')
def cmd_gateway_add(cmd:dict) -> tuple:
    """ adds a new instance of a GATEWAY plugin """
    err, ret = Gateway.add(cmd.get('gwpid', None))

    return (err, ret)

#######

@Cmd.route('gateway.clear')
@Cmd.route('gateway.del.all')
def cmd_gateway_del_all(cmd:dict) -> tuple:
    """ remove all GATEWAY instances """
    err, ret = Gateway.clear()

    return (err, ret)

#######

@Cmd.route('gateway.del.#')
def cmd_gateway_del(cmd:dict) -> tuple:
    """ remove one GATEWAY instance """
    index = cmd['IDX']
    err, ret = Gateway.delete(index)

    return (err, ret)

#######

@Cmd.route('gateway.getparam.#', 'key')
def cmd_gateway_get(cmd:dict) -> tuple:
    """ gets params from one GATEWAY instance """
    index = cmd['IDX']
    key = cmd.get('key', None)
    err, ret = Gateway.get_param(index, key)

    return (err, ret)

#######

@Cmd.route('gateway.setparam.#', 'params')
def cmd_gateway_set(cmd:dict) -> tuple:
    """ sets params for one GATEWAY instance """
    index = cmd['IDX']
    params = cmd.get('params', None)
    if params and type(params) is str:
        params = json.loads(params)
    err, ret = Gateway.set_param(index, params)

    return (err, ret)

#######

@Cmd.route('gateway.gethtml.#')
def cmd_gateway_html(cmd:dict) -> tuple:
    """ gets the correcponding html page name for the GATEWAY instance/plugin """
    index = cmd['IDX']
    err, ret = Gateway.get_html(index)

    return (err, ret)

#######
