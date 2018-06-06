"""
Command Plugin for handling Machine
"""
from com.modules import *

import dev.M as M
import dev.Machine as Machine
import dev.Cmd as Cmd

#######

@Cmd.route('plugin.machine.list')
@Cmd.route('pmal')
def cmd_machine_list(cmd:dict) -> tuple:
    """ gets a list of all available MACHINE plugins """
    err, ret = Machine.get_plugin_list()

    return (err, ret)

#######

@Cmd.route('machine.list')
@Cmd.route('mal')
def cmd_machine_task_list(cmd:dict) -> tuple:
    """ gets a list of all MACHINE instances """
    err, ret = Machine.get_list()

    return (err, ret)

#######

@Cmd.route('machine.getparam', 'key')
def cmd_machine_get(cmd:dict) -> tuple:
    """ gets params from MACHINE instances (merged) """
    key = cmd.get('key', None)
    err, ret = Machine.get_param(key)

    return (err, ret)

#######

@Cmd.route('machine.setparam', 'params')
def cmd_machine_set(cmd:dict) -> tuple:
    """ sets params for MACHINE instances (merged) """
    params = cmd.get('params', None)
    if params and type(params) is str:
        params = json.loads(params)
    err, ret = Machine.set_param(params)

    return (err, ret)

#######
