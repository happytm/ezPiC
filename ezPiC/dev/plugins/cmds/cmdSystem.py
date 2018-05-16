"""
Command Plugin for System Commands

"""
try:   # CPython
    import os
    import sys
    import re
    import json
    import random
except:   # MicroPython
    import uos as os
    import usys as sys
    import ure as re
    import ujson as json
    import urandom as random

import logging
import dev.Cmd as Cmd
import dev.SysConfig as SysConfig

import G

###################################################################################################

@Cmd.route('info')
def cmd_system_info(cmd:dict) -> dict:
    """ Returns common information about the system and the environment """
    i = {}
    i['System'] = 'ezPiC'
    i['Version'] = G.VERSION
    i['Platform'] = sys.platform
    i['Python Version'] = sys.version
    i['Python Implementation'] = sys.implementation.name
    #i['Implementation'] = sys.implementation
    i['Source'] = cmd['SRC']

    return Cmd.ret(0, i)

###################################################################################################

@Cmd.route('version')
def cmd_system_version(cmd:dict) -> dict:
    """ Returns the version of ezPiC """
    return Cmd.ret(0, G.VERSION)

###################################################################################################

@Cmd.route('about')
def cmd_system_about(cmd:dict) -> dict:
    """ Returns about information """
    return Cmd.ret(0, 'ezPiC-Project by Jochen Krapf et al. - https://github.com/fablab-wue/ezPiC')

###################################################################################################

@Cmd.route('login', 'name password')
def cmd_system_login(cmd:dict) -> dict:
    """ Login to the system and change security level for actual connection """
    return Cmd.ret(0, "NOT IMPLEMENTED")

###################################################################################################

@Cmd.route('logout')
def cmd_system_logout(cmd:dict) -> dict:
    """ Logout for actual connection """
    return Cmd.ret(0, "NOT IMPLEMENTED")

###################################################################################################
###################################################################################################

@Cmd.route('commands')
def cmd_system_commands(cmd:dict) -> dict:
    """ Returns a list of all available commands with arguments """

    cl = []

    for cmd in Cmd.COMMANDS:
        cmd_str = cmd['command']
        if cmd['has_index']:
            cmd_str += '.<idx>'
        args = cmd['args']
        if args:
            for key in args:
                cmd_str += ' <' + key + '>'
        #func = cmd['func']
        #cmd_str += '   ' + func.__doc__
        cl.append(cmd_str)

    return Cmd.ret(0, cl)

###################################################################################################

@Cmd.route('system.getparam')
@Cmd.route('sysconfig.getparam')
def cmd_syscongig_getparam(cmd:dict) -> dict:
    """ Returns the system configutation """
    err, ret = SysConfig.get_param()

    return Cmd.ret(err, ret)

###################################################################################################

@Cmd.route('system.setparam', 'param')
@Cmd.route('sysconfig.setparam', 'param')
def cmd_syscongig_setparam(cmd:dict) -> dict:
    """ Sets the system configutation """
    params = cmd.get('params', None)
    err, ret = SysConfig.set_param(param)

    return Cmd.ret(err, ret)

###################################################################################################
