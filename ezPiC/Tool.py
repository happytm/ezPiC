"""
Common tools
"""
try:   # CPython
    import os
    import json
except:   # MicroPython
    import uos as os
    import ujson as json

import gc

import G

###################################################################################################

def load_plugins(path: str, pre :str=None) -> list:
    """
    Imports all python modules from given path inside the plugin folder
    path: Relative path name
    pre: (optional) Filter python files/modules with start string
    return: List of imported modules
    """
    gc.collect()

    try:
        full_path = os.path.join(os.path.dirname(__file__), path)
    except:   # MicroPython has no os.path
        full_path = path
    G.log(G.LOG_INFO, 'Loading plugins from path "{}"'.format(full_path))

    modules = []

    try:
        files = os.listdir(full_path)
    except:   # Micropython on WIN32
        files = []
        for f in os.ilistdir(full_path):
            files.append(f[0])
    print(files)

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
            G.log(G.LOG_DEBUG, 'MEM "{}"'.format(gc.mem_free()))
            module = __import__(module_name, globals(), locals(), ['object'], 0)
            gc.collect()
            modules.append(module)
            gc.collect()
            G.log(G.LOG_DEBUG, 'MEM "{}"'.format(gc.mem_free()))
            G.log(G.LOG_INFO, 'Import plugin "{}"'.format(module_name))
        except Exception as e:
            gc.collect()
            G.log(G.LOG_DEBUG, 'MEM "{}"'.format(gc.mem_free()))
            G.log(G.LOG_ERROR, 'Fail to import plugin "{}"\n{}'.format(module_name, e))

    gc.collect()
    return modules

###################################################################################################

def get_random_string(length=12, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    """
    Returns a securely generated random string.

    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits.

    Taken from the django.utils.crypto module.
    """
    return ''.join(random.choice(allowed_chars) for i in range(length))

# =================================================================================================

def get_secret_key():
    """
    Create a random secret key.

    Taken from the Django project.
    """
    #chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    #return get_random_string(50, chars)
    return get_random_string(24)

# =================================================================================================

def make_random_password(length=12, symbols='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@$^_+&'):
    """ TODO """
    password = []
    for i in map(lambda x: int(len(symbols)*x/255.0), os.urandom(length)):
        password.append(symbols[i])
    return ''.join(password)

###################################################################################################

def params_to_str(params:dict) -> str:
    """ converts the param dict to a string """

    return json.dumps(params)

# =================================================================================================

def str_to_params(paramstr:str) -> dict:
    """ converts the string to a param dict """

    return json.loads(paramstr)

###################################################################################################

def start_thread(func, *args):
    gc.collect()

    try:
        from threading import Thread

        t = Thread(name=func.__name__, target=func, args=args)
        t.setDaemon(True)
        t.start()
        return t

    except:
        pass
        #from _thread import start_new_thread

        #t = start_new_thread(func, ())
        #return t

###################################################################################################