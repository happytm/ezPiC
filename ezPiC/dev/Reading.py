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

#######
# Globals:

READINGS = {}
READINGLOCK = RLock()
READINGACTTICK = 0

#######

def init():
    """ Prepare module vars and load plugins """
    pass

# =====

def run():
    pass

#######

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

# =====

def get(key:str):
    global READINGS, READINGACTTICK

    with READINGLOCK:
        r = READINGS.get(key, None)
        if r:
            return r['value']

    return None

# =====

def get_act_tick() -> int:
    global READINGS, READINGACTTICK

    return READINGACTTICK

# =====

def is_new(tick:int) -> bool:
    global READINGS, READINGACTTICK

    return READINGACTTICK > tick

# =====

def get_news(tick:int) -> tuple:
    global READINGS, READINGACTTICK

    news = {}

    if tick < READINGACTTICK:
        with READINGLOCK:
            for key, r in READINGS.items():
                if r['tick'] > tick:
                    value = r['value']
                    news[key] = value

    return (READINGACTTICK, news)

#######

def get_news_full(tick:int) -> tuple:
    global READINGS, READINGACTTICK

    news = {}

    if tick < READINGACTTICK:
        with READINGLOCK:
            for key, r in READINGS.items():
                if r['tick'] > tick:
                    news[key] = r

    return (READINGACTTICK, news)

#######

def make_key(gadget:str, channel:str) -> str:
    return gadget + '.' + channel

#######

class Filter():
    """ TODO """
    __all__ = ['init', 'fits', 'get_info']

    class FilterTag():
        """ TODO """
        MODE_EXACT = 0
        MODE_START_WITH = 1
        MODE_END_WITH = 2
        MODE_CONTAINS = 3
        def __init__(self, key:str, mode:int):
            self.key = key
            self.mode = mode

    version = '1.0'


    def __init__(self):
        self.tags = []
        pass

    def init(self, filter_pattern_str:str):
        """ init a new instance ... TODO """
        self.tags = []

        if not filter_pattern_str:
            return
        
        patterns = filter_pattern_str.split()
        for pattern in patterns:
            mode = self.FilterTag.MODE_EXACT
            if pattern.endswith('*'):
                mode = self.FilterTag.MODE_START_WITH
                pattern = pattern[:-1]
            if pattern.startswith('*'):
                if mode == self.FilterTag.MODE_START_WITH:
                    mode = self.FilterTag.MODE_CONTAINS
                else:
                    mode = self.FilterTag.MODE_END_WITH
                pattern = pattern[1:]

            tag = self.FilterTag(pattern, mode)
            self.tags.append(tag)  
        pass

    def fits(self, key:str) -> bool:
        """ TODO """
        if not self.tags:   # empty list -> fits all!
            return True

        for tag in self.tags:
            if tag.mode == self.FilterTag.MODE_EXACT:
                if tag.key == key:
                    return True
            elif tag.mode == self.FilterTag.MODE_START_WITH:
                if key.startswith(tag.key):
                    return True
            elif tag.mode == self.FilterTag.MODE_END_WITH:
                if key.endswith(tag.key):
                    return True
            elif tag.mode == self.FilterTag.MODE_CONTAINS:
                if key.find(tag.key) >= 0:
                    return True
        return False

    def get_info(self) -> str:
        """ get the description from the module """
        return ''

#######
