"""
...TODO
"""
import logging
#from MicroWebSrv.microWebTemplate import MicroWebTemplate
from MicroWebSrv.microWebSrv import MicroWebSrv
import json
import Tool
import G

import Cmd

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

def command(cmd_str:str, index:int=None, params:dict=None, source:str='?') -> tuple:
    """ TODO """
    request = {}
    request['CMD'] = cmd_str
    if index:
        request['IDX'] = index
    request['SRC'] = source
    if params:
        request.update(params)

    if True:
        answer = Cmd.excecute(request)
    else:
        request_json = json.dumps(request)
        answer_json = '{}'
        answer = json.loads(answer_json)

    #logging.debug('Starting web server')
    code = answer.get('CODE', 0)
    result = answer.get('RESULT', None)

    return (code, result)

###################################################################################################
