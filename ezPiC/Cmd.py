"""
...TODO
"""
import re
import logging
import Tool

###################################################################################################
# Globals:

COMMANDS = []
COMMANDS_C = []

###################################################################################################
#Decorator

def route(re_command):
    """ Adds a command handler function to the command list """
    def route_decorator(func):
        global COMMANDS

        #def function_wrapper(*args, **kwargs):
        #    print(re_command + ", " + func.__name__ + " returns:")
        #    return func(*args, **kwargs)
        #return function_wrapper

        item = (re_command, func)
        COMMANDS.append(item)
        logging.debug(' - Added command "%s" with function "%s()"', re_command, func.__name__)
        return func
    return route_decorator

###################################################################################################
###################################################################################################
###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    global COMMANDS_C, COMMANDS

    plugins = Tool.load_plugins('cmds', 'cmd')
    #print(plugins)
    #for plugin in plugins:
    #    try:
    #        COMMANDS += plugin.COMMANDS
    #    except:
    #        pass

    # precompile all regex for plugin-commands
    for reCmd, fHandler in COMMANDS:
        reCmdC = re.compile(reCmd)
        COMMANDS_C.append((reCmdC, fHandler))

###################################################################################################

def run():
    pass

###################################################################################################

def excecute(cmd: str) -> tuple:
    """
    Excecutes a command and route to specified handler
    cmd: Command line with command and params as string
    return: Answer from excecuted command. Can be any object type or None
    """
    err = -1
    ret = 'Unknown command'

    for reCmdC, fHandler in COMMANDS_C:
        m = reCmdC.match(cmd)
        if m:   # command found
            params = {}
            index = None

            if m.groups():
                print(m.groups())
                print(m.groupdict())
                for key, value in m.groupdict().items():
                    if key == 'index' or key == 'idx':
                        index = int(value)
                    elif key == 'params':
                        p = Tool.str_to_params(value)
                        params.update(p)
                    else:
                        params[key] = value

            #if reParC:
            #    paramList = reParC.findall(cmd)
            #    if paramList:   # params found and valid
            #        #print(paramList)
            #        #print()
            #        for param in paramList:
            #            keyvalue = param.split(sep=':', maxsplit=1)
            #            if len(keyvalue) > 1:
            #                params[keyvalue[0]] = keyvalue[1]
            #            else:
            #                params[keyvalue[0]] = None
            #    else:
            #        pass   # invalid params

            try:
                err, ret = fHandler(params=params, cmd=cmd, index=index)
            except Exception as e:
                err, ret =  (-9, 'Fail to call handler - ' + e)
            break   # stop scanning after first match
    return (err, ret)

###################################################################################################

