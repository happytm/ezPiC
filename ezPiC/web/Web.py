"""
...TODO
"""
#from MicroWebSrv.microWebTemplate import MicroWebTemplate
from .MicroWebSrv.microWebSrv import MicroWebSrv
import json
import Tool
import G

try:
    import dev.Cmd as Cmd
    DIRECT_CMD = True
except:
    DIRECT_CMD = False

MWS = None

###################################################################################################
# Globals:

PLUGINDIR = 'web/plugins/web'

###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    global MWS

    www = Tool.load_plugins(PLUGINDIR, 'web')
    #print(www)

    MWS = MicroWebSrv(webPath='web/www') # TCP port 80 and files in /flash/www
    #mws = MicroWebSrv(webPath='MicroWebSrv/www/') # TCP port 80 and files in /flash/www
    G.MWS = MWS


    #scheduler = APScheduler()
    #scheduler.init_app(app)
    #scheduler.start()

# =================================================================================================

def run(threaded=False):
    """ TODO """
    global MWS

    G.log(G.LOG_DEBUG, 'Starting web server')

    MWS.Start(threaded=threaded)         # Starts server in a new thread

###################################################################################################

def command(cmd_str:str, index:int=None, items:dict=None, params:dict=None) -> tuple:
    """ TODO """
    request = {}
    request['CMD'] = cmd_str
    if index is not None:
        request['IDX'] = index
    request['SRC'] = 'WEB'
    if params is not None:
        request['params'] = params
    if items is not None:
        request.update(items)

    if DIRECT_CMD:
        answer = Cmd.excecute(request) #JKJKJK TODO
    else:
        request_json = json.dumps(request)
        answer_json = '{}' #JKJKJK TODO
        answer = json.loads(answer_json)

    code = answer.get('CODE', 0)
    result = answer.get('RESULT', None)

    return (code, result)

###################################################################################################

def flash_error(httpResponse, err, ret, idx=None):
    if idx:
        msg = 'Error {0} [{2}] - {1}'.format(err, ret, idx)
    else:
        msg = 'Error {0} - {1}'.format(err, ret)

    httpResponse.FlashMessage(msg, 'danger')
