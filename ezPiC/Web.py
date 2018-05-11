"""
...TODO
"""
import logging
#from MicroWebSrv.microWebTemplate import MicroWebTemplate
from MicroWebSrv.microWebSrv import MicroWebSrv
import Tool
import G

MWS = None

###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    global MWS

    www = Tool.load_plugins('web', 'web')
    #print(www)

    MWS = MicroWebSrv(webPath='www/') # TCP port 80 and files in /flash/www
    #mws = MicroWebSrv(webPath='MicroWebSrv/www/') # TCP port 80 and files in /flash/www
    G.MWS = MWS


    #scheduler = APScheduler()
    #scheduler.init_app(app)
    #scheduler.start()

###################################################################################################

def run(threaded=False):
    """ TODO """
    global MWS

    logging.debug('Starting web server')

    MWS.Start(threaded=threaded)         # Starts server in a new thread

###################################################################################################
