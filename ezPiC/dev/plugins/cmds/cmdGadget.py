"""
Command Plugin for Gadget handling
"""
try:   # CPython
    import json
except:   # MicroPython
    import ujson as json

import dev.Gadget as Gadget
import dev.Cmd as Cmd
import G

#####

@Cmd.route('plugin.gadget.list')
@Cmd.route('pdl')
def cmd_gadget_list(cmd:dict) -> tuple:
    """
    Handle command 'plugin.gadget.list'.
    Returns a list of dicts with information about availabe gadget modules
    """
    err, ret = Gadget.get_plugin_list()

    return (err, ret)

#####

@Cmd.route('gadget.list')
@Cmd.route('dl')
def cmd_gadget_task_list(cmd:dict) -> tuple:
    """ Handle command 'gadget[] list' """
    err, ret = Gadget.get_list()

    return (err, ret)

#####

@Cmd.route('plugin.gadget.info', 'ggpid')
def cmd_gadget_info(cmd:dict) -> tuple:
    """ Handle command 'gadget info <ggpid>' """

    return (0, None)

#####

@Cmd.route('gadget.add', 'ggpid')
def cmd_gadget_add(cmd:dict) -> tuple:
    """ Handle command 'gadget[] add <ggpid>' """
    err, ret = Gadget.add(cmd.get('ggpid', None))

    return (err, ret)

#####

@Cmd.route('gadget.clear')
@Cmd.route('gadget.del.all')
def cmd_gadget_del_all(cmd:dict) -> tuple:
    """ Handle command 'gadget[] del all' """
    err, ret = Gadget.clear()

    return (err, ret)

#####

@Cmd.route('gadget.del.#')
def cmd_gadget_del(cmd:dict) -> tuple:
    """ Handle command 'gadget.del.<index>' """
    index = cmd['IDX']
    err, ret = Gadget.delete(index)

    return (err, ret)

#####

@Cmd.route('gadget.getparam.#', 'key')
def cmd_gadget_get(cmd:dict) -> tuple:
    """ Handle command 'gadget[#] get <param> (no <param> for all)' """
    index = cmd['IDX']
    key = cmd.get('key', None)
    err, ret = Gadget.get_param(index, key)

    return (err, ret)

#####

@Cmd.route('gadget.setparam.#', 'params')
def cmd_gadget_set(cmd:dict) -> tuple:
    """ Handle command 'gadget[#] set <param>:<value> ...' """
    index = cmd['IDX']
    params = cmd.get('params', None)
    if params and type(params) is str:
        params = json.loads(params)
    err, ret = Gadget.set_param(index, params)

    return (err, ret)

#####

@Cmd.route('gadget.cmd.#', 'cmd')
def cmd_gadget_cmd(cmd:dict) -> tuple:
    """ Handle command 'gadget[#] cmd <command>' """
    index = cmd['IDX']

    return (0, None)

#####

@Cmd.route('gadget.gethtml.#')
def cmd_gadget_html(cmd:dict) -> tuple:
    """ Handle command 'gadget[#] html' """
    index = cmd['IDX']
    err, ret = Gadget.get_html(index)

    return (err, ret)

#####

@Cmd.route('gadget.event.#')
def cmd_gadget_event(cmd:dict) -> tuple:
    """ Handle command 'gadget[#] event' """
    index = cmd['IDX']

    return (0, None)

#####

@Cmd.route('gadget.help')
def cmd_gadget_help(cmd:dict) -> tuple:
    """ Handle command 'gadget help' """
    
    return (0, 'Help?!?')

#####
