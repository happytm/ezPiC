"""
...TODO
"""
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