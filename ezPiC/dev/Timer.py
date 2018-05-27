"""
...TODO
"""
import time

import Tool
import G
import dev.Reading as Reading

#####
# Globals:

THREAD = None

CYCLICTIMEHANDLER = []

#####

def thread_timer_loop():
    """ TODO """
    global CYCLICTIMEHANDLER

    _reading_tick = 0

    while G.RUN:
        if Reading.is_new(_reading_tick):
            _reading_tick, _news = Reading.get_news(_reading_tick)
            #G.log(G.LOG_INFO, 'News in thread_timer_loop: {}', _news)
        else:
            _news = {}

        for func, args in CYCLICTIMEHANDLER:
            try:
                func(_news, args)
            except:
                pass

        time.sleep(0.100)

#####

def init():
    """ Prepare module vars and load plugins """
    pass

# ===

def run():
    """ TODO """
    global THREAD

    G.log(G.LOG_DEBUG, 'Starting scheduler thread')
    if not THREAD:
        THREAD = Tool.start_thread(thread_timer_loop)

#####

def register_cyclic_hnadler(func, args=()):
    """ Adds a function to the list of handlers """

    CYCLICTIMEHANDLER.append((func, args))

#####
