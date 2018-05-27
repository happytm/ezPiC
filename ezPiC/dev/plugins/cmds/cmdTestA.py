"""
Command Plugin for Testing
"""

import dev.Cmd as Cmd
import com.G as G

#######

@Cmd.route('xxx.#', 'a b c')
def cmd_xxx(cmd:dict) -> tuple:
    """
    Handle command 'xxx' ...
    """
    x = cmd.get('a', '0')

    return (0, None)

#######

@Cmd.route('ping')
def cmd_ping(cmd:dict) -> tuple:
    """
    Handle command 'ping' and returns string 'pong'
    """
    G.log(G.LOG_DEBUG, 'Ping')

    return (0, 'pong')

#######
