"""
Command Plugin for Machine handling
"""
try:   # CPython
    import json
except:   # MicroPython
    import ujson as json

import dev.Machine as Machine
import dev.Cmd as Cmd
import com.G as G
import dev.M as M

#######

@Cmd.route('plugin.machine.list')
@Cmd.route('pml')
def cmd_machine_list(cmd:dict) -> tuple:
    """
    Handle command 'plugin.machine.list'.
    Returns a list of dicts with information about availabe machine modules
    """
    err, ret = Machine.get_plugin_list()

    return (err, ret)

#######

@Cmd.route('machine.list')
@Cmd.route('ml')
def cmd_machine_task_list(cmd:dict) -> tuple:
    """ Handle command 'machine[] list' """
    err, ret = Machine.get_list()

    return (err, ret)

#######

@Cmd.route('machine.getparam', 'key')
def cmd_machine_get(cmd:dict) -> tuple:
    """ Handle command 'machine[#] get <param> (no <param> for all)' """
    key = cmd.get('key', None)
    err, ret = Machine.get_param(key)

    return (err, ret)

#######

@Cmd.route('machine.setparam', 'params')
def cmd_machine_set(cmd:dict) -> tuple:
    """ Handle command 'machine[#] set <param>:<value> ...' """
    params = cmd.get('params', None)
    if params and type(params) is str:
        params = json.loads(params)
    err, ret = Machine.set_param(params)

    return (err, ret)

#######

@Cmd.route('machine.help')
def cmd_machine_help(cmd:dict) -> tuple:
    """ Handle command 'machine help' """
    return (0, 'Help?!?')

#######
