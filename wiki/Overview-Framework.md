*>>> UNDER CONSTRUCTION <<<*

### Readings (Values, Measurements)

Readings are typically generated by gadgets but also rules and can be consumed by gateways and rules. Additionaly they can  displayed at GUI and logged in a file (data logger). 

A value entry is based on a key value (content) pair with additional meta data (time, change flag, source, decimal place, unit)

The key of the value is a string with separators. 
"\<gadget-name\>.\<channel\>"

The content can be any data type of Python, typically int, float, string or dict. A conversion to string is done at the end of the data flow (e.g. gateway, web page)

### CLI

...