"""
Command Plugin for Testing
"""

import dev.Cmd as Cmd
import G

###################################################################################################

@Cmd.route('xxx.#', 'a b c')
def cmd_xxx(cmd:dict) -> dict:
    """
    Handle command 'xxx' ...
    """
    x = cmd.get('a', '0')

    return Cmd.ret()

###################################################################################################

@Cmd.route('ping')
def cmd_ping(cmd:dict) -> dict:
    """
    Handle command 'ping' and returns string 'pong'
    """
    G.log(G.LOG_DEBUG, 'Ping')

    return Cmd.ret(0, 'pong')

###################################################################################################
