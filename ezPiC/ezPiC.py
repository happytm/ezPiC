#!/usr/bin/env python3
"""
ezPiC - IoT-Device
"""
__author__ = "Jochen Krapf"
__license__ = "CC-BY-SA"

from com.modules import *

# get program configuration
import com.Tool as Tool
Tool.load_cnf()
try:   # CPython only
    import com.Args
except Exception as e:
    pass
G.LOGLEVEL = G.CNF['logLevel']


# load module dependent on configuration
if G.CNF['useWeb']:
    import web.Web as Web
if G.CNF['useIoT']:
    import dev.Cmd as Cmd
    import dev.Timer as Timer
    import dev.Machine as Machine
    import dev.Gadget as Gadget
    import dev.Gateway as Gateway
    import dev.Rule as Rule
    import dev.Device as Device
    import dev.Reading as Reading
    if G.CNF['useCLI']:
        import dev.CLI as CLI
    if G.CNF['useTelnet']:
        import dev.TelnetServer as TelnetServer

#######

def main():
    """ Entry point for ezPiC """

    G.log(G.LOG_DEBUG, '# Starting main init')
    if G.CNF['useIoT']:
        Timer.init()
        Cmd.init()
        Machine.init()
        Gadget.init()
        Gateway.init()
        Rule.init()
        Device.init()
        Reading.init()
        if G.CNF['useCLI']:
            CLI.init()
        if G.CNF['useTelnet']:
            TelnetServer.init(port=G.CNF['portTelnet'])
    if G.CNF['useWeb']:
        Web.init(port=G.CNF['portWeb'])

    G.log(G.LOG_INFO, '# Starting main run')
    if G.CNF['useCLI']:
        Timer.run()
        Cmd.run()
        Machine.run()
        Gadget.run()
        Gateway.run()
        Rule.run()
        Device.run()
        Reading.run()
        if G.CNF['useCLI']:
            G.log(G.LOG_DEBUG, '# Starting CLI')
            CLI.run()

        # DEBUG
        Cmd.excecute('vs Lorem_ {"e": 2, "d": 756, "c": 234, "b": 12313, "a": 123}')
        Cmd.excecute('vs Lörém_ [0, 8, 15]')
        Cmd.excecute('vs Lorem {"e":2,"d":756,"c":234,"b":12313,"a":123}')
        Cmd.excecute('vs Lörém [0,8,15]')

        G.log(G.LOG_DEBUG, '# Load settings')
        Cmd.excecute("load")

    if G.CNF['useWeb']:
        G.log(G.LOG_DEBUG, '# Starting web server')
        Web.run(threaded=G.CNF['useIoT'])   # this call never comes back .. normally

    if G.CNF['useIoT']:
        G.log(G.LOG_DEBUG, '# Starting telnet server')
        if G.CNF['useTelnet']:
            TelnetServer.run()   # this call never comes back .. normally

    G.log(G.LOG_ERROR, 'PANIC! Server terminated')
    G.RUN = False

#######

def __exit__():
    G.RUN = False
    G.log(G.LOG_ERROR, '<<<<<<<<EXIT>>>>>>>>>')

#######

if G.MICROPYTHON:
    main()   # this call never comes back!
    G.RUN = False
else:    
    if __name__ == '__main__':
        main()   # this call never comes back!
        G.RUN = False

#######

