## What is MQTT

... see Wikipedia

## MQTT Data Flow by Examples

![Logo](https://github.com/fablab-wue/ezPiC/blob/master/doc/MQTT.svg)

Based on this image the following examples can show typical data flows

### Example: 1 Publisher, no Subscriber

* Client X connected

If Client X publishes any data with Topic 1 and nobody is listening (nobody has subscribed Topic 1) the data is lost.

(Exception: see Topics with Retain Flag)

TODO
