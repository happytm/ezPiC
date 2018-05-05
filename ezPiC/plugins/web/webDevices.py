"""
...TODO
"""
from MicroWebSrv.microWebSrv import MicroWebSrv

import Tool
import Cmd

###################################################################################################

@MicroWebSrv.route('/devices')
def web_devices(httpClient, httpResponse):
    """ TODO """

    vars = {'error': None, 'message': None}
    vars['menu'] = 'devices'

    err, ret = Cmd.excecute('device[] list')
    if err:
        ret = []

    vars['device_list'] = ret

    return httpResponse.WriteResponsePyHTMLFile('www/devices.pyhtml', headers=None, vars=vars)

###################################################################################################

@MicroWebSrv.route('/devices/list/')
def web_devices_list(httpClient, httpResponse):
    """ TODO """

    vars = {'error': None, 'message': None}
    vars['menu'] = 'devices'

    err, ret = Cmd.excecute('device list')
    if err:
        ret = []

    vars['device_list'] = ret

    return httpResponse.WriteResponsePyHTMLFile('www/devices_list.pyhtml', headers=None, vars=vars)

###################################################################################################

@MicroWebSrv.route('/devices/add/<duid>/')
def web_device_add(httpClient, httpResponse, args):
    """ TODO """
    duid = args['duid']

    vars = {'error': None, 'message': None}
    vars['menu'] = 'devices'

    cmd = 'device[] add {}'.format(duid)
    err, idx = Cmd.excecute(cmd)
    if err:
        msg = 'Error "{0}" - Can not add device "{1}"'.format(err, duid)
        httpResponse.FlashMessage(msg, 'danger')
    else:
        Cmd.excecute('save')
        msg = 'Device "{}" added'.format(duid)
        httpResponse.FlashMessage(msg, 'info')

    return httpResponse.WriteResponseRedirect('/devices')

###################################################################################################

@MicroWebSrv.route('/devices/edit/<idx>/')
@MicroWebSrv.route('/devices/edit/<idx>/', 'POST')
def web_device_edit(httpClient, httpResponse, args):
    """ TODO """
    idx = int(args['idx'])

    vars = {'error': None, 'message': None}

    cmd = 'device[{}] get'.format(idx)
    err, ret = Cmd.excecute(cmd)
    if err:
        vars['message'] = 'Error "{0}" - Can not get params from device [{1}]'.format(err, idx)
        return httpResponse.WriteResponseRedirect('/devices')

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
        cmd = 'device[{}] set {}'.format(idx, Tool.params_to_str(params))
        err, ret = Cmd.excecute(cmd)
        err, ret = Cmd.excecute('save')
    else: # GET
        pass

    vars['menu'] = 'devices'
    vars['name'] = 'TEST'
    vars['index'] = idx
    vars.update(params)

    cmd = 'device[{}] html'.format(idx)
    err, html = Cmd.excecute(cmd)

    return httpResponse.WriteResponsePyHTMLFile(html, headers=None, vars=vars)

###################################################################################################

@MicroWebSrv.route('/devices/del/<idx>/')
def web_device_del(httpClient, httpResponse, args):
    """ TODO """
    idx = int(args['idx'])

    vars = {'error': None, 'message': None}

    cmd = 'device[{}] del'.format(idx)
    err, ret = Cmd.excecute(cmd)
    if err:
        msg = 'Error "{0}" - Can not delete device task [{1}]'.format(err, idx)
        httpResponse.FlashMessage(msg, 'danger')
        return httpResponse.WriteResponseRedirect('/devices')
    else:
        err, ret = Cmd.excecute('save')
        msg = 'Device task deleted'
        httpResponse.FlashMessage(msg, 'info')

    return httpResponse.WriteResponseRedirect('/devices')

###################################################################################################
