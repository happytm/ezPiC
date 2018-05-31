"""
Web Plugin for Reading-Pages
"""
from com.modules import *

from web.MicroWebSrv.microWebSrv import MicroWebSrv

import com.Tool as Tool
import web.Web as Web

#######

@MicroWebSrv.route('/readings/<tick>')
@MicroWebSrv.route('/readings')
@MicroWebSrv.route('/readings', 'POST')
def web_reading_list(httpClient, httpResponse, args=None):
    """ TODO """
    key = ''
    value = ''
    if args:
        act_tick = int(args.get('tick', 0))
    else:
        act_tick = 0

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

    err, ret = Web.command('reading.list', index=act_tick)
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

#######

@MicroWebSrv.route('/readingsfull/<tick>')
@MicroWebSrv.route('/readingsfull')
@MicroWebSrv.route('/readingsfull', 'POST')
def web_reading_full_list(httpClient, httpResponse, args=None):
    """ TODO """
    key = ''
    value = ''
    if args:
        act_tick = int(args.get('tick', 0))
    else:
        act_tick = 0

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

    return httpResponse.WriteResponsePyHTMLFile('web/www/readingsfull.html', vars=vars)

#######