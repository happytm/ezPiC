"""
Common tools
"""
import os
import logging
import random
import re
import importlib
import ast

#random = random.SystemRandom()
PLUGINDIR = 'plugins'

###################################################################################################

def load_plugins(package: str, startswith: str='') -> list:
    """
    Imports all python modules from given path/package
    package: Relative path name
    startswith: (optional) Filter python files/modules with start string
    return: List of imported modules
    """
    global PLUGINDIR

    pysearchre = re.compile('.py$', re.IGNORECASE)
    pluginfiles = filter(pysearchre.search, os.listdir(os.path.join(os.path.dirname(__file__), PLUGINDIR, package)))
    form_module = lambda fp: '.' + os.path.splitext(fp)[0]
    plugins = map(form_module, pluginfiles)

    package = PLUGINDIR + '.' + package

    importlib.import_module(package) # import parent module / namespace

    modules = []
    for plugin in plugins:
        if not plugin.startswith('__'):
            if not startswith or plugin.startswith('.' + startswith):
                try:
                    module = importlib.import_module(plugin, package=package)
                    #module.ID
                    modules.append(module)
                    logging.info('Import plugin "{}{}"'.format(package, plugin))
                except Exception as e:
                    logging.error('Fail to import plugin "{}{}"\n{}'.format(package, plugin, e))

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

###################################################################################################

def get_secret_key():
    """
    Create a random secret key.

    Taken from the Django project.
    """
    #chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    #return get_random_string(50, chars)
    return get_random_string(24)

###################################################################################################

def make_random_password(length=12, symbols='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@$^_+&'):
    """ TODO """
    password = []
    for i in map(lambda x: int(len(symbols)*x/255.0), os.urandom(length)):
        password.append(symbols[i])
    return ''.join(password)

###################################################################################################

def params_to_str2(params:dict) -> str:
    """ TODO """
    ret = ''

    if params:
        for param, value in params.items():
            if ret:
                ret += ', '
            separators = (' ', ',')
            value = str(value)
            if any(s in value for s in separators):
                ret += '{}:"{}"'.format(param, value)
            else:
                ret += '{}:{}'.format(param, value)

    return ret

###################################################################################################

re_str_to_params = '(\w+)(?:\s*:\s*(\w+|"[^"]*"))?'
re_str_to_params_c = re.compile(re_str_to_params, re.IGNORECASE)

def str_to_params2(paramstr:str) -> dict:
    """ TODO """
    global re_str_to_params_c

    ret = {}

    keyvalueList = re_str_to_params_c.findall(paramstr)
    if keyvalueList:   # params found and valid
        #print(paramList)
        #print()
        for key, value in keyvalueList:
            if value and value[0] == '"' and value[-1] == '"':
                value = value[1:-1]
            if not value:
                value = None
            ret[key] = value
    else:
        pass   # invalid params

    return ret

###################################################################################################

def params_to_str(params:dict) -> str:
    """ TODO """
    return str(params)

###################################################################################################

def str_to_params(paramstr:str) -> dict:
    """ TODO """
    ret = {}

    if paramstr:
        paramstr = paramstr.strip()
        if paramstr[0] != '{':
            paramstr = '{' + paramstr
        if paramstr[-1] != '}':
            paramstr = paramstr + '}'
        try:
            ret = ast.literal_eval(paramstr)
        except Exception as e:
            pass

    return ret

###################################################################################################
###################################################################################################
