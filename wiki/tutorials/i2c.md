# I2C


| Board | SCL | SDA | Reset | en3V3 |
|-|-|-|-|-|
| WeMos LoLin32 +OLED | 4 | 5 | 
| ESP32 +LoRa +OLED | 15 | 4 | 16
| FabLab ESP32-ST BOB | 22 | 21 || 0

```Python
import machine
scl=machine.Pin(4, machine.Pin.PULL_UP)
sda=machine.Pin(5, machine.Pin.PULL_UP)
i2c = machine.I2C(scl=scl, sda=sda, freq=400000)
i2c.scan()

# On ESP32 +LoRa +OLED
import machine
res=machine.Pin(16, machine.Pin.OUT)
res.value(1)
scl=machine.Pin(15, machine.Pin.PULL_UP)
sda=machine.Pin(4, machine.Pin.PULL_UP)
i2c = machine.I2C(scl=scl, sda=sda, freq=400000)
i2c.scan()
--> [60]   =0x3C


import machine
p3v3=machine.Pin(0, machine.Pin.OUT)
scl=machine.Pin(22, machine.Pin.PULL_UP)
sda=machine.Pin(21, machine.Pin.PULL_UP)
i2c = machine.I2C(scl=scl, sda=sda, freq=400000)
i2c.scan()

import micropython
micropython.mem_info()
```