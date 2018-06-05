"""
Device
"""
from com.modules import *

#######
# Globals:

PARAMS = {}

#######

def set_default():
    global PARAMS

    PARAMS['name'] = 'ezPiC-Device'
    PARAMS['version'] = 1

#######

def init():
    """ Prepare module vars and load plugins """
    set_default()

# =====

def run():
    pass

#######

def load(config_all: dict):
    global PARAMS

    if not "Device" in config_all:
        return
    config = config_all.get("Device", {})
    if config:
        PARAMS = config
    else:
        set_default()

# =====

def save(append: dict = None):
    global PARAMS

    err = None
    ret = PARAMS

    if not append is None:
        append["Device"] = ret
        return (err, append)
    
    return (err, {"Device": ret})

#######

def set(key:str, value):
    global PARAMS

    PARAMS[key] = value

# =====

def get(key:str):
    global PARAMS

    return PARAMS.get(key, None)

# =====

def get_param(key:str=None) -> tuple:
    global PARAMS

    if key:
        return (0, PARAMS.get(key, None))
    else:
        return (0, PARAMS)

# =====

def set_param(params:dict) -> tuple:
    global PARAMS

    if params and type(params) is dict:
        PARAMS.update(params)

    return (0, None)

#######
