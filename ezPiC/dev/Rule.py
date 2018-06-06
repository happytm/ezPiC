"""
...TODO
"""
from com.modules import *

import com.Tool as Tool
import dev.Timer as Timer

#######
# Globals:

PLUGINDIR = 'dev/plugins/rules'
RULEPLUGINS = {}
RULES = []
RULELOCK = RLock()
RULETIMER = 0

#######

def rule_timer_handler(news, args):
    global RULES, RULETIMER

    with RULELOCK:
        t = time.time()

        for idx, rule in enumerate(RULES):
            if rule.timer_next and (t >= rule.timer_next):
                if rule.get_param('enable'):
                    if rule.timer_period:   # cyclic timer
                        rule.timer_next += rule.timer_period
                        if rule.timer_next < t:   # missed some events
                            rule.timer_next = t + rule.timer_period
                    else:   # singel event
                        rule.timer_next = None
                    rule.timer()
                else:   # disabled
                    rule.timer_next = None

            if news:
                if rule.get_param('enable'):
                    rule.readings(news)

#######

def init():
    """ Prepare module vars and load plugins """
    global RULEPLUGINS

    plugins = Tool.load_plugins(PLUGINDIR, 'ru')
    for plugin in plugins:
        try:
            RULEPLUGINS[plugin.RUPID] = plugin
        except:
            pass

# =====

def run():
    """ TODO """
    global RULEPLUGINS, RULETIMER

    Timer.register_cyclic_handler(rule_timer_handler)

#######

def load(config_all: dict):
    if not "rules" in config_all:
        return
    for config in config_all["rules"]:
        rupid = config["RUPID"]
        loaded_version = config["version"]
        params = config["params"]
        err, idx = add(rupid, params)
        running_version = RULES[idx].version

        if not err and loaded_version != running_version:
            G.log(G.LOG_WARN, "task " +  rupid + " has change version form " + loaded_version + " to " + running_version)

# =====

def save(append: dict = None):
    err = None
    ret = []
    with RULELOCK:
        for rule in RULES:
            try:
                config = {}
                config["RUPID"] = rule.module.RUPID
                config["version"] = rule.version
                config["params"] = rule.get_param()
                ret.append(config)
            except Exception as e:
                err = -1
                ret = str(e)

    if not append is None:
        append["rules"] = ret
        return (err, append)
    
    return (err, {"rules": ret})

#######

def add(plugin_id: str, params: dict = None) -> tuple:
    """ TODO """
    err = None
    ret = None

    with RULELOCK:
        try:
            module = RULEPLUGINS.get(plugin_id, None)
            if module:
                rule = module.PluginRule(module)
                RULES.append(rule)
                ret = len(RULES) - 1
                if params:
                    rule.set_param(params)
                if rule.timer_period:
                    rule.timer_next = time.time() + rule.timer_period
                rule.init()
            else:
                err = 'Unknown RUPID'
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

# =====

def delete(idx: int) -> tuple:
    """ TODO """
    err = None
    ret = None

    with RULELOCK:
        try:
            rule = RULES[idx]
            rule.exit()
            del RULES[idx]
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

# =====

def clear() -> tuple:
    """ TODO """
    global RULES
    err = None
    ret = None

    with RULELOCK:
        for rule in RULES:
            try:
                rule.exit()
            except Exception as e:
                err = -1
                ret = str(e)
        RULES = []

    return (err, ret)

# =====

def get_plugin_list() -> tuple:
    """ TODO """
    pl = []
    err = None

    with RULELOCK:
        for rupid, module in RULEPLUGINS.items():
            p = {}
            p['RUPID'] = module.RUPID
            p['PNAME'] = module.PNAME
            p['PINFO'] = module.PINFO
            p['PFILE'] = module.__name__
            pl.append(p)

    return (err, pl)

# =====

def get_list() -> tuple:
    """ TODO """
    gl = []
    err = None

    with RULELOCK:
        for idx, rule in enumerate(RULES):
            g = {}
            g['idx'] = idx
            g['RUPID'] = rule.module.RUPID
            g['PNAME'] = rule.module.PNAME
            g['name'] = rule.get_name()
            g['enable'] = rule.get_param('enable')
            g['info'] = rule.get_info()
            gl.append(g)

    return (err, gl)

# =====

def get_param(idx: int, key: str=None) -> tuple:
    """ TODO """
    err = None
    ret = None

    with RULELOCK:
        try:
            rule = RULES[idx]
            ret = rule.get_param(key)
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

# =====

def set_param(idx: int, params: dict) -> tuple:
    """ TODO """
    err = None
    ret = None

    with RULELOCK:
        try:
            rule = RULES[idx]
            ret = rule.set_param(params)
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

# =====

def get_html(idx: int) -> tuple:
    """ TODO """
    err = None
    ret = 'None'

    with RULELOCK:
        try:
            rule = RULES[idx]
            ret = rule.get_html()
        except Exception as e:
            err = -1
            ret = str(e)

    return (err, ret)

#######

class PluginRuleBase():
    """ TODO """
    version = '1.0'

    def __init__(self, module):
        self.module = module
        self.param = {}
        self.timer_next = None
        self.timer_period = None

    def init(self):
        """ init a new instance after adding to task list or reinit an existing instance after loading/changing params """
        if not self.timer_next and self.timer_period and self.get_param('enable'):
            self.timer_next = time.time() + self.timer_period

    def exit(self):
        """ exit an existing instance after removing from task list """
        pass

    def get_name(self) -> str:
        """ get the name from the module """
        return self.param.get('name', 'Unknown')

    def get_info(self) -> str:
        """ get the description from the module """
        return str(self.param)

    def get_param(self, key:str=None):
        """ get the value for a given param key or get all key-value pairs as dict """
        if key:
            return self.param.get(key, None)
        else:
            return self.param

    def set_param(self, param_new:dict):
        """ updates the param key-value pairs with given dict """
        #self.param.update(param_new)
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

    def get_html(self) -> str:
        """ get the html template name from the module """
        return 'web/www/rules/{}.html'.format(self.module.RUPID)

    def cmd(self, cmd: str) -> str:
        return None

    def timer(self):
        pass

    def readings(self, news:dict):
        pass

#######
