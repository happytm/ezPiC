"""
...TODO
"""
import re
#import logging
import Tool

###################################################################################################
# Globals:

COMMANDS = []
COMMANDS_C = []

###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    global COMMANDS_C, COMMANDS

    plugins = Tool.load_plugins('cmds', 'cmd')
    #print(plugins)
    for plugin in plugins:
        try:
            COMMANDS += plugin.COMMANDS
        except:
            pass

    # precompile all regex for plugin-commands
    for reCmd, rePar, fHandler in COMMANDS:
        reCmdC = re.compile(reCmd, re.IGNORECASE)
        if rePar:
            reParC = re.compile(rePar, re.IGNORECASE)
        else:
            reParC = None
        COMMANDS_C.append((reCmdC, reParC, fHandler))

###################################################################################################

def run():
    pass

###################################################################################################

def excecute(cmd: str):
    """
    Excecutes a command and route to specified handler
    cmd: Command line with command and params as string
    return: Answer from excecuted command. Can be any object type or None
    """
    ret = 'Unknown command'

    for reCmdC, reParC, fHandler in COMMANDS_C:
        m = reCmdC.match(cmd)
        if m:   # command found
            params = {}
            index = None

            print(m)
            print(m.groups())

            if m.groups():
                if m.group('index'):
                    index = int(m.group('index'))

            if reParC:
                paramList = reParC.findall(cmd)
                if paramList:   # params found and valid
                    print(paramList)
                    #print()
                    for param in paramList:
                        keyvalue = param.split(sep=':', maxsplit=1)
                        if len(keyvalue) > 1:
                            params[keyvalue[0]] = keyvalue[1]
                        else:
                            params[keyvalue[0]] = None
                else:
                    pass   # invalid params

            try:
                ret = fHandler(params=params, cmd=cmd, index=index)
            except Exception as e:
                ret = 'Fail to call handler - ' + e
            break   # stop scanning after first match
    return ret


#p = re.compile(r'(?P<cmd>^"[^"]*"|\S*) *(?P<prm>.*)?')
#r = re.compile(r'(?P<key>[^\s]+[\s\w]*)(?:[\s]*:[\s]*)(?P<value>\b[^,:]+\b)')
#print(r)
