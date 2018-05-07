"""
...TODO
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
import Cmd

###################################################################################################

@Cmd.route(r'b\b')
def cmd_b(params, cmd, index) -> tuple:
    """
    Handle command 'b' ...
    """
    logging.debug('cmdB ' + str(params))
    x = params.get('x', '0')
    return (None, 'b')

###################################################################################################
