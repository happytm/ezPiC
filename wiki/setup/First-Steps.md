# First Steps

## Install on RaspberryPi

### Start a terminal

### Get the source code from GitHub repositors

```
> git clone https://github.com/falab-wue/ezPiC
```

A directory `ezPiC` is created

### Set actual user privilages for socket access

```
> sudo touch /etc/authbind/byport/80
> sudo chmod 777 /etc/authbind/byport/80
```

### Start program

```
> cd ezPiC
ezPiC> python3 ezPiC.py
```
