# HybridPython

HybridPython is __NOT__ a new implementation of the language Python. It is the trial to write code which runs on CPython 3.4 (PC, RaspberryPi) __AND__ on Miropython 1.9.* (ESP32).

## Incompatible functions

|CPython|MicroPython|HybridPython|
|-|-|-|
|`module.__dict__.get(name)`|-|`getattr(module, name)`|
|`type(obj) is types.function`|-|`callable(obj)`|
|-|`socket.readline()`|`socket.makefile('rwb').readline()`|
|`json.dumps(str, indent=2)`|-|`json.dumps(str)` without indent|
|`os.listdir`|`os.ilistdir`|_if * else *_|
|`Bytearray-obj.decode()`|-|`bytes(Bytearray-obj).decode()`|
|`from threading import RLock`||`from _thread import allocate_lock as RLock`|
||||

## One Only Modules

### Only in CPython

|Module|
|-|
|types|
|datetime|
|telnetlib|

### Only in MicroPython

|Module|
|-|
|u*|
|machine|

Most base CPython modules like os, sys, json, ... has a pandon in Micropython with a 'u' in front of a name like uos, usys, ujson, ... . The Windows and Unix implementation of Micropython is strict and expects to use the 'u'-versions of the module names. The ESP8266 and ESP32 implementation is more friendly and have a fallback. They allows to import 'json' to get 'ujson'.


### Check Python Variant

```Python
try:   # try MicroPython
    import uos as os
    MICROPYTHON = True
except:   # CPython
    MICROPYTHON = False
```