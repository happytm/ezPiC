"""
Command Plugin for Reading handling
"""
try:   # CPython
    import json
except:   # MicroPython
    import ujson as json

import dev.Reading as Reading
import dev.Cmd as Cmd
import G

###################################################################################################

@Cmd.route('reading.full.list.#')
@Cmd.route('vfl.#')
def cmd_reading_task_list(cmd:dict) -> dict:
    """ Handle command 'reading[] list' """
    index = cmd['IDX']
    last_tick, d = Reading.get_news_full(index)

    return Cmd.ret(0, d)

###################################################################################################

###################################################################################################
