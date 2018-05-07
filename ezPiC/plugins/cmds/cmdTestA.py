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

@Cmd.route(r'aaaaa')
def cmd_a(params, cmd, index) -> tuple:
    """
    Handle command 'a' ...
    """
    logging.debug('cmdA ' + str(params))
    x = params.get('x', '0')
    return (None, None)

###################################################################################################

@Cmd.route(r'ping')
def cmd_ping(params, cmd, index) -> tuple:
    """
    Handle command 'ping' and returns string 'pong'
    """
    logging.debug('Ping')
    return (None, 'pong')

###################################################################################################
