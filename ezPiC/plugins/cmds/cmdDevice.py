"""
...TODO
"""
import logging
import Device
import Cmd
import Tool

###################################################################################################

@Cmd.route(r'device\s*list')
@Cmd.route(r'dl\b')
def cmd_device_list(params, cmd, index) -> tuple:
    """ Handle command 'device list' """
    #logging.debug('cmdA ' + str(params))
    #x = params.get('x', '0')
    err, ret = Device.get_device_list()
    #print(ret)
    return (err, ret)

###################################################################################################

@Cmd.route(r'device\[\]\s*list')
def cmd_device_task_list(params, cmd, index) -> tuple:
    """ Handle command 'device[] list' """
    #logging.debug('cmdA ' + str(params))
    #x = params.get('x', '0')
    err, ret = Device.get_device_task_list()
    #print(ret)
    return (err, ret)

###################################################################################################

@Cmd.route(r'device\s*info')
def cmd_device_info(params, cmd, index) -> tuple:
    """ Handle command 'device info <duid>' """
    ids = list(params.keys())
    if ids:
        id = ids[0]
        #Device.get
    #logging.debug('cmdA ' + str(params))
    x = params.get('x', '0')
    return (None, ids)

###################################################################################################

@Cmd.route(r'device\[\]\s*clear')
def cmd_device_clear(params, cmd, index) -> tuple:
    """ Handle command '' """
    return (None, None)

###################################################################################################

@Cmd.route(r'device\[\]\s*add\s+(?P<duid>\w+)')
def cmd_device_add(params, cmd, index) -> tuple:
    """ Handle command 'device[] add <duid>' """
    err, ret = Device.task_add(params.get('duid', None))
    return (err, ret)

###################################################################################################

@Cmd.route(r'device\[(?P<index>\d+)\]\s*del')
def cmd_device_del(params, cmd, index) -> tuple:
    """ Handle command 'device[#] del' """
    err, ret = Device.task_del(index)
    return (err, ret)

###################################################################################################

@Cmd.route(r'device\[\]\s*del\s?all')
def cmd_device_del_all(params, cmd, index) -> tuple:
    """ Handle command 'device[] del all' """
    err, ret = Device.task_del_all()
    return (err, ret)

###################################################################################################

@Cmd.route(r'device\[(?P<index>\d+)\]\s*get\s*(?P<param>\w+)?')
def cmd_device_get(params, cmd, index) -> tuple:
    """ Handle command 'device[#] get <param> (no <param> for all)' """
    param = params.get('param', None)
    err, ret = Device.task_get_param(index, param)
    return (err, ret)

###################################################################################################

@Cmd.route(r'device\[(?P<index>\d+)\]\s*set\s+(?P<params>.+)')
def cmd_device_set(params, cmd, index) -> tuple:
    """ Handle command 'device[#] set <param>:<value> ...' """
    #paramdict = Tool.str_to_params(cmd)
    err, ret = Device.task_set_param(index, params)
    return (err, ret)

###################################################################################################

@Cmd.route(r'device\[(?P<index>\d+)\]\s*cmd')
def cmd_device_cmd(params, cmd, index) -> tuple:
    """ Handle command 'device[#] cmd <command>' """
    return (None, None)

###################################################################################################

@Cmd.route(r'device\[(?P<index>\d+)\]\s*html')
def cmd_device_html(params, cmd, index) -> tuple:
    """ Handle command 'device[#] html' """
    err, ret = Device.task_get_html(index)
    return (err, ret)

###################################################################################################

@Cmd.route(r'device\[(?P<index>\d+)\]\s*event')
def cmd_device_event(params, cmd, index) -> tuple:
    """ Handle command 'device[#] event' """
    return (None, None)

###################################################################################################

@Cmd.route(r'device\s*help')
def cmd_device_help(params, cmd, index) -> tuple:
    """ Handle command 'device help' """
    return (None, 'Help?!?')

###################################################################################################

@Cmd.route(r'device')
def cmd_device__(params, cmd, index) -> tuple:
    """ Handle command 'device help' """
    return (None, 'Häh? Type "device help" for help on device commands')

###################################################################################################
###################################################################################################

@Cmd.route(r'xping')
@Cmd.route(r'yping\b')
@Cmd.route(r'zping')
def cmd_testping(params, cmd, index) -> tuple:
    """ Handle command 'ping' and returns string 'pong' """
    logging.debug('Ping')
    return (None, 'dpong' + str(list(params.keys())))

###################################################################################################
###################################################################################################
