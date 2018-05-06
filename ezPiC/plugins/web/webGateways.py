"""
...TODO
"""
from MicroWebSrv.microWebSrv import MicroWebSrv

import Tool
import Cmd

###################################################################################################

@MicroWebSrv.route('/gateways')
def web_gateways(httpClient, httpResponse):
    """ TODO """

    vars = {'error': None, 'message': None}
    vars['menu'] = 'gateways'

    err, ret = Cmd.excecute('gateway[] list')
    if err:
        ret = []

    vars['gateway_list'] = ret

    return httpResponse.WriteResponsePyHTMLFile('www/gateways.html', headers=None, vars=vars)

###################################################################################################

@MicroWebSrv.route('/gateways/list/')
def web_gateways_list(httpClient, httpResponse):
    """ TODO """

    vars = {'error': None, 'message': None}
    vars['menu'] = 'gateways'

    err, ret = Cmd.excecute('gateway list')
    if err:
        ret = []

    vars['gateway_list'] = ret

    return httpResponse.WriteResponsePyHTMLFile('www/gateways_list.html', headers=None, vars=vars)

###################################################################################################

@MicroWebSrv.route('/gateways/add/<duid>/')
def web_gateway_add(httpClient, httpResponse, args):
    """ TODO """
    duid = args['duid']

    vars = {'error': None, 'message': None}
    vars['menu'] = 'gateways'

    cmd = 'gateway[] add {}'.format(duid)
    err, idx = Cmd.excecute(cmd)
    if err:
        msg = 'Error "{0}" - Can not add gateway "{1}"'.format(err, duid)
        httpResponse.FlashMessage(msg, 'danger')
    else:
        Cmd.excecute('save')
        msg = 'Gateway "{}" added'.format(duid)
        httpResponse.FlashMessage(msg, 'info')

    return httpResponse.WriteResponseRedirect('/gateways')

###################################################################################################

@MicroWebSrv.route('/gateways/edit/<idx>/')
@MicroWebSrv.route('/gateways/edit/<idx>/', 'POST')
def web_gateway_edit(httpClient, httpResponse, args):
    """ TODO """
    idx = int(args['idx'])

    vars = {'error': None, 'message': None}

    cmd = 'gateway[{}] get'.format(idx)
    err, ret = Cmd.excecute(cmd)
    if err:
        vars['message'] = 'Error "{0}" - Can not get params from gateway [{1}]'.format(err, idx)
        return httpResponse.WriteResponseRedirect('/gateways')

    params = {}
    params['name'] = 'Test-Name'
    params.update(ret)

    cmd = ''
    err = ''
    ret = ''

    if httpClient.GetRequestMethod() == 'POST':
        formParams = httpClient.ReadRequestPostedFormData()
        if formParams:
            for key, value in params.items():
                if key in formParams:
                    params[key] = formParams.get(key)
        cmd = 'gateway[{}] set {}'.format(idx, Tool.params_to_str(params))
        err, ret = Cmd.excecute(cmd)
        err, ret = Cmd.excecute('save')
    else: # GET
        pass

    vars['menu'] = 'gateways'
    vars['name'] = 'TEST'
    vars['index'] = idx
    vars.update(params)

    cmd = 'gateway[{}] html'.format(idx)
    err, html = Cmd.excecute(cmd)

    return httpResponse.WriteResponsePyHTMLFile(html, headers=None, vars=vars)

###################################################################################################

@MicroWebSrv.route('/gateways/del/<idx>/')
def web_gateway_del(httpClient, httpResponse, args):
    """ TODO """
    idx = int(args['idx'])

    vars = {'error': None, 'message': None}

    cmd = 'gateway[{}] del'.format(idx)
    err, ret = Cmd.excecute(cmd)
    if err:
        msg = 'Error "{0}" - Can not delete gateway task [{1}]'.format(err, idx)
        httpResponse.FlashMessage(msg, 'danger')
        return httpResponse.WriteResponseRedirect('/gateways')
    else:
        err, ret = Cmd.excecute('save')
        msg = 'Gateway task deleted'
        httpResponse.FlashMessage(msg, 'info')

    return httpResponse.WriteResponseRedirect('/gateways')

###################################################################################################
