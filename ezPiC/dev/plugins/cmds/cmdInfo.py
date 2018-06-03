"""
Command Plugin for System Commands

"""
from com.modules import *

import dev.SysConfig as SysConfig
import dev.Cmd as Cmd

#######

@Cmd.route('info')
def cmd_system_info(cmd:dict) -> tuple:
    """ Returns common information about the system and the environment """
    i = {}
    i['software.name'] = 'ezPiC'
    i['software.version'] = G.VERSION
    i['command.source'] = cmd['SRC']

    try:
        i['sys.version'] = sys.version
        i['sys.platform'] = sys.platform
        i['sys.implementation.name'] = sys.implementation.name
        i['sys.maxsize'] = sys.maxsize
    except:
        pass

    try:
        import platform
        i['platform.node'] = platform.node()
        i['platform.system'] = platform.system()
        i['platform.release'] = platform.release()
        i['platform.version'] = platform.version()
        i['platform.machine'] = platform.machine()
        i['platform.processor'] = platform.processor()
        i['platform.python_version'] = platform.python_version()
    except:
        pass

    return (0, i)

#######
