"""
Command Plugin for System Commands

"""
from com.modules import *

import dev.SysConfig as SysConfig
import dev.Cmd as Cmd

#######

@Cmd.route('ping')
def cmd_ping(cmd:dict) -> tuple:
    """
    Handle command 'ping' and returns string 'pong'
    """
    G.log(G.LOG_DEBUG, 'Ping')

    return (0, 'pong')

#######

@Cmd.route('version')
def cmd_system_version(cmd:dict) -> tuple:
    """ Returns the version of ezPiC """
    return (0, G.VERSION)

#######

@Cmd.route('about')
def cmd_system_about(cmd:dict) -> tuple:
    """ Returns about information """
    return (0, 'ezPiC-Project by Jochen Krapf et al. - https://github.com/fablab-wue/ezPiC')

#######

@Cmd.route('commands')
def cmd_system_commands(cmd:dict) -> tuple:
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

    return (0, cl)

#######

@Cmd.route('system.getparam')
@Cmd.route('sysconfig.getparam')
def cmd_syscongig_getparam(cmd:dict) -> tuple:
    """ Returns the system configutation """
    err, ret = SysConfig.get_param()

    return (err, ret)

#######

@Cmd.route('system.setparam', 'param')
@Cmd.route('sysconfig.setparam', 'param')
def cmd_syscongig_setparam(cmd:dict) -> tuple:
    """ Sets the system configutation """
    params = cmd.get('params', None)
    err, ret = SysConfig.set_param(params)

    return (err, ret)

#######

