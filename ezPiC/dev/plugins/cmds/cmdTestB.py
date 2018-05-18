"""
Command Plugin for Testing
"""

import dev.Cmd as Cmd
import G

###################################################################################################

@Cmd.route(r'b')
def cmd_b(cmd:dict) -> dict:
    """
    Handle command 'b' ...
    """
    G.log(G.LOG_DEBUG, 'cmdB ' + str(cmd))
    x = cmd.get('x', '0')
    return Cmd.ret(0, 'b')

###################################################################################################
