"""
Command Plugin for handling Gateways
"""
from com.modules import *

import dev.Gateway as Gateway
import dev.Cmd as Cmd

#######

@Cmd.route('plugin.gateway.list')
@Cmd.route('pgl')
def cmd_gateway_list(cmd:dict) -> tuple:
    """
    Handle command 'plugin.gateway.list'.
    Returns a list of dicts with information about availabe gateway modules 
    """
    err, ret = Gateway.get_plugin_list()

    return (err, ret)

#######

@Cmd.route('gateway.list')
@Cmd.route('gl')
def cmd_gateway_task_list(cmd:dict) -> tuple:
    """ Handle command 'gateway[] list' """
    err, ret = Gateway.get_list()

    return (err, ret)

#######

@Cmd.route('plugin.gateway.info', 'gwpid')
def cmd_gateway_info(cmd:dict) -> tuple:
    """ Handle command 'gateway info <gwpid>' """
    ids = list(cmd.keys())

    return (0, ids)

#######

@Cmd.route('gateway.add', 'ggpid')
def cmd_gateway_add(cmd:dict) -> tuple:
    """ Handle command 'gateway[] add <gwpid>' """
    err, ret = Gateway.add(cmd.get('gwpid', None))

    return (err, ret)

#######

@Cmd.route('gateway.clear')
@Cmd.route('gateway.del.all')
def cmd_gateway_del_all(cmd:dict) -> tuple:
    """ Handle command 'gateway[] del all' """
    err, ret = Gateway.clear()

    return (err, ret)

#######

@Cmd.route('gateway.del.#')
def cmd_gateway_del(cmd:dict) -> tuple:
    """ Handle command 'gateway[#] del' """
    index = cmd['IDX']
    err, ret = Gateway.delete(index)

    return (err, ret)

#######

@Cmd.route('gateway.getparam.#', 'key')
def cmd_gateway_get(cmd:dict) -> tuple:
    """ Handle command 'gateway[#] get <param> (no <param> for all)' """
    index = cmd['IDX']
    key = cmd.get('key', None)
    err, ret = Gateway.get_param(index, key)

    return (err, ret)

#######

@Cmd.route('gateway.setparam.#', 'params')
def cmd_gateway_set(cmd:dict) -> tuple:
    """ Handle command 'gateway[#] set <param>:<value> ...' """
    index = cmd['IDX']
    params = cmd.get('params', None)
    if params and type(params) is str:
        params = json.loads(params)
    err, ret = Gateway.set_param(index, params)

    return (err, ret)

#######

@Cmd.route('gateway.cmd.#')
def cmd_gateway_cmd(cmd:dict) -> tuple:
    """ Handle command 'gateway[#] cmd <command>' """
    index = cmd['IDX']

    return (0, None)

#######

@Cmd.route('gateway.gethtml.#')
def cmd_gateway_html(cmd:dict) -> tuple:
    """ Handle command 'gateway[#] html' """
    index = cmd['IDX']
    err, ret = Gateway.get_html(index)

    return (err, ret)

#######

@Cmd.route('gateway.event.#')
def cmd_gateway_event(cmd:dict) -> tuple:
    """ Handle command 'gateway[#] event' """
    index = cmd['IDX']

    return (0, None)

#######

@Cmd.route('gateway.help')
def cmd_gateway_help(cmd:dict) -> tuple:
    """ Handle command 'gateway help' """
    return (0, 'Help?!?')

#######

@Cmd.route('gateway')
def cmd_gateway__(cmd:dict) -> tuple:
    """ Handle command 'gateway help' """
    return (0, 'Häh? Type "gateway help" for help on gateway commands')

#######
