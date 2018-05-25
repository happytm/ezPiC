Commands are used to get information from the IoT-device and send configuration data to it.

Commands can be send via a JSON string or a "command line interface" (CLI) like string.

JSON commands have the folloging elements:

| Key | Comment |
|-|-|
| CMD | Command |
| IDX | (optional) Index of an instance |
| SRC | (optional) Source of the request for autentification |
| params | (optional) Parameters to transport |
| xxx | (optional) Additional argument for the command |

Example:
```JSON
{
  'CMD': 'gadget.setparam',
  'SRC': '127.0.0.1:55555',
  'IDX': 1,
  'params': { 'Lorem':1, 'Ipsum':2 }
}
```
The return is always in JSON format


# Commands by Functions

* [Gadget](Gadget)
* [Gateway](Gateway)