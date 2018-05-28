# Overview

Commands are used to get information from the IoT-device and send configuration data to it.

Commands can be send via a JSON string or a "command line interface" (CLI) like string.

## Commands in JSON-Format

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
  'params': {"Lorem":1, "Ipsum":2}
}
```

## Commands as CLI

TODO

`reading.set <key> <value>`

Examples:

`reading.get pi`

`reading.set pi 3.14`

`reading.set mystr "Lorem Ipsum"}`

`reading.set mylist ["Lorem", "Ipsum", 0, 8, 15]`

`reading.set mydict {"Lorem":1, "Ipsum":2}`


## Command Return

Each command returns something - there is no silent command.

The return is always in JSON format.

Examples:

`[0, null]`   No error, no content

`[0, "Lorem Ipsum"]`   No error, str as payload

`[0, {"Lorem":1, "Ipsum":2}]`   No error, dict as payload

`[-900, "Unknown command"]`   Error with description


# Commands by Functions

* [Gadget](Gadget)
* [Gateway](Gateway)