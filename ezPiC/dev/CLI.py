"""
Command Line Interface for Configuration the IoT-Device
"""
from com.modules import *

import com.Tool as Tool
import dev.Cmd as Cmd

#######
# Globals:

LOGO = '''\r\n\
                       _|_|_|    _|     _|_|_|\r\n\
    _|_|    _|_|_|_|   _|    _|       _|\r\n\
  _|    _|        _|   _|    _|  _|   _|\r\n\
  _|_|_|_|      _|     _|_|_|    _|   _|\r\n\
  _|          _|       _|        _|   _|\r\n\
    _|_|_|  _|_|_|_|   _|        _|     _|_|_|\r\n\
 \r\n\
 ezPiC IoT-Device - github.com/fablab-wue/ezPiC\r\n\r\n'''

#######

def process_cli():
    print(LOGO)
    while G.RUN:
        print('> ', end='')
        cmd_str = input()
        if not cmd_str:
            continue
        err, ret = Cmd.excecute(cmd_str, 'CLI')
        if err:
            print( 'ERROR {}: {}'.format(err, ret) )
        elif ret:
            try:
                print(json.dumps(ret, indent=2))
            except:
                print(ret)
        print()

#######

def init():
    """ Prepare module vars and load plugins """
    pass

# =====

def run():
    Tool.start_thread(process_cli, ())
 
#######
