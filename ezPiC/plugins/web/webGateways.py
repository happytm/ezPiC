"""
Web Plugin for Gateway-Pages
"""
from MicroWebSrv.microWebSrv import MicroWebSrv

import Tool
import Web

###################################################################################################

@MicroWebSrv.route('/gateways')
def web_gateways(httpClient, httpResponse):
    """ TODO """

    err, ret = Web.command('gateway.list')
    if err:
        Web.flash_error(httpResponse, err, ret)
        ret = []

    vars = {}
    vars['menu'] = 'gateways'
    vars['gateway_list'] = ret

    return httpResponse.WriteResponsePyHTMLFile('www/gateways.html', vars=vars)

###################################################################################################

@MicroWebSrv.route('/gateways/list/')
def web_gateways_list(httpClient, httpResponse):
    """ TODO """

    err, ret = Web.command('plugin.gateway.list')
    if err:
        Web.flash_error(httpResponse, err, ret)
        ret = []

    vars = {}
    vars['menu'] = 'gateways'
    vars['gateway_list'] = ret

    return httpResponse.WriteResponsePyHTMLFile('www/gateways_list.html', vars=vars)

###################################################################################################

@MicroWebSrv.route('/gateways/add/<guid>/')
def web_gateway_add(httpClient, httpResponse, args):
    """ TODO """
    guid = args['guid']

    params = {'guid': guid}
    err, ret = Web.command('gateway.add', items=params)
    if err:
        Web.flash_error(httpResponse, err, ret, guid)
    else:
        Web.command('save')
        msg = 'Gateway "{}" added'.format(guid)
        httpResponse.FlashMessage(msg, 'info')

    return httpResponse.WriteResponseRedirect('/gateways')

###################################################################################################

@MicroWebSrv.route('/gateways/edit/<idx>/')
@MicroWebSrv.route('/gateways/edit/<idx>/', 'POST')
def web_gateway_edit(httpClient, httpResponse, args):
    """ TODO """
    idx = int(args['idx'])

    err, ret = Web.command('gateway.getparam', index=idx)
    if err:
        Web.flash_error(httpResponse, err, ret, idx)
        return httpResponse.WriteResponseRedirect('/gateways')

    params = {}
    params['name'] = 'Test-Name'
    params.update(ret)

    if httpClient.GetRequestMethod() == 'POST':
        formParams = httpClient.ReadRequestPostedFormData()
        if formParams:
            for key, value in params.items():
                if key in formParams:
                    params[key] = formParams.get(key)
        err, ret = Web.command('gateway.setparam', index=idx, params=params)
        if err:
            Web.flash_error(httpResponse, err, ret, idx)
        err, ret = Web.command('save')
    else: # GET
        pass

    vars = {}
    vars['menu'] = 'gateways'
    #vars['name'] = 'TEST'
    vars['index'] = idx
    vars.update(params)

    err, html = Web.command('gateway.gethtml', index=idx)

    return httpResponse.WriteResponsePyHTMLFile(html, vars=vars)

###################################################################################################

@MicroWebSrv.route('/gateways/del/<idx>/')
def web_gateway_del(httpClient, httpResponse, args):
    """ TODO """
    idx = int(args['idx'])

    err, ret = Web.command('gateway.delete', index=idx)
    if err:
        Web.flash_error(httpResponse, err, ret, idx)
    else:
        err, ret = Web.command('save')
        msg = 'Gateway task deleted'
        httpResponse.FlashMessage(msg, 'info')

    return httpResponse.WriteResponseRedirect('/gateways')

###################################################################################################
