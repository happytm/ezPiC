"""
...TODO
"""
import os
import logging
import G
import Web
import Cmd
import Device
import Gateway
import Rule
import Reading
import Scheduler

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)-15s %(levelname).1s %(threadName).5s %(message)s',)

###################################################################################################

def main():
    """ Entry point for ezPiC """
    logging.debug('Starting main init')
    Scheduler.init()
    Cmd.init()
    Device.init()
    Gateway.init()
    Rule.init()
    Reading.init()
    Web.init()

    logging.debug('Starting main run')
    Scheduler.run()
    Cmd.run()
    Device.run()
    Gateway.run()
    Rule.run()
    Reading.run()

    Cmd.excecute("xxx 123 456 789")

    Cmd.excecute("load")

    Web.run()   # this call never comes back .. normally

    logging.error('PANIC! Web server terminated')
    G.RUN = False

###################################################################################################

if __name__ == '__main__':
    main()   # this call never comes back!

###################################################################################################
