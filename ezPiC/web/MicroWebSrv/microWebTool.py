from datetime import datetime
from time import localtime

def lorem(a=None):
    return 'ipsum' + str(a)

def ipsum():
    return 'dolor'

def noneStr(s):
    if s is None:
        return '-'
    else:
        return str(s)
    
def timeStr(t):
    #return datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
    y, m, d, hh, mm, ss, weekday, jday, dst = localtime(t)
    return "%04d-%02d-%02d %02d:%02d:%02d" % (y, m, d, hh, mm, ss)


def typeStr(o):
    type_str = str(type(o))
    try:
        parts = type_str.split("'")
        return parts[1]
    except:
        return type_str
