"""
...TODO
"""
import logging
import Device

###################################################################################################

def cmd_device_list(params, cmd, index) -> tuple:
    """
    Handle command 'device list' ...
    """
    #logging.debug('cmdA ' + str(params))
    #x = params.get('x', '0')
    ret = Device.get_device_list()
    print(ret)
    return (None, ret)

###################################################################################################

def cmd_device_task_list(params, cmd, index) -> tuple:
    """
    Handle command 'device[] list' ...
    """
    #logging.debug('cmdA ' + str(params))
    #x = params.get('x', '0')
    ret = Device.get_device_task_list()
    print(ret)
    return (None, ret)

###################################################################################################

def cmd_device_info(params, cmd, index) -> tuple:
    """
    Handle command 'a' ...
    """
    ids = list(params.keys())
    if ids:
        id = ids[0]
        #Device.get
    #logging.debug('cmdA ' + str(params))
    x = params.get('x', '0')
    return (None, ids)

###################################################################################################

def cmd_ping(params, cmd, index) -> tuple:
    """
    Handle command 'ping' and returns string 'ping'
    """
    logging.debug('Ping')
    return (None, 'dpong' + str(list(params.keys())))

###################################################################################################
# Globals:

COMMANDS = [
    (r'device_list',                r'',                            cmd_device_list),
    (r'device\s*list',                r'',                            cmd_device_list),
    (r'device\[\] list',                r'',                            cmd_device_task_list),
    (r'device info',                r'[\s,]+(\w+)+',                            cmd_device_info),
    #(r'bbbbbbbbbbbb\w*[#-=]?(?P<index>\d+)',   r'[\s,]+(\w+(?::\w+)?)',        cmd_a),
    #(r'cccccccccccccc',                          r'',                            cmd_a),
    (r'dping',                       r'[\s,]+(\w+)+',                            cmd_ping),
    (r'd ping',                       r'[\s,]+(\w+)+',                            cmd_ping),
    ]

###################################################################################################
