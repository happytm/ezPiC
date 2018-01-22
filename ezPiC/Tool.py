"""
Common tools
"""
import os
import logging
import random
import re
import importlib

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
