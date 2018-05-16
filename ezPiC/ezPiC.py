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
    import dev.Gadget as Gadget
    import dev.Gateway as Gateway
    import dev.Rule as Rule
    import dev.SysConfig as SysConfig
    import dev.Reading as Reading
    import dev.TelnetServer as TelnetServer

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)-15s %(levelname).1s %(threadName).5s %(message)s',)

###################################################################################################

def main():
    """ Entry point for ezPiC """
    logging.debug('Starting main init')
    if G.IOT:
        Timer.init()
        Cmd.init()
        Gadget.init()
        Gateway.init()
        Rule.init()
        SysConfig.init()
        Reading.init()
        TelnetServer.init()
    if G.WEBSERVER:
        Web.init()

    logging.debug('Starting main run')
    if G.IOT:
        Timer.run()
        Cmd.run()
        Gadget.run()
        Gateway.run()
        Rule.run()
        SysConfig.run()
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
