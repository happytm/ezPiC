"""
Command Plugin for System Commands

"""
from com.Globals import *

import dev.Cmd as Cmd

#######

@Cmd.route('quit')
def cmd_quit(cmd:dict) -> tuple:
    """ exit program """
    log(LOG_ERROR, 'QUIT')
    RUN = False
    sys.exit(0)

    return (0, None)

#######

@Cmd.route('loglevel', 'level')
def cmd_loglevel(cmd:dict) -> tuple:
    """ set logging level """
    level = int(cmd.get('level', None))
    LOG_LEVEL = level

    return (0, None)

#######

