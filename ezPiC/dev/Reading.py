"""
Measurements
"""
import os
import logging
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

###################################################################################################

def run():
    pass

###################################################################################################

def set(key:str, value, source:str=None) -> int:
    global READINGS, READINGACTTICK

    with READINGLOCK:
        READINGACTTICK += 1

        r = READINGS.get(key, {})
        r['tick'] = READINGACTTICK
        r['value'] = value
        r['source'] = source
        r['time'] = time.time()
        r['count'] = r.get('count', 0) + 1
        READINGS[key] = r

        return READINGACTTICK

###################################################################################################

def get(key:str):
    global READINGS, READINGACTTICK

    with READINGLOCK:
        r = READINGS.get(key, None)
        if r:
            return r['value']

    return None

###################################################################################################

def get_act_tick() -> int:
    global READINGS, READINGACTTICK

    return READINGACTTICK

###################################################################################################

def is_new(tick:int) -> bool:
    global READINGS, READINGACTTICK

    return READINGACTTICK > tick

###################################################################################################

def get_new_list(tick:int) -> tuple:
    global READINGS, READINGACTTICK

    l = []

    if tick < READINGACTTICK:
        with READINGLOCK:
            for key, r in READINGS.items():
                if r['tick'] > tick:
                    value = r['value']
                    l.append((key, value))

    return (READINGACTTICK, l)

###################################################################################################

def make_key(unit:str, device:str, channel:str) -> str:
    return unit + '.' + device + '.' + channel

###################################################################################################
###################################################################################################
###################################################################################################
