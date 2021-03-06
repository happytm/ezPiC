"""
Command Line Interface for Configuration the IoT-Device
"""
from com.Globals import *

import com.Tool as Tool
import dev.Cmd as Cmd

#######
# Globals:

#######

def process_cli():
    time.sleep(0.75)
    print(Tool.LOGO)
    while RUN:
        cmd_str = input(':-> ')
        if not cmd_str:
            continue
        err, ret = Cmd.excecute(cmd_str, 'CLI')
        #print (err)  #JK DEBUG
        #print (ret)  #JK DEBUG
        if err is not None and err != 0:
            print( 'ERROR {}: {}'.format(err, ret) )
        elif ret:
            print(Tool.json_str(ret))
        print()

#######

def init():
    """ Prepare module vars and load plugins """
    pass

# =====

def run():
    Tool.start_thread(process_cli, ())
 
#######
