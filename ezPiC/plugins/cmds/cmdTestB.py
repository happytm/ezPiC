"""
...TODO
"""
import logging

###################################################################################################

def cmd_b(params, cmd, index) -> str:
    """
    Handle command 'b' ...
    """
    logging.debug('cmdB ' + str(params))
    x = params.get('x', '0')
    return None

###################################################################################################
# Globals:

COMMANDS = [
    (r'bbb',                          r'[\s,]+(\w+(?::\w+)?)',        cmd_b),
    (r'aaa',                          r'',                            cmd_b),
    (r'ccc',                          r'',                            cmd_b),
    ]

###################################################################################################
