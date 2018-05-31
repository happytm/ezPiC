"""
Command Plugin for handling Readings
"""
from com.modules import *

import com.G as G
import dev.Reading as Reading
import dev.Cmd as Cmd

#######

@Cmd.route('reading.full.list.#')
@Cmd.route('vfl.#')
def cmd_reading_full_list(cmd:dict) -> tuple:
    """ Handle command 'reading[] list' """
    index = cmd['IDX']
    last_tick, readings = Reading.get_news_full(index)
    ret = {'tick':last_tick, 'readings':readings}

    return (0, ret)

#######

@Cmd.route('reading.list.#')
@Cmd.route('vl.#')
def cmd_reading_list(cmd:dict) -> tuple:
    """ Handle command 'reading[] list' """
    index = cmd['IDX']
    last_tick, readings = Reading.get_news(index)
    ret = {'tick':last_tick, 'readings':readings}

    return (0, ret)

#######

@Cmd.route('reading.set', 'key value source')
@Cmd.route('vs', 'key value source')
def cmd_reading_set(cmd:dict) -> tuple:
    """ Handle command 'reading[] list' """
    key = cmd.get('key', None)
    value = cmd.get('value', None)
    source = cmd.get('SRC', None)
    source = cmd.get('source', source)
    
    try:
        if type(value) is str:
            value = json.loads(value)
            #if value.isdigit():
            #    value = int(value)
            #elif value.replace('.','',1).isdigit():
            #    value = float(value)
            #elif value.startswith('{') and value.endswith('}'):
            #    value = json.loads(value)
    except:
        pass

    last_tick = Reading.set(key, value, source)
    
    return (0, last_tick)

#######

#######
