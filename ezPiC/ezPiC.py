"""
...TODO
"""
__author__ = "Jochen Krapf"
__license__ = "CC-BY-SA"

from com.modules import *


if G.WEBSERVER:
    import web.Web as Web
if G.IOTDEVICE:
    import dev.Cmd as Cmd
    import dev.Timer as Timer
    import dev.Machine as Machine
    import dev.Gadget as Gadget
    import dev.Gateway as Gateway
    import dev.Rule as Rule
    import dev.SysConfig as SysConfig
    import dev.Reading as Reading
    import dev.CLI as CLI
    import dev.TelnetServer as TelnetServer

#######

def main():
    G.log(1, 'Lorem ipsum')
    G.log(1, 'Lorem {} ipsum', 'test')
    G.log(1, 'Lorem {} ipsum {}', 'test', 123)

    cmd_args = sys.argv
    G.log(1, cmd_args)

    """ Entry point for ezPiC """
    G.log(G.LOG_INFO, '# Starting main init #')
    if G.IOTDEVICE:
        Timer.init()
        Cmd.init()
        Machine.init()
        Gadget.init()
        Gateway.init()
        Rule.init()
        SysConfig.init()
        Reading.init()
        CLI.init()
        TelnetServer.init()
    if G.WEBSERVER:
        Web.init()

    G.log(G.LOG_INFO, '# Starting main run #')
    if G.IOTDEVICE:
        Timer.run()
        Cmd.run()
        Machine.run()
        Gadget.run()
        Gateway.run()
        Rule.run()
        SysConfig.run()
        Reading.run()
        CLI.run()

        Cmd.excecute('vs Lorem_ {"e": 2, "d": 756, "c": 234, "b": 12313, "a": 123}')
        Cmd.excecute('vs Lörém_ [0, 8, 15]')
        Cmd.excecute('vs Lorem {"e":2,"d":756,"c":234,"b":12313,"a":123}')
        Cmd.excecute('vs Lörém [0,8,15]')

        Cmd.excecute("load")

    if G.WEBSERVER:
        G.log(G.LOG_INFO, 'Starting web server')
        Web.run(threaded=G.IOTDEVICE)   # this call never comes back .. normally

    if G.IOTDEVICE:
        G.log(G.LOG_INFO, 'Starting telnet server')
        TelnetServer.run()   # this call never comes back .. normally

    G.log(G.LOG_ERROR, 'PANIC! Server terminated')
    G.RUN = False

#######

def __exit__():
    G.RUN = False
    G.log(1, '<<<<<<<<EXIT>>>>>>>>>')

#######

if G.MICROPYTHON:
    main()   # this call never comes back!
    G.RUN = False
else:    
    if __name__ == '__main__':
        main()   # this call never comes back!
        G.RUN = False

#######

