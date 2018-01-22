"""
...TODO
"""
import logging
from flask import Flask
#from flask_apscheduler import APScheduler
import Tool
import G

app = Flask('ezPiC')
G.APP = app

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
    global app

    # Load default config and override config from an environment variable
    app.config.update(dict(
        #DATABASE=os.path.join(app.root_path, 'flaskr.db'),
        SECRET_KEY=Tool.get_secret_key(),
        DEBUG=False,
        USERNAME='admin',
        PASSWORD='12345',
        SERVER_NAME='localhost',
        ))
    app.config.from_object(Config())
    app.config.from_pyfile('ezPiC.cfg', silent=True)
    app.config.from_envvar('EZPIC_SETTINGS', silent=True)

    www = Tool.load_plugins('web', 'web')
    #print(www)

    #app.logger.debug('Starting flask')
    #app.logger.warning('A warning occurred (%d apples)', 42)
    #app.logger.error('An error occurred')

    #scheduler = APScheduler()
    #scheduler.init_app(app)
    #scheduler.start()

###################################################################################################

def run():
    """ TODO """
    global app

    logging.debug('Starting web server')
    app.run(
        use_debugger=True,
        debug=app.debug,
        use_reloader=False,
        host='localhost',
        port=80,
        threaded=True
        )
    #app.run(threaded=True)

###################################################################################################
