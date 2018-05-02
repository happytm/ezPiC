"""
...TODO
"""
import logging
from flask import Flask
from MicroWebSrv.microWebSrv import MicroWebSrv
import Tool
import G

app = Flask('ezPiC')
G.APP = app
mws = None

###################################################################################################

class Config(object):
    """ TODO """
    JOBS = [
        {
            'id': 'job1',
            'func': 'jobs:job1',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 1
        }
    ]

    SCHEDULER_API_ENABLED = False

###################################################################################################

def job1(a, b):
    print(str(a) + ' ' + str(b))

###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    global app, mws

    www = Tool.load_plugins('web', 'web')
    #print(www)

    mws = MicroWebSrv(webPath='www/') # TCP port 80 and files in /flash/www
    #mws = MicroWebSrv(webPath='MicroWebSrv/www/') # TCP port 80 and files in /flash/www
    G.MWS = mws


    #app.logger.debug('Starting flask')
    #app.logger.warning('A warning occurred (%d apples)', 42)
    #app.logger.error('An error occurred')

    #scheduler = APScheduler()
    #scheduler.init_app(app)
    #scheduler.start()

###################################################################################################

def run():
    """ TODO """
    global app, mws

    logging.debug('Starting web server')

    mws.Start(threaded=False)         # Starts server in a new thread

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
