"""
Common tools
"""
from com.modules import *

import gc
import time

#######

def load_plugins(path: str, pre :str=None) -> list:
    """
    Imports all python modules from given path inside the plugin folder
    path: Relative path name
    pre: (optional) Filter python files/modules with start string
    return: List of imported modules
    """
    gc.collect()

    try:
        full_path = os.path.join(os.path.dirname(__file__), '..', path)
    except:   # MicroPython has no os.path
        full_path = '../' + path
    G.log(G.LOG_INFO, 'Loading plugins from path "{}"'.format(full_path))

    modules = []

    try:
        files = os.listdir(full_path)
    except:   # Micropython on WIN32
        files = []
        for f in os.ilistdir(full_path):
            files.append(f[0])
    G.log(5, 'Plugin files: {}', files)

    module_prefix = path.replace('/', '.')

    gc.collect()

    for file in files:
        if file.startswith('__'):
            continue
        if not file.endswith('.py'):
            continue
        if pre and not file.startswith(pre):
            continue
        
        module_name = module_prefix + '.' + file[:-3]
        try:
            gc.collect()
            #G.log(G.LOG_DEBUG, 'MEM "{}"'.format(gc.mem_free()))
            module = __import__(module_name, globals(), locals(), ['object'], 0)
            gc.collect()
            modules.append(module)
            gc.collect()
            #G.log(G.LOG_DEBUG, 'MEM "{}"'.format(gc.mem_free()))
            G.log(G.LOG_INFO, 'Import plugin "{}"'.format(module_name))
        except Exception as e:
            gc.collect()
            #G.log(G.LOG_DEBUG, 'MEM "{}"'.format(gc.mem_free()))
            G.log(G.LOG_ERROR, 'Fail to import plugin "{}"\n{}'.format(module_name, e))

    gc.collect()
    return modules

#######

def params_to_str(params:dict) -> str:
    """ converts the param dict to a string """

    return json.dumps(params)

# =====

def str_to_params(paramstr:str) -> dict:
    """ converts the string to a param dict """

    return json.loads(paramstr)

#######

def start_thread(func, *args):
    gc.collect()

    #if G.MICROPYTHON:
    if True:
        from _thread import start_new_thread

        t = start_new_thread(func, ())
        return t
    else:
        from threading import Thread

        t = Thread(name=func.__name__, target=func, args=args)
        t.setDaemon(True)
        t.start()
        return t

#######

