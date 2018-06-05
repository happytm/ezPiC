*>>> UNDER CONSTRUCTION <<<*

Goal:
* Like ESPEasy a web configurable IoT device
* Usage of IoT devices by hobbyists without progrmming expirence
* Adding plugins with low/mid level Python knowlage
* Append plugins by community (GitHub)
* Open source

Platform:
* RaspberryPi, \*Pi (initially planned)
* PC (for development and debugging)
* ESP32
* PyBoard ?
* ~~ESP8266~~ too less memory :-(
* Other platforms running MicroPython with 100 kByte free RAM (`gc.mem_free()`)

Programming Lanuage:
* Hybrid-Python to fit all platforms:
    * CPython 3.4.x  (or higher) for Raspberry Pi and PC
    * MicroPython 1.9.4 (or higher) for ESP32 and PyBoard

User GUI:
* Web server front end on the platform based on the project [MicroWebSrc](https://github.com/jczic/MicroWebSrv) which is already in Hybrid-Python

User CLI:
* All funcionalitys are accessable by a command line interface via HTTP GET request, web page (HTML form), Telnet, ...

Plugin system:
* Easiely extend by anyone
* Unloadable plugins (import fails) are dismissed and don't affect other plugins
* If nessecary intall with reduced plugin count

* Gadget-plugins:
  * Interface to hardware sensors and actuators
  * Deliver readings/measurements (e.g. temperature, switch on/off, ...) to active gateway-plugins, rules, web interface, ...
  * Each gadget has its own partial web page form for configuration
  * A gadget plugin can be instanciated multiple times (e.g. many temperature sensors of same type)

* Gateway-plugins:
  * Interface to external servers and brokers
  * Consume readings/measurements (e.g. temperature, switch on/off, ...) and deliver them to the configured server (e.g. MQTT, HTTP, Socket, InfluxDB, ...)
  * Can also support hardware access to transmission modules (e.g. LoRaWan, Philips Hue, ...)
  * Each gateway has its own partial web page form for configuration
  * A gateway can be instanciated multiple times

* Command-plugins:
  * Extend cli with additional commands

* rule-plugins:
  * Add rules to react on new measurements and call cli commands or set the values of other reading
  * Each rule has its own partial web page form for configuration

* web-plugins:
  * Extend web front end with additional pages

Front-end-Languages:
* Initial: English
* Later: localisation
