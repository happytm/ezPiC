"""
Command Plugin for Testing
"""
from com.modules import *

import com.G as G
import dev.Cmd as Cmd

#######

@Cmd.route('xxx.#', 'a b c')
def cmd_xxx(cmd:dict) -> tuple:
    """
    Handle command 'xxx' ...
    """
    x = cmd.get('a', '0')

    return (0, None)

#######

@Cmd.route(r'b')
def cmd_b(cmd:dict) -> tuple:
    """
    Handle command 'b' ...
    """
    G.log(G.LOG_DEBUG, 'cmdB ' + str(cmd))
    x = cmd.get('x', '0')
    return (0, 'b')

#######
