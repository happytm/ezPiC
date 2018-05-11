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

@Cmd.route(r'xxx.#', 'a b c')
def cmd_xxx(cmd: dict) -> tuple:
    """
    Handle command 'xxx' ...
    """
    #logging.debug('cmdA ' + str(params))
    x = cmd.get('a', '0')
    return (None, None)

###################################################################################################

@Cmd.route(r'ping')
def cmd_ping(cmd: dict) -> tuple:
    """
    Handle command 'ping' and returns string 'pong'
    """
    logging.debug('Ping')
    return (None, 'pong')

###################################################################################################
