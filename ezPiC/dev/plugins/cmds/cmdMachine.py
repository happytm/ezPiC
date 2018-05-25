"""
Command Plugin for Machine handling
"""
try:   # CPython
    import json
except:   # MicroPython
    import ujson as json

import dev.Machine as Machine
import dev.Cmd as Cmd
import G
import dev.M as M

###################################################################################################

@Cmd.route('plugin.machine.list')
@Cmd.route('pml')
def cmd_machine_list(cmd:dict) -> dict:
    """
    Handle command 'plugin.machine.list'.
    Returns a list of dicts with information about availabe machine modules
    """
    err, ret = Machine.get_plugin_list()

    return Cmd.ret(err, ret)

###################################################################################################

@Cmd.route('machine.list')
@Cmd.route('ml')
def cmd_machine_task_list(cmd:dict) -> dict:
    """ Handle command 'machine[] list' """
    err, ret = Machine.get_list()

    return Cmd.ret(err, ret)

###################################################################################################

@Cmd.route('machine.getparam', 'key')
def cmd_machine_get(cmd:dict) -> dict:
    """ Handle command 'machine[#] get <param> (no <param> for all)' """
    key = cmd.get('key', None)
    err, ret = Machine.get_param(key)

    return Cmd.ret(err, ret)

###################################################################################################

@Cmd.route('machine.setparam', 'params')
def cmd_machine_set(cmd:dict) -> dict:
    """ Handle command 'machine[#] set <param>:<value> ...' """
    params = cmd.get('params', None)
    if params and type(params) is str:
        params = json.loads(params)
    err, ret = Machine.set_param(params)

    return Cmd.ret(err, ret)

###################################################################################################

@Cmd.route('machine.help')
def cmd_machine_help(cmd:dict) -> dict:
    """ Handle command 'machine help' """
    return Cmd.ret(0, 'Help?!?')

###################################################################################################
