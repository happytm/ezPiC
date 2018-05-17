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

import Tool
import G

###################################################################################################
# Globals:

PLUGINDIR = 'dev/plugins/cmds'
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
        G.log(G.LOG_DEBUG, ' - Added command "%s" with function "%s()"', command, func.__name__)
        return func
    return route_decorator

###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    global COMMANDS

    plugins = Tool.load_plugins(PLUGINDIR, 'cmd')
    #print(plugins)


def run():
    pass

###################################################################################################

def ret(code: int=0, result=None) -> dict:
    params = {}
    params['CODE'] = code
    params['RESULT'] = result

    return params

###################################################################################################

def _excecute_line(cmd_str: str, source=None) -> dict:
    """
    Excecutes a command as str
    cmd: Command line with command and params as string
    return: Answer from excecuted command. Can be any object type or None
    """
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
                    return ret(-903, 'Command needs index')

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
                return ret(-901, 'Exception in command handler - ' + str(e))

    return ret(-900, 'Unknown command: ' + cmd_str)

# =================================================================================================

def _excecute_json(cmd_dict: dict, source=None) -> dict:
    """
    Excecutes a command as a dict
    cmd: Command dict with dict-items as params
    return: Answer from excecuted command. Can be any object type or None
    """
    cmd_params = cmd_dict

    cmd_str = cmd_params.get('CMD', None)
    if not cmd_str:
        return ret(-911, 'JSON-Command has no item "CMD"')
    
    for c in COMMANDS:
        if cmd_str == c['command']:   # command found

            if c['has_index']:
                index = cmd_params.get('IDX', None)
                if index is None:
                    return ret(-903, 'Command needs index')

            if source:
                cmd_params['SRC'] = source
                
            fHandler = c['func']

            try:
                return fHandler(cmd=cmd_params)
            except Exception as e:
                return ret(-901, 'Exception in command handler - ' + str(e))

    return ret(-900, 'Unknown command: ' + cmd_str)

# =================================================================================================

def excecute(cmd, source=None) -> dict:
    """
    Excecutes a command and route to specified handler
    cmd: Command as str or JSON-str or dict
    return: Answer from excecuted command. Can be any object type or None
    """
    try:
        if type(cmd) is str:
            cmd = cmd.strip()
            if cmd.startswith('{') and cmd.endswith('}'):
                cmd_dict = json.loads(cmd)
                return _excecute_json(cmd_dict, source)
            else:
                return _excecute_line(cmd, source)
        elif type(cmd) is dict:
            return _excecute_json(cmd, source)
        else:
            return ret(-909, 'Wrong type in command parser: ' + str(type(cmd)))
        
    except Exception as e:
        return ret(-902, 'Exception in command parser - ' + str(e))

