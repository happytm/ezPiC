"""
Command Plugin for handling Gadgets
"""
from com.Globals import *

import dev.Gadget as Gadget
import dev.Cmd as Cmd

#######

@Cmd.route('plugin.gadget.list')
@Cmd.route('pgdl')
def cmd_gadget_list(cmd:dict) -> tuple:
    """ gets a list of all available GADGET plugins """
    err, ret = Gadget.get_plugin_list()

    return (err, ret)

#######

@Cmd.route('gadget.list')
@Cmd.route('gdl')
def cmd_gadget_task_list(cmd:dict) -> tuple:
    """ gets a list of all GADGET instances """
    err, ret = Gadget.get_list()

    return (err, ret)

#######

@Cmd.route('plugin.gadget.info', 'ggpid')
def cmd_gadget_info(cmd:dict) -> tuple:
    """ gets information for a specific GADGET plugin """

    return (0, None)

#######

@Cmd.route('gadget.add', 'ggpid')
def cmd_gadget_add(cmd:dict) -> tuple:
    """ adds a new instance of a GADGET plugin """
    err, ret = Gadget.add(cmd.get('ggpid', None))

    return (err, ret)

#######

@Cmd.route('gadget.clear')
@Cmd.route('gadget.del.all')
def cmd_gadget_del_all(cmd:dict) -> tuple:
    """ remove all GADGET instances """
    err, ret = Gadget.clear()

    return (err, ret)

#######

@Cmd.route('gadget.del.#')
def cmd_gadget_del(cmd:dict) -> tuple:
    """ remove one GADGET instance """
    index = cmd['IDX']
    err, ret = Gadget.delete(index)

    return (err, ret)

#######

@Cmd.route('gadget.getparam.#', 'key')
def cmd_gadget_get(cmd:dict) -> tuple:
    """ gets params from one GADGET instance """
    index = cmd['IDX']
    key = cmd.get('key', None)
    err, ret = Gadget.get_param(index, key)

    return (err, ret)

#######

@Cmd.route('gadget.setparam.#', 'params')
def cmd_gadget_set(cmd:dict) -> tuple:
    """ sets params for one GADGET instance """
    index = cmd['IDX']
    params = cmd.get('params', None)
    if params and type(params) is str:
        params = json.loads(params)
    err, ret = Gadget.set_param(index, params)

    return (err, ret)

#######

@Cmd.route('gadget.gethtml.#')
def cmd_gadget_html(cmd:dict) -> tuple:
    """ gets the correcponding html page name for the GADGET instance/plugin """
    index = cmd['IDX']
    err, ret = Gadget.get_html(index)

    return (err, ret)

#######
