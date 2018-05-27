"""
...TODO
"""

import time

try:
    from threading import RLock
except:
    from _thread import allocate_lock as RLock

import com.G as G
import com.Tool as Tool
import dev.Timer as Timer

#######
# Globals:

PLUGINDIR = 'dev/plugins/machines'
MACHINEPLUGINS = {}
MACHINES = []
MACHINELOCK = RLock()
MACHINETIMER = 0

#######

def init():
    """ Prepare module vars and load plugins """
    global MACHINEPLUGINS

    plugins = Tool.load_plugins(PLUGINDIR, 'ma')
    for plugin in plugins:
        try:
            MACHINEPLUGINS[plugin.MAPID] = plugin
        except:
            pass


    err = None
    ret = None

    for mapid, module in MACHINEPLUGINS.items():
        try:
            machine = module.PluginMachine(module)
            MACHINES.append(machine)
            machine.init()
        except Exception as e:
            err = -1
            ret = str(e)

# =====

def run():
    """ TODO """
    global MACHINEPLUGINS, MACHINETIMER


#######

def load(config_all: dict):
    if not "machines" in config_all:
        return
    for config in config_all["machines"]:
        #mapid = config["MAPID"]
        #loaded_version = config["version"]
        params = config["params"]
        set_param(params)

# =====

def save(append: dict = None):
    err = None
    ret = []
    with MACHINELOCK:
        for machine in MACHINES:
            try:
                config = {}
                config["MAPID"] = machine.module.MAPID
                config["version"] = machine.version
                config["params"] = machine.get_param()
                ret.append(config)
            except Exception as e:
                err = -1
                ret = str(e)

    if not append is None:
        append["machines"] = ret
        return (err, append)
    
    return (err, {"machines": ret})

#######

# =====

def get_plugin_list() -> tuple:
    """ TODO """
    pl = []
    err = None

    with MACHINELOCK:
        for mapid, module in MACHINEPLUGINS.items():
            p = {}
            p['MAPID'] = module.MAPID
            p['PNAME'] = module.PNAME
            p['PINFO'] = module.PINFO
            p['PFILE'] = module.__name__
            pl.append(p)

    return (err, pl)

# =====

def get_list() -> tuple:
    """ TODO """
    dl = []
    err = None

    with MACHINELOCK:
        for idx, machine in enumerate(MACHINES):
            d = {}
            d['idx'] = idx
            d['MAPID'] = machine.module.MAPID
            d['PNAME'] = machine.module.PNAME
            d['info'] = machine.get_info()
            dl.append(d)

    return (err, dl)

# =====

def get_param(key: str=None) -> tuple:
    """ TODO """
    err = None
    ret = {}

    with MACHINELOCK:
        try:
            for machine in MACHINES:
                ret1 = machine.get_param(key)
                ret.update(ret1)
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

# =====

def set_param(params: dict) -> tuple:
    """ TODO """
    err = None
    ret = None

    with MACHINELOCK:
        try:
            for machine in MACHINES:
                machine.set_param(params)
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

#######

class PluginMachineBase():
    """ TODO """
    version = '1.0'

    def __init__(self, module):
        self.module = module
        self.param = {}

    def init(self):
        """ init a new instance after adding to task list or reinit an existing instance after loading/changing params """
        pass

    def exit(self):
        """ exit an existing instance after removing from task list """
        pass

    def get_info(self) -> str:
        """ get the description from the module """
        return str(self.param)

    def get_param(self, key: str=None):
        """ get the value for a given param key or get all key-value pairs as dict """
        if key:
            return self.param.get(key, None)
        else:
            return self.param

    def set_param(self, param_new: dict):
        """ updates the param key-value pairs with given dict """
        changed = False
        for key in self.param:
            if self.param[key] != param_new.get(key, None):
                changed = True
                break

        if changed:
            self.exit()
            for key in self.param:
                self.param[key] = param_new.get(key, None)
            self.init()

#######
