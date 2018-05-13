"""
Web Plugin for Command-Test-Page
"""
from web.MicroWebSrv.microWebSrv import MicroWebSrv
import logging, time
#import html
import Tool
import json
import web.Web as Web

###################################################################################################

@MicroWebSrv.route('/cmd')
@MicroWebSrv.route('/cmd', 'POST')
def web_cmd(httpClient, httpResponse):
    """ Shows a form to enter a command and display the result for testing the ezPiC-commands """
    cmd = ''
    err = ''
    ret = ''
    formParams = None

    if httpClient.GetRequestMethod() == 'POST':
        formParams = httpClient.ReadRequestPostedFormData()
    else: # GET
        formParams  = httpClient.GetRequestQueryParams()

    if formParams and 'cmd' in formParams:
        cmd = formParams.get('cmd')
        #cmd = html.escape(cmd)

    if cmd:
        err, ret = Web.command(cmd)
        try:
            ret = json.dumps(ret, indent=2)
        except:
            pass
        ret = str(ret)
        #ret = html.escape(ret)
        logging.debug('Cmd ' + cmd + ' -> ' + ret)

    vars = {}
    vars['menu'] = 'tools'
    vars['cmd'] = cmd
    vars['err'] = err
    vars['ret'] = ret

    return httpResponse.WriteResponsePyHTMLFile('web/www/cmd.html', vars=vars)

###################################################################################################
