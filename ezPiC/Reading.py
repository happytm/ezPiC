"""
Measurements
"""
import os
import logging

try:
    from threading import RLock
except:
    from _thread import allocate_lock as RLock

#random = random.SystemRandom()

###################################################################################################
# Globals:

READINGS = {}
READINGS_NEW = {}
READINGLOCK = RLock()

###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    global READINGS, READINGS_NEW

###################################################################################################

def run():
    pass

###################################################################################################

def set(name: str, value):
    global READINGS, READINGS_NEW

    READINGS_NEW[name] = value
    READINGS[name] = value

###################################################################################################

def get(name: str=None):
    global READINGS

    if name:
        return READINGS.get(name, None)
    else:
        return READINGS

###################################################################################################

def get_new() -> dict:
    global READINGS_NEW

    return READINGS_NEW

###################################################################################################

def is_new() -> bool:
    global READINGS_NEW

    return len(READINGS_NEW) > 0

###################################################################################################

def set_handled():
    global READINGS, READINGS_NEW

    #READINGS.update(READINGS_NEW)
    READINGS_NEW = {}

###################################################################################################
###################################################################################################
###################################################################################################
