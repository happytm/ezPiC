# Gadget-Commands

## Command "plugin.gadget.list"
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

---

## Command "gadget.list"
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

