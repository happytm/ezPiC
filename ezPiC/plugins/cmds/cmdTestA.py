"""
...TODO
"""
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
# Globals:

COMMANDS = [
    (r'bbbbb\w*[#-=]?(?P<index>\d+)',   r'[\s,]+(\w+(?::\w+)?)',        cmd_a),
    #(r'bbbbb',                          r'',                            cmd_a),
    (r'ccccc',                          r'',                            cmd_a),
    #(r'ping',                       r'',                            cmd_ping),
    ]

###################################################################################################
