"""
...TODO
"""
import logging
import Gateway
import Cmd
import Tool

###################################################################################################

@Cmd.route(r'gateway\s*list')
def cmd_gateway_list(params, cmd, index) -> tuple:
    """ Handle command 'gateway list' """
    err, ret = Gateway.get_gateway_list()
    return (err, ret)

###################################################################################################

@Cmd.route(r'gateway\[\]\s*list')
def cmd_gateway_task_list(params, cmd, index) -> tuple:
    """ Handle command 'gateway[] list' """
    err, ret = Gateway.get_gateway_task_list()
    return (err, ret)

###################################################################################################

@Cmd.route(r'gateway\s*info')
def cmd_gateway_info(params, cmd, index) -> tuple:
    """ Handle command 'gateway info <duid>' """
    ids = list(params.keys())
    return (None, ids)

###################################################################################################

@Cmd.route(r'gateway\[\]\s*clear')
def cmd_gateway_clear(params, cmd, index) -> tuple:
    """ Handle command '' """
    return (None, None)

###################################################################################################

@Cmd.route(r'gateway\[\]\s*add\s+(?P<duid>\w+)')
def cmd_gateway_add(params, cmd, index) -> tuple:
    """ Handle command 'gateway[] add <duid>' """
    err, ret = Gateway.task_add(params.get('duid', None))
    return (err, ret)

###################################################################################################

@Cmd.route(r'gateway\[(?P<index>\d+)\]\s*del')
def cmd_gateway_del(params, cmd, index) -> tuple:
    """ Handle command 'gateway[#] del' """
    err, ret = Gateway.task_del(index)
    return (err, ret)

###################################################################################################

@Cmd.route(r'gateway\[\]\s*del\s?all')
def cmd_gateway_del_all(params, cmd, index) -> tuple:
    """ Handle command 'gateway[] del all' """
    err, ret = Gateway.task_del_all()
    return (err, ret)

###################################################################################################

@Cmd.route(r'gateway\[(?P<index>\d+)\]\s*get\s*(?P<param>\w+)?')
def cmd_gateway_get(params, cmd, index) -> tuple:
    """ Handle command 'gateway[#] get <param> (no <param> for all)' """
    param = params.get('param', None)
    err, ret = Gateway.task_get_param(index, param)
    return (err, ret)

###################################################################################################

@Cmd.route(r'gateway\[(?P<index>\d+)\]\s*set\s+(?P<params>.+)')
def cmd_gateway_set(params, cmd, index) -> tuple:
    """ Handle command 'gateway[#] set <param>:<value> ...' """
    err, ret = Gateway.task_set_param(index, params)
    return (err, ret)

###################################################################################################

@Cmd.route(r'gateway\[(?P<index>\d+)\]\s*cmd')
def cmd_gateway_cmd(params, cmd, index) -> tuple:
    """ Handle command 'gateway[#] cmd <command>' """
    return (None, None)

###################################################################################################

@Cmd.route(r'gateway\[(?P<index>\d+)\]\s*html')
def cmd_gateway_html(params, cmd, index) -> tuple:
    """ Handle command 'gateway[#] html' """
    err, ret = Gateway.task_get_html(index)
    return (err, ret)

###################################################################################################

@Cmd.route(r'gateway\[(?P<index>\d+)\]\s*event')
def cmd_gateway_event(params, cmd, index) -> tuple:
    """ Handle command 'gateway[#] event' """
    return (None, None)

###################################################################################################

@Cmd.route(r'gateway\s*help')
def cmd_gateway_help(params, cmd, index) -> tuple:
    """ Handle command 'gateway help' """
    return (None, 'Help?!?')

###################################################################################################

@Cmd.route(r'gateway')
def cmd_gateway__(params, cmd, index) -> tuple:
    """ Handle command 'gateway help' """
    return (None, 'Häh? Type "gateway help" for help on gateway commands')

###################################################################################################
###################################################################################################
