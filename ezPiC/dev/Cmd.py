"""
...TODO
"""
try:   # CPython
    import json
except:   # MicroPython
    import ujson as json

import com.Tool as Tool
import com.G as G

#######
# Globals:

PLUGINDIR = 'dev/plugins/cmds'
COMMANDS = []

#######
#Decorator

def route(command: str, arg_keys: str=None, security_level: int=0):
    """ Adds a command handler function to the command list """
    def route_decorator(func):
        global COMMANDS

        item = {}
        if command.endswith('.#'):
            item['command'] = command[:-2]
            item['has_index'] = True
        else:
            item['command'] = command
            item['has_index'] = False

        if arg_keys:
            item['args'] = arg_keys.split()
        else:
            item['args'] = None

        item['func'] = func

        COMMANDS.append(item)
        G.log(G.LOG_DEBUG, ' - Added command "%s" with function "%s()"', command, func.__name__)
        return func

    return route_decorator

#######

def _split_ex(src_str:str) -> list:
    #return src_str.split(' ')
    ret = []
    line = src_str.strip()

    while line:
        c = line[0]
        if c == '"':
            parts = line[1:].split('"')
            ret.append(parts[0])
            if len(parts) <= 1:
                return ret
            line = parts[1].strip()
            continue

        if c == '{' or c == '[':
            try:
                json_obj = json.loads(line)
                ret.append(line)
                return ret
            except:
                pass
            i = 2
            while i < len(line):
                try:
                    json_obj = json.loads(line[:i])
                    ret.append(line[:i])
                    line = line[i:].strip()
                    continue
                except:
                    pass
                i += 1

        parts = line.split(' ', 1)
        ret.append(parts[0])
        if len(parts) <= 1:
            return ret
        line = parts[1]
        continue

    return ret

#######

def init():
    """ Prepare module vars and load plugins """
    global COMMANDS

    plugins = Tool.load_plugins(PLUGINDIR, 'cmd')
    #print(plugins)

# =====

def run():
    pass

#######

def _excecute_line(cmd_str: str, source=None) -> tuple:
    """
    Excecutes a command as str
    cmd: Command line with command and params as string
    return: Answer from excecuted command. Can be any object type or None
    """
    for c in COMMANDS:
        if cmd_str.startswith(c['command']):   # command found
            cmd_params = {}

            cmd_arg = cmd_str.split(' ', 1)
            cmd = cmd_arg[0]
            cmd_params['CMD'] = cmd

            if c['has_index']:
                l = len(c['command'])
                index_str = cmd[l+1:]
                if index_str:
                    cmd_params['IDX'] = int(index_str)
                else:
                    return (-903, 'Command needs index')

            if c['args'] and len(cmd_arg)>1:
                arg_str = cmd_arg[1].strip()
                #TODO check json
                args = _split_ex(arg_str)
                i = 0
                for key in c['args']:
                    if i<len(args):
                        value = args[i]
                        cmd_params[key] = value
                    else:
                        cmd_params[key] = None
                    i += 1

            cmd_params['SRC'] = source
                
            fHandler = c['func']

            try:
                return fHandler(cmd=cmd_params)
            except Exception as e:
                return (-901, 'Exception in command handler - ' + str(e))

    return (-900, 'Unknown command: ' + cmd_str)

# =====

def _excecute_json(cmd_dict: dict, source=None) -> tuple:
    """
    Excecutes a command as a dict
    cmd: Command dict with dict-items as params
    return: Answer from excecuted command. Can be any object type or None
    """
    cmd_params = cmd_dict

    cmd_str = cmd_params.get('CMD', None)
    if not cmd_str:
        return (-911, 'JSON-Command has no item "CMD"')
    
    for c in COMMANDS:
        if cmd_str == c['command']:   # command found

            if c['has_index']:
                index = cmd_params.get('IDX', None)
                if index is None:
                    return (-903, 'Command needs index')

            if source:
                cmd_params['SRC'] = source
                
            fHandler = c['func']

            try:
                return fHandler(cmd=cmd_params)
            except Exception as e:
                return (-901, 'Exception in command handler - ' + str(e))

    return (-900, 'Unknown command: ' + cmd_str)

# =====

def excecute(cmd, source=None) -> tuple:
    """
    Excecutes a command and route to specified handler
    cmd: Command as str or JSON-str or dict
    return: Answer from excecuted command. Can be any object type or None
    """
    try:
        if type(cmd) is str:
            cmd = cmd.strip()
            if cmd.startswith('{') and cmd.endswith('}'):
                cmd_dict = json.loads(cmd)
                return _excecute_json(cmd_dict, source)
            else:
                return _excecute_line(cmd, source)
        elif type(cmd) is dict:
            return _excecute_json(cmd, source)
        else:
            return (-909, 'Wrong type in command parser: ' + str(type(cmd)))
        
    except Exception as e:
        return (-902, 'Exception in command parser - ' + str(e))

    return (-999, 'Error')

#######
"""
import re
regex = re.compile(r'''
'.*?' | # single quoted substring
".*?" | # double quoted substring
\S+ # all the rest
''', re.VERBOSE)

print regex.findall('''
This is 'single "quoted" string'
followed by a "double 'quoted' string"
''')



[r for r in [(i%2 and ['"'+z+'"'] or [z.strip()])[0] for i,z in enumerate(x.split('"'))] if r] or [''] 
['sspam', '" ssthe life of brianss "', '42'] x = ' "" "" '
[r for r in [(i%2 and ['"'+z+'"'] or [z.strip()])[0] for i,z in enumerate(x.split('"'))] if r] or [''] 
['""', '""'] x='""'
[r for r in [(i%2 and ['"'+z+'"'] or [z.strip()])[0] for i,z in enumerate(x.split('"'))] if r] or [''] 
['""'] x=''
[r for r in [(i%2 and ['"'+z+'"'] or [z.strip()])[0] for i,z in enumerate(x.split('"'))] if r] or [''] 
['']
[(i%2 and ['"'+z+'"'] or [z.strip()])[0] for i,z in enumerate(x.split('"'))]
"""
