"""
Commen Module to be loaded in all project modules
"""
try:   # try MicroPython
    import uos as os
    MICROPYTHON = True
except:   # CPython
    MICROPYTHON = False

if MICROPYTHON:
    import ujson as json
    from _thread import allocate_lock as RLock
else:   # CPython
    import os
    import json
    from threading import RLock

import sys
import time

import com.G as G

