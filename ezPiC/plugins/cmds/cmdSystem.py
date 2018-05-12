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
import Device
import Cmd

CONFIG_FILE = 'config.json'

###################################################################################################

@Cmd.route('info')
def cmd_system_info(cmd: dict) -> dict:
    """ Handle command 'info' """
    return Cmd.ret()

###################################################################################################

@Cmd.route('version')
def cmd_system_version(cmd: dict) -> dict:
    """ Handle command 'version' """
    return Cmd.ret('0.0.?')

###################################################################################################

@Cmd.route('about')
def cmd_system_about(cmd: dict) -> dict:
    """ Handle command 'about' """
    return Cmd.ret('ezPiC by JK')

###################################################################################################

@Cmd.route('login', 'name password')
def cmd_system_login(cmd: dict) -> dict:
    """ Handle command 'login' """
    return Cmd.ret()

###################################################################################################

@Cmd.route('logout')
def cmd_system_logout(cmd: dict) -> dict:
    """ Handle command 'logout' """
    return Cmd.ret()

###################################################################################################

@Cmd.route('save')
def cmd_system_save(cmd: dict) -> dict:
    """ Handle command 'save' """

    err = None

    with open(CONFIG_FILE, 'w') as outfile:
        try:
            save_dict = {}
            Device.save(save_dict)
            # add other stuff like Gateway
            json.dump(save_dict, outfile, indent=2)
        except Exception as e:
            return Cmd.ret(None, -100, 'Error on collectin save values - ' + str(e))

    return Cmd.ret()

###################################################################################################

@Cmd.route('load')
def cmd_system_load(cmd: dict) -> dict:
    """ Handle command 'load' """

    try:
        with open(CONFIG_FILE, 'r') as infile:
            config_all = json.load(infile)
            Device.load(config_all)
            # Gateway(s?).load(...)
            # ...
    except FileNotFoundError as e:
        pass
    except Exception as e:
            return Cmd.ret(None, -101, 'Error on collectin load values - ' + str(e))

    return Cmd.ret()

###################################################################################################

@Cmd.route('commands')
def cmd_system_commands(cmd: dict) -> dict:
    """ Handle command 'commands' """

    cl = []

    for cmd in Cmd.COMMANDS:
        cmd_str = cmd['command']
        if cmd['has_index']:
            cmd_str += '.<idx>'
        args = cmd['args']
        if args:
            for key in args:
                cmd_str += ' <' + key + '>'
        cl.append(cmd_str)

    return Cmd.ret(cl)

###################################################################################################

###################################################################################################
