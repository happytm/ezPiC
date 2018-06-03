"""
Command Plugin for System Commands

"""
from com.modules import *

import dev.Cmd as Cmd

#######

@Cmd.route('login', 'name password')
def cmd_system_login(cmd:dict) -> tuple:
    """ Login to the system and change security level for actual connection """
    return (0, "NOT IMPLEMENTED")

#######

@Cmd.route('logout')
def cmd_system_logout(cmd:dict) -> tuple:
    """ Logout for actual connection """
    return (0, "NOT IMPLEMENTED")

#######
