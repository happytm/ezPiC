"""
...TODO
"""
from com.Globals import *

import com.Tool as Tool
import dev.Reading as Reading

#######
# Globals:

THREAD = None

CYCLICTIMEHANDLER = []

#######

def thread_timer_loop():
    """ TODO """
    global CYCLICTIMEHANDLER

    _reading_tick = 0

    while RUN:
        if Reading.is_new(_reading_tick):
            _reading_tick, _news = Reading.get_news(_reading_tick)
        else:
            _news = {}

        for func, args in CYCLICTIMEHANDLER:
            try:
                func(_news, args)
            except:
                pass

        time.sleep(0.100)

#######

def init():
    """ Prepare module vars and load plugins """
    pass

# =====

def run():
    """ TODO """
    global THREAD

    log(LOG_DEBUG, 'Starting timer thread')
    if not THREAD:
        THREAD = Tool.start_thread(thread_timer_loop)

#######

def register_cyclic_handler(func, args=()):
    """ Adds a function to the list of handlers """

    CYCLICTIMEHANDLER.append((func, args))

#######
