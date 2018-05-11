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

@Cmd.route('xxx.#', 'a b c')
def cmd_xxx(cmd: dict) -> dict:
    """
    Handle command 'xxx' ...
    """
    #logging.debug('cmdA ' + str(params))
    x = cmd.get('a', '0')

    return Cmd.ret()

###################################################################################################

@Cmd.route('ping')
def cmd_ping(cmd: dict) -> dict:
    """
    Handle command 'ping' and returns string 'pong'
    """
    logging.debug('Ping')

    return Cmd.ret('pong')

###################################################################################################
