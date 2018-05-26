# What is MQTT

... see Wikipedia

# MQTT Data Flow by Examples

![Logo](MQTT.svg)

Based on this image the following examples can show typical data flows

## Example: 1 Publisher, no Subscriber

* Client X connected

If Client X publishes any data with Topic 1 and nobody is listening (nobody has subscribed Topic 1) the data is lost.

(Exception: see Topics with Retain Flag)

## Example: 1 Publisher, 1 Subscriber

* Client A connected
* Client B connected and subscribes Topic 2

If Client A publishes any data with Topic 2 and Client B is notified instantly about change of Topic 2.

## TODO
