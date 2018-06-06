"""
Measurements
"""
from com.Globals import *

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
            r['unit'] = None
            r['format'] = None

        r['tick'] = READINGACTTICK
        r['value'] = value
        r['source'] = source
        r['time'] = time.time()
        READINGS[key] = r

        return READINGACTTICK

# =====

def set_meta(key:str, unitstr:str=None, formatstr:str=None) -> int:
    global READINGS, READINGACTTICK

    with READINGLOCK:
        if key in READINGS:   #update
            r = READINGS[key]
        else:   #new entry
            r = {}
            r['count'] = 0
            r['tick'] = 0
            r['value'] = None
            r['source'] = None
            r['time'] = time.time()
            r['unit'] = None
            r['format'] = None

        if unitstr:
            r['unit'] = unitstr
        if formatstr:
            r['format'] = formatstr
        READINGS[key] = r

        return READINGACTTICK

# =====

def _get(key:str):
    global READINGS

    r = READINGS.get(key, None)
    if not r:
        return None
    
    return r['value']

# =====

def get(key:str):
    global READINGACTTICK

    with READINGLOCK:
        return _get(key)

# =====

def _get_str(key:str) -> str:
    global READINGS

    r = READINGS.get(key, None)
    if not r:
        return ''
    
    value = r['value']

    if r['format']:
        try:
            value = r['format'].format(value)
        except:
            value = str(value)
    else:
        value = str(value)

    if r['unit']:
        value += ' [' + str(r['unit']) + ']'
        
    return value

# =====

def get_str(key:str) -> str:
    global READINGACTTICK

    with READINGLOCK:
        return _get_str(key)

# =====

def get_act_tick() -> int:
    global READINGACTTICK

    return READINGACTTICK

# =====

def is_new(tick:int) -> bool:
    global READINGACTTICK

    return READINGACTTICK > tick

# =====

def get_news(tick:int) -> tuple:
    global READINGS, READINGACTTICK

    news = {}

    if tick < READINGACTTICK:
        with READINGLOCK:
            for key, r in READINGS.items():
                if r['tick'] > tick:
                    news[key] = _get_str(key)

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
        """ init a new instance - TODO """
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
