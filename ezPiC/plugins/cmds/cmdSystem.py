"""
...TODO
"""
import logging
import Device
import Cmd

###################################################################################################

@Cmd.route(r'info')
def cmd_system_info(params, cmd, index) -> tuple:
    """ Handle command 'info' """
    return (None, None)

###################################################################################################

@Cmd.route(r'version')
def cmd_system_version(params, cmd, index) -> tuple:
    """ Handle command 'version' """
    return (None, None)

###################################################################################################

@Cmd.route(r'about')
def cmd_system_about(params, cmd, index) -> tuple:
    """ Handle command 'about' """
    return (None, None)

###################################################################################################

@Cmd.route(r'login')
def cmd_system_login(params, cmd, index) -> tuple:
    """ Handle command 'login' """
    return (None, None)

###################################################################################################

@Cmd.route(r'logout')
def cmd_system_logout(params, cmd, index) -> tuple:
    """ Handle command 'logout' """
    return (None, None)

###################################################################################################

@Cmd.route(r'save')
def cmd_system_save(params, cmd, index) -> tuple:
    """ Handle command 'save' """
    return (None, None)

###################################################################################################

@Cmd.route(r'load')
def cmd_system_load(params, cmd, index) -> tuple:
    """ Handle command 'load' """
    return (None, None)

###################################################################################################

###################################################################################################
# Globals:

COMMANDS = []

###################################################################################################
