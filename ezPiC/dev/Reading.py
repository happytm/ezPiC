"""
Measurements
"""
import os
import time

try:
    from threading import RLock
except:
    from _thread import allocate_lock as RLock

#random = random.SystemRandom()

###################################################################################################
# Globals:

READINGS = {}
READINGLOCK = RLock()
READINGACTTICK = 0

###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    pass

# =================================================================================================

def run():
    pass

###################################################################################################

def set(key:str, value, source:str=None) -> int:
    global READINGS, READINGACTTICK

    with READINGLOCK:
        READINGACTTICK += 1

        if key in READINGS:   #update
            r = READINGS[key]
            r['count'] += 1
        else:   #new entry
            r = {}
            r['count'] = 1
        r['tick'] = READINGACTTICK
        r['value'] = value
        r['source'] = source
        r['time'] = time.time()
        READINGS[key] = r

        return READINGACTTICK

# =================================================================================================

def get(key:str):
    global READINGS, READINGACTTICK

    with READINGLOCK:
        r = READINGS.get(key, None)
        if r:
            return r['value']

    return None

# =================================================================================================

def get_act_tick() -> int:
    global READINGS, READINGACTTICK

    return READINGACTTICK

# =================================================================================================

def is_new(tick:int) -> bool:
    global READINGS, READINGACTTICK

    return READINGACTTICK > tick

# =================================================================================================

def get_news(tick:int) -> dict:
    global READINGS, READINGACTTICK

    news = {}

    if tick < READINGACTTICK:
        with READINGLOCK:
            for key, r in READINGS.items():
                if r['tick'] > tick:
                    value = r['value']
                    news[key] = value

    return (READINGACTTICK, news)

###################################################################################################

def make_key(gadget:str, channel:str) -> str:
    return gadget + '.' + channel

###################################################################################################
