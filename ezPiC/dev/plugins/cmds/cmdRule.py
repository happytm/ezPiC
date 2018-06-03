"""
Command Plugin for handling Rules
"""
from com.modules import *

import dev.Rule as Rule
import dev.Cmd as Cmd

#######

@Cmd.route('plugin.rule.list')
@Cmd.route('prl')
def cmd_rule_list(cmd:dict) -> tuple:
    """
    Handle command 'plugin.rule.list'.
    Returns a list of dicts with information about availabe rule modules 
    """
    err, ret = Rule.get_plugin_list()

    return (err, ret)

#######

@Cmd.route('rule.list')
@Cmd.route('rl')
def cmd_rule_task_list(cmd:dict) -> tuple:
    """ Handle command 'rule[] list' """
    err, ret = Rule.get_list()

    return (err, ret)

#######

@Cmd.route('plugin.rule.info', 'rupid')
def cmd_rule_info(cmd:dict) -> tuple:
    """ Handle command 'rule info <rupid>' """
    ids = list(cmd.keys())

    return (0, ids)

#######

@Cmd.route('rule.add', 'rupid')
def cmd_rule_add(cmd:dict) -> tuple:
    """ Handle command 'rule[] add <rupid>' """
    err, ret = Rule.add(cmd.get('rupid', None))

    return (err, ret)

#######

@Cmd.route('rule.clear')
@Cmd.route('rule.del.all')
def cmd_rule_del_all(cmd:dict) -> tuple:
    """ Handle command 'rule[] del all' """
    err, ret = Rule.clear()

    return (err, ret)

#######

@Cmd.route('rule.del.#')
def cmd_rule_del(cmd:dict) -> tuple:
    """ Handle command 'rule[#] del' """
    index = cmd['IDX']
    err, ret = Rule.delete(index)

    return (err, ret)

#######

@Cmd.route('rule.getparam.#', 'key')
def cmd_rule_get(cmd:dict) -> tuple:
    """ Handle command 'rule[#] get <param> (no <param> for all)' """
    index = cmd['IDX']
    key = cmd.get('key', None)
    err, ret = Rule.get_param(index, key)

    return (err, ret)

#######

@Cmd.route('rule.setparam.#', 'params')
def cmd_rule_set(cmd:dict) -> tuple:
    """ Handle command 'rule[#] set <param>:<value> ...' """
    index = cmd['IDX']
    params = cmd.get('params', None)
    if params and type(params) is str:
        params = json.loads(params)
    err, ret = Rule.set_param(index, params)

    return (err, ret)

#######

@Cmd.route('rule.cmd.#')
def cmd_rule_cmd(cmd:dict) -> tuple:
    """ Handle command 'rule[#] cmd <command>' """
    index = cmd['IDX']

    return (0, None)

#######

@Cmd.route('rule.gethtml.#')
def cmd_rule_html(cmd:dict) -> tuple:
    """ Handle command 'rule[#] html' """
    index = cmd['IDX']
    err, ret = Rule.get_html(index)

    return (err, ret)

#######

@Cmd.route('rule.event.#')
def cmd_rule_event(cmd:dict) -> tuple:
    """ Handle command 'rule[#] event' """
    index = cmd['IDX']

    return (0, None)

#######

@Cmd.route('rule.help')
def cmd_rule_help(cmd:dict) -> tuple:
    """ Handle command 'rule help' """
    return (0, 'Help?!?')

#######

@Cmd.route('rule')
def cmd_rule__(cmd:dict) -> tuple:
    """ Handle command 'rule help' """
    return (0, 'Häh? Type "rule help" for help on rule commands')

#######
