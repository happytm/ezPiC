"""
...TODO
"""
import logging
from flask import Flask
from MicroWebSrv.microWebSrv import MicroWebTemplate
from MicroWebSrv.microWebSrv import MicroWebSrv
import Tool
import G

app = Flask('ezPiC')
G.APP = app
MWS = None

###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    global app, MWS

    www = Tool.load_plugins('web', 'web')
    #print(www)

    MWS = MicroWebSrv(webPath='www/') # TCP port 80 and files in /flash/www
    #mws = MicroWebSrv(webPath='MicroWebSrv/www/') # TCP port 80 and files in /flash/www
    G.MWS = MWS


    #scheduler = APScheduler()
    #scheduler.init_app(app)
    #scheduler.start()

###################################################################################################

def run():
    """ TODO """
    global app, MWS

    logging.debug('Starting web server')

    MWS.Start(threaded=False)         # Starts server in a new thread

    #app.run(
    #    use_debugger=True,
    #    debug=app.debug,
    #    use_reloader=False,
    #    host='localhost',
    #    port=8080,
    #    threaded=True
    #    )
    #app.run(threaded=True)

###################################################################################################
