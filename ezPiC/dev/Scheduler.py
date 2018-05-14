"""
...TODO
"""
import logging
import sched, time
try:
    from threading import RLock
except:
    from _thread import allocate_lock as RLock

import Tool
import dev.Cmd as Cmd
import G

###################################################################################################
# Globals:

SCHED = None
THREAD = None

###################################################################################################

def __exit__():
    print('<<<<<<<<EXIT>>>>>>>>>')

###################################################################################################

def handler_idle():
    """ TODO """
    #t = str(time.clock()) + ' ' + str(time.time())
    logging.debug('idle')

###################################################################################################

def handler_cmd(cmd):
    """ TODO """
    ret = Cmd.excecute(cmd)
    t = 'Cmd ' + str(time.time()) + ' ' + cmd + ' -> ' + str(ret)
    logging.debug(t)

###################################################################################################

def thread_loop():
    """ TODO """
    global SCHED

    while G.RUN:
        SCHED.enter(1, 9, handler_idle)
        SCHED.run()

###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    global SCHED, THREAD

    if not SCHED:
        SCHED = sched.scheduler(time.time, time.sleep)

###################################################################################################

def run():
    """ TODO """
    global SCHED, THREAD

    logging.debug('Starting scheduler thread')
    if not THREAD:
        THREAD = Tool.start_thread(thread_loop)

    add_cmd(3, 'Hallo')

###################################################################################################

def add_event(t: float, handler, a=()):
    """ TODO """
    global SCHED, THREAD

    if t > 31536000:
        SCHED.enterabs(t, 5, handler, argument=a)
    else:
        SCHED.enter(t, 5, handler, argument=a)
    #SCHED.enter(5, 2, print_time, argument=('positional',))
    #SCHED.enter(5, 1, print_time, kwargs={'a': 'keyword'})

###################################################################################################

def add_cmd(t: float, cmd: str):
    """ TODO """
    global SCHED, THREAD

    SCHED.enter(t, 5, handler_cmd, argument=(cmd,))

###################################################################################################

TIMEHANDLER = []

def add_time_handler(time_handler):
    """ TODO """
    global TIMEHANDLER

    TIMEHANDLER.append(time_handler)

# =================================================================================================

def thread_handler_loop():
    """ TODO """
    global TIMEHANDLER

    while G.RUN:
        for th in TIMEHANDLER:
            try:
                th()
            except:
                pass
        time.sleep(0.100)

# =================================================================================================

###################################################################################################
###################################################################################################
###################################################################################################
