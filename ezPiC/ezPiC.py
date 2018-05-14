"""
...TODO
"""
import os
import logging
import G

if G.WEBSERVER:
    import web.Web as Web
if G.IOT:
    import dev.Cmd as Cmd
    import dev.Timer as Timer
    import dev.Device as Device
    import dev.Gateway as Gateway
    import dev.Rule as Rule
    import dev.Reading as Reading
    import dev.Scheduler as Scheduler
    import dev.TelnetServer as TelnetServer

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)-15s %(levelname).1s %(threadName).5s %(message)s',)

###################################################################################################

def main():
    """ Entry point for ezPiC """
    logging.debug('Starting main init')
    if G.IOT:
        Scheduler.init()
        Timer.init()
        Cmd.init()
        Device.init()
        Gateway.init()
        Rule.init()
        Reading.init()
        TelnetServer.init()
    if G.WEBSERVER:
        Web.init()

    logging.debug('Starting main run')
    if G.IOT:
        Scheduler.run()
        Timer.run()
        Cmd.run()
        Device.run()
        Gateway.run()
        Rule.run()
        Reading.run()

        Cmd.excecute("xxx 123 456 789")
        Cmd.excecute("xxx.99 123 456 789")
        x = Cmd.excecute("ping")

        Cmd.excecute("load")

    if G.WEBSERVER:
        logging.debug('Starting web server')
        Web.run(threaded=G.IOT)   # this call never comes back .. normally

    if G.IOT:
        logging.debug('Starting telnet server')
        TelnetServer.run()   # this call never comes back .. normally

    logging.error('PANIC! Server terminated')
    G.RUN = False

###################################################################################################

if __name__ == '__main__':
    main()   # this call never comes back!

###################################################################################################
