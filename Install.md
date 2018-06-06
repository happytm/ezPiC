
### Windows

Open program "cmd"

Install or update python tools for programming

```
pip3 install esptool
pip3 install ampy
```

Download Micropython firmware for ESP32 boards from `http://micropython.org/download`. Version 1.9.4 (or higher) is required

Open program "Device Manager" to check which com-port is used for the connected ESP32

Flash firmware to ESP32:

```
esptool --chip esp32 --port <PORT> erase_flash
esptool --chip esp32 --port <PORT> write_flash -z 0x1000 <FIRMWARE.BIN>
```

<PORT> is the com-port of the USB-serial interface like "COM10"
<FIRMWARE.BIN> is the filename of the downloaded binary file like "esp32-20180606-v1.9.4-119-gaace60a7.bin"

Download ezPiC source

Change path to where the ezPiC.py file is like `cd /where/it/is/ezPiC/ezPiC`

Note: If you started ezPiC locally with Python3 (for test...) cache folders with name `__pycache__` are created. They have to be removed first.

Put project files to ESP32:
```
ampy --port <PORT> put com
ampy --port <PORT> put dev
ampy --port <PORT> put esp
ampy --port <PORT> put ezPiC.py

ampy --port <PORT> put web

ampy --port <PORT> put ezPiC.cnf
ampy --port <PORT> reset
```

Note: Transfer can take several minutes


