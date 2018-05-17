"""
Command Plugin for Testing
"""
try:   # CPython
    import os
    import re
    import json
    import random
except:   # MicroPython
    import uos as os
    import ure as re
    import ujson as json
    import urandom as random

import G
import dev.Cmd as Cmd

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
