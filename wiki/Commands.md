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
```
{
  'CMD': 'gadget.setparam',
  'SRC': '127.0.0.1:55555',
  'IDX': 1,
  'params': { 'Lorem':1, 'Ipsum':2 }
}
```
The return is always in JSON format


# Gadget-Commands

### Command "plugin.gadget.list"
Gets a list of all gadget plugins. Each element of the list contains a dict

#### JSON elements
| Key | Value | Comment |
|-|-|-|
| CMD | "plugin.gadget.list" | Command

#### CLI
`plugin.gadget.list` or `pdl`

#### Return
List of dicts:

| Key | Type | Comment |
|-|-|-|
| GGPID | str | Unique ID of the plugin module |
| PNAME | str | Name of the plugin module |
| PINFO | str | Info about the plugin |
| PFILE | str | Path and file name of the plugin module |


### Command "gadget.list"
Gets a list of all gadget instances. Each element of the list contains a dict

#### JSON elements
| Key | Value | Comment |
|-|-|-|
| CMD | "gadget.list" | Command

#### CLI
`gadget.list` or `dl`

#### Return
List of dicts:

| Key | Type | Comment |
|-|-|-|
| idx | int | Index of the instance |
| GGPID | str | Unique ID of the plugin module |
| PNAME | str | Name of the plugin module |
| name | str | Name of the instance (can be changed by user) |
| enable | bool | Is instance enabled |
| info | str | Info about the instance (plugin dependent) |


# Gateway-Commands

The Gateway-Commands use the same structure and types as the Gadget-Commands.
Simply replace:
* Gadget --> Gateway
* GGPID --> GWPID
