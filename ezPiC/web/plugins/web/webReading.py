"""
Web Plugin for Reading-Pages
"""
from web.MicroWebSrv.microWebSrv import MicroWebSrv

import Tool
import web.Web as Web

###################################################################################################

@MicroWebSrv.route('/readings/<tick>')
@MicroWebSrv.route('/readings')
@MicroWebSrv.route('/readings', 'POST')
def web_reading_list(httpClient, httpResponse, args={}):
    """ TODO """
    key = ''
    value = ''
    act_tick = int(args.get('tick', 0))

    if httpClient.GetRequestMethod() == 'POST':
        formParams = httpClient.ReadRequestPostedFormData()
    else: # GET
        formParams  = httpClient.GetRequestQueryParams()

    if formParams and 'key' in formParams:
        key = formParams.get('key')
        value = formParams.get('value')
        reading = {}
        reading['key'] = key
        reading['value'] = value
        #reading['source'] = 'WEB-SET'
        err, ret = Web.command('reading.set', items=reading)
        if err:
            Web.flash_error(httpResponse, err, ret)

    err, ret = Web.command('reading.full.list', index=act_tick)
    if err:
        Web.flash_error(httpResponse, err, ret)
        ret = {}

    vars = {}
    vars['menu'] = 'tools'
    vars['reading_list'] = ret['readings']
    vars['last_tick'] = ret['tick']
    vars['act_tick'] = act_tick
    vars['add_key'] = key
    vars['add_value'] = value

    return httpResponse.WriteResponsePyHTMLFile('web/www/readings.html', vars=vars)

###################################################################################################