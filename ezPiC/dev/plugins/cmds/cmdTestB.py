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

import logging
import dev.Cmd as Cmd

###################################################################################################

@Cmd.route(r'b')
def cmd_b(cmd:dict) -> dict:
    """
    Handle command 'b' ...
    """
    logging.debug('cmdB ' + str(params))
    x = params.get('x', '0')
    return Cmd.ret(0, 'b')

###################################################################################################