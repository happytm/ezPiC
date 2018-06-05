"""
Commen Module to be loaded in all project modules
"""
try:   # try MicroPython
    import uos as os
    MICROPYTHON = True
except:   # CPython
    import os
    MICROPYTHON = False

if MICROPYTHON:
    try:
        import usys as sys
    except:
        import sys
    import ujson as json

    from _thread import allocate_lock as RLock

else:   # CPython
    import sys
    import json

    from threading import RLock
    from datetime import datetime

import time

import com.G as G

