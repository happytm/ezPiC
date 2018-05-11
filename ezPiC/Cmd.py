"""
...TODO
"""
try:   # CPython
    import os
    import re
    import json
    import random
except:   # MicroPython
    import uos as os
    import ure as re
    import ujson as json
    import urandom as random

import logging
import Tool

###################################################################################################
# Globals:

COMMANDS = []

###################################################################################################
#Decorator

def route(command: str, arg_keys: str=None, security_level: int=0):
    """ Adds a command handler function to the command list """
    def route_decorator(func):
        global COMMANDS

        item = {}
        if command.endswith('.#'):
            item['command'] = command[:-2]
            item['has_index'] = True
        else:
            item['command'] = command
            item['has_index'] = False

        if arg_keys:
            item['args'] = arg_keys.split()
        else:
            item['args'] = None

        item['func'] = func

        COMMANDS.append(item)
        logging.debug(' - Added command "%s" with function "%s()"', command, func.__name__)
        return func
    return route_decorator

###################################################################################################
###################################################################################################
###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    global COMMANDS

    plugins = Tool.load_plugins('cmds', 'cmd')
    #print(plugins)

###################################################################################################

def run():
    pass

###################################################################################################

def excecute_line(cmd_str: str, source=None) -> tuple:
    """
    Excecutes a command and route to specified handler
    cmd: Command line with command and params as string
    return: Answer from excecuted command. Can be any object type or None
    """
    err = -900
    ret = 'Unknown command'

    try:
        for c in COMMANDS:
            if cmd_str.startswith(c['command']):   # command found
                cmd_params = {}

                cmd_arg = cmd_str.split(' ', 1)
                cmd = cmd_arg[0]
                cmd_params['CMD'] = cmd

                if c['has_index']:
                    l = len(c['command'])
                    index_str = cmd[l+1:]
                    if index_str:
                        cmd_params['IDX'] = int(index_str)
                    else:
                        err, ret =  (-903, 'Command needs index')
                        break   # stop scanning after first match

                if c['args'] and len(cmd_arg)>1:
                    arg_str = cmd_arg[1].strip()
                    #TODO check json
                    args = arg_str.split()
                    i = 0
                    for key in c['args']:
                        if i<len(args):
                            value = args[i]
                            cmd_params[key] = value
                        else:
                            cmd_params[key] = None
                        i += 1

                cmd_params['SRC'] = source
                    
                fHandler = c['func']

                try:
                    err, ret = fHandler(cmd=cmd_params)
                except Exception as e:
                    err, ret =  (-901, 'Fail to call handler - ' + str(e))
                break   # stop scanning after first match

    except Exception as e:
        err, ret =  (-902, 'Fail to interpret command - ' + str(e))

    return (err, ret)

###################################################################################################

def excecute_json(cmd_str: str, source=None) -> tuple:
    """
    Excecutes a command and route to specified handler
    cmd: Command line with command and params as string
    return: Answer from excecuted command. Can be any object type or None
    """
    cmd_params = {}
    err = -900
    ret = 'Unknown command'

    try:
        cmd_params = json.loads(cmd_str)

        command = cmd_params,get('CMD', None)
        if not command:
            err, ret =  (-911, 'JSON-Command has no item "CMD"')
            break
        
        for c in COMMANDS:
            if command == c['command']:   # command found

                if c['has_index']:
                    l = len(c['command'])
                    index_str = cmd[l+1:]
                    if cmd_params.get('IDX', None)
                        err, ret =  (-913, 'JSON-Command needs index')
                        break

                cmd_params['SRC'] = source
                    
                fHandler = c['func']

                try:
                    err, ret = fHandler(cmd=cmd_params)
                except Exception as e:
                    err, ret =  (-901, 'Fail to call handler - ' + str(e))
                break   # stop scanning after first match

    except Exception as e:
        err, ret =  (-902, 'Fail to interpret command - ' + str(e))

    return (err, ret)

###################################################################################################

def excecute(cmd_str: str, source=None) -> tuple:
    """
    Excecutes a command and route to specified handler
    cmd: Command line with command and params as string
    return: Answer from excecuted command. Can be any object type or None
    """
    cmd_str = cmd_str.strip()

    if cmd_str.beginswith('{') and cmd_str.endswith('}'):
        return excecute_json(cmd_str, source)
    else:
        return excecute_line(cmd_str, source)
