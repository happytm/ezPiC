"""
Command Plugin for System Commands

"""
from com.modules import *

import dev.Cmd as Cmd

#######

@Cmd.route('quit')
def cmd_quit(cmd:dict) -> tuple:
    """
    Handle command 'quit' TODO
    """
    G.log(G.LOG_ERROR, 'QUIT')
    G.RUN = False
    sys.exit(0)

    return (0, None)

#######

@Cmd.route('debug', 'level')
def cmd_debug(cmd:dict) -> tuple:
    """ TODO """
    level = int(cmd.get('level', None))
    G.LOGLEVEL = level

    return (0, None)

#######

