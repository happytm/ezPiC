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

def ret(result=None, code: int=0, error: str='') -> dict:
    params = {}

    params['RESULT'] = result
    params['CODE'] = code
    if error:
        params['ERROR'] = error

    return params

###################################################################################################

def _excecute_line(cmd_str: str, source=None) -> dict:
    """
    Excecutes a command and route to specified handler
    cmd: Command line with command and params as string
    return: Answer from excecuted command. Can be any object type or None
    """
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
                        return ret(None, -903, 'Command needs index')

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
                    return fHandler(cmd=cmd_params)
                except Exception as e:
                    return ret(None, -901, 'Exception in command handler - ' + str(e))

    except Exception as e:
        return ret(None, -902, 'Exception in command parser - ' + str(e))

    return ret(None, -900, 'Unknown command: ' + cmd_str)

###################################################################################################

def _excecute_json(cmd_str: str, source=None) -> dict:
    """
    Excecutes a command and route to specified handler
    cmd: Command line with command and params as string
    return: Answer from excecuted command. Can be any object type or None
    """
    cmd_params = {}

    try:
        cmd_params = json.loads(cmd_str)

        command = cmd_params,get('CMD', None)
        if not command:
            return ret(None, -911, 'JSON-Command has no item "CMD"')
        
        for c in COMMANDS:
            if command == c['command']:   # command found

                if c['has_index']:
                    l = len(c['command'])
                    index_str = cmd[l+1:]
                    if cmd_params.get('IDX', None):
                        return ret(None, -903, 'Command needs index')

                cmd_params['SRC'] = source
                    
                fHandler = c['func']

                try:
                    return fHandler(cmd=cmd_params)
                except Exception as e:
                    return ret(None, -901, 'Exception in command handler - ' + str(e))

    except Exception as e:
        return ret(None, -902, 'Exception in command parser - ' + str(e))

    return ret(None, -900, 'Unknown command: ' + cmd_str)

###################################################################################################

def excecute(cmd_str: str, source=None) -> dict:
    """
    Excecutes a command and route to specified handler
    cmd: Command line with command and params as string
    return: Answer from excecuted command. Can be any object type or None
    """
    cmd_str = cmd_str.strip()

    if cmd_str.startswith('{') and cmd_str.endswith('}'):
        return _excecute_json(cmd_str, source)
    else:
        return _excecute_line(cmd_str, source)
