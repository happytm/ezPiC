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

def route(command: str, arg_keys: str=None):
    """ Adds a command handler function to the command list """
    def route_decorator(func):
        global COMMANDS

        #def function_wrapper(*args, **kwargs):
        #    print(re_command + ", " + func.__name__ + " returns:")
        #    return func(*args, **kwargs)
        #return function_wrapper

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
    global COMMANDS_C, COMMANDS

    plugins = Tool.load_plugins('cmds', 'cmd')
    #print(plugins)
    #for plugin in plugins:
    #    try:
    #        COMMANDS += plugin.COMMANDS
    #    except:
    #        pass

###################################################################################################

def run():
    pass

###################################################################################################

def excecute(cmd_str: str) -> tuple:
    """
    Excecutes a command and route to specified handler
    cmd: Command line with command and params as string
    return: Answer from excecuted command. Can be any object type or None
    """
    err = -1
    ret = 'Unknown command'

    for c in COMMANDS:
        if cmd_str.startswith(c['command']):   # command found
            cmd_params = {}

            cmd_arg = cmd_str.split(' ', 1)
            cmd = cmd_arg[0]
            cmd_params['CMD'] = cmd

            if c['has_index']:
                l = len(c['command'])
                cmd_params['IDX'] = int(cmd[l+1:])

            if c['args'] and len(cmd_arg)>1:
                args = cmd_arg[1].split()
                i = 0
                for key in c['args']:
                    if i<len(args):
                        value = args[i]
                        cmd_params[key] = value
                    else:
                        cmd_params[key] = None
                    i += 1
                
            fHandler = c['func']

            try:
                err, ret = fHandler(cmd=cmd_params)
            except Exception as e:
                err, ret =  (-9, 'Fail to call handler - ' + str(e))
            break   # stop scanning after first match

    return (err, ret)

###################################################################################################

