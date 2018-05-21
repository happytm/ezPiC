"""
Web Plugin for Reading-Pages
"""
from web.MicroWebSrv.microWebSrv import MicroWebSrv

import Tool
import web.Web as Web

###################################################################################################

@MicroWebSrv.route('/readings')
def web_reading_list(httpClient, httpResponse):
    """ TODO """
    #idx = int(args['idx'])

    err, ret = Web.command('reading.full.list', index=0)
    if err:
        Web.flash_error(httpResponse, err, ret)
        ret = {}

    vars = {}
    vars['menu'] = 'tools'
    vars['reading_list'] = ret

    return httpResponse.WriteResponsePyHTMLFile('web/www/readings.html', vars=vars)

###################################################################################################
