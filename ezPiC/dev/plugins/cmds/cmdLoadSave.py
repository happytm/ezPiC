"""
Command Plugin for Load and Save Parameters
"""
try:   # CPython
    import json
except:   # MicroPython
    import ujson as json

import dev.SysConfig as SysConfig
import dev.Gadget as Gadget
import dev.Gateway as Gateway
import dev.Cmd as Cmd
import G

CONFIG_FILE = 'config.json'

###################################################################################################

@Cmd.route('save')
def cmd_system_save(cmd:dict) -> dict:
    """ Saves all configuration and parameters of the plugins to a json-file """

    err = None

    with open(CONFIG_FILE, 'w') as outfile:
        try:
            save_dict = {}
            SysConfig.save(save_dict)
            Gadget.save(save_dict)
            Gateway.save(save_dict)
            # add other stuff like Gateway
            json.dump(save_dict, outfile, indent=2)
        except Exception as e:
            return Cmd.ret(-100, 'Error on collectin save values - ' + str(e))

    return Cmd.ret()

###################################################################################################

@Cmd.route('load')
def cmd_system_load(cmd:dict) -> dict:
    """ Loads all configuration and parameters of the plugins from a json-file """

    try:
        with open(CONFIG_FILE, 'r') as infile:
            config_all = json.load(infile)
            SysConfig.load(config_all)
            Gadget.load(config_all)
            Gateway.load(config_all)
            # ...
    except FileNotFoundError as e:
        pass
    except Exception as e:
            return Cmd.ret(-101, 'Error on collectin load values - ' + str(e))

    return Cmd.ret()

###################################################################################################
