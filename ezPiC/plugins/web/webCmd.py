"""
...TODO
"""
from MicroWebSrv.microWebSrv import MicroWebSrv
import logging, time
import html
import Tool
import Cmd
import json

###################################################################################################

@MicroWebSrv.route('/cmd')
@MicroWebSrv.route('/cmd', 'POST')
def web_cmd(httpClient, httpResponse):
    """ TODO """
    cmd = ''
    err = ''
    ret = ''

    if httpClient.GetRequestMethod() == 'POST':
        formParams = httpClient.ReadRequestPostedFormData()
        if formParams and 'cmd' in formParams:
            cmd = formParams.get('cmd')
    else: # GET
        formParams  = httpClient.GetRequestQueryParams()
        if formParams and 'cmd' in formParams:
            cmd = formParams.get('cmd')

    #cmd = html.escape(cmd)

    if cmd:
        #print(cmd)
        err, ret = Cmd.excecute(cmd)
        try:
            ret = json.dumps(ret, indent=2)
        except:
            pass
        ret = str(ret)
        #ret = html.escape(ret)
        t = 'Cmd ' + cmd + ' -> ' + str(ret)
        logging.debug(t)

    vars = {}
    vars['menu'] = 'tools'
    vars['cmd'] = cmd
    vars['err'] = err
    vars['ret'] = ret

    return httpResponse.WriteResponsePyHTMLFile('www/cmd.html', headers=None, vars=vars)

###################################################################################################
