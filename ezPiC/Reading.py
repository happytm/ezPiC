"""
Measurements
"""
import os
from threading import RLock
import logging

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

###################################################################################################

def get(name: str=None):
    global READINGS, READINGS_NEW

    if name:
        return READINGS.get(name, None)
    else:
        return READINGS

###################################################################################################

def get_new() -> dict:
    global READINGS, READINGS_NEW

    return READINGS_NEW

###################################################################################################

def update():
    global READINGS, READINGS_NEW

    READINGS.update(READINGS_NEW)
    READINGS_NEW = {}

###################################################################################################
###################################################################################################
###################################################################################################
