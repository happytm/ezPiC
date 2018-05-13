"""
...TODO
"""
from MicroWebSrv.microWebSrv import MicroWebSrv

import Tool
import Web

###################################################################################################

@MicroWebSrv.route('/devices')
def web_devices(httpClient, httpResponse):
    """ TODO """

    err, ret = Web.command('device.list')
    if err:
        ret = []

    vars = {}
    vars['menu'] = 'devices'
    vars['device_list'] = ret

    return httpResponse.WriteResponsePyHTMLFile('www/devices.html', headers=None, vars=vars)

###################################################################################################

@MicroWebSrv.route('/devices/list/')
def web_devices_list(httpClient, httpResponse):
    """ TODO """

    err, ret = Web.command('plugin.device.list')
    if err:
        ret = []

    vars = {}
    vars['menu'] = 'devices'
    vars['device_list'] = ret

    return httpResponse.WriteResponsePyHTMLFile('www/devices_list.html', headers=None, vars=vars)

###################################################################################################

@MicroWebSrv.route('/devices/add/<duid>/')
def web_device_add(httpClient, httpResponse, args):
    """ TODO """
    duid = args['duid']

    params = {'duid': duid}
    err, idx = Web.command('device.add', params=params)
    if err:
        msg = 'Error "{0}" - Can not add device "{1}"'.format(err, duid)
        httpResponse.FlashMessage(msg, 'danger')
    else:
        Web.command('save')
        msg = 'Device "{}" added'.format(duid)
        httpResponse.FlashMessage(msg, 'info')

    return httpResponse.WriteResponseRedirect('/devices')

###################################################################################################

@MicroWebSrv.route('/devices/edit/<idx>/')
@MicroWebSrv.route('/devices/edit/<idx>/', 'POST')
def web_device_edit(httpClient, httpResponse, args):
    """ TODO """
    idx = int(args['idx'])

    err, ret = Web.command('device.getparam', index=idx)
    if err:
        msg = 'Error "{0}" - Can not get params from device [{1}]'.format(err, idx)
        httpResponse.FlashMessage(msg, 'danger')
        return httpResponse.WriteResponseRedirect('/devices')

    params = {}
    #params['name'] = 'Test-Name'
    params.update(ret)

    if httpClient.GetRequestMethod() == 'POST':
        formParams = httpClient.ReadRequestPostedFormData()
        if formParams:
            for key, value in params.items():
                if key in formParams:
                    params[key] = formParams.get(key)
        err, ret = Web.command('device.setparam', index=idx, params=params)
        err, ret = Web.command('save')
    else: # GET
        pass

    vars = {}
    vars['menu'] = 'devices'
    #vars['name'] = 'TEST'
    vars['index'] = idx
    vars.update(params)

    err, html = Web.command('device.gethtml', index=idx)

    return httpResponse.WriteResponsePyHTMLFile(html, headers=None, vars=vars)

###################################################################################################

@MicroWebSrv.route('/devices/del/<idx>/')
def web_device_del(httpClient, httpResponse, args):
    """ TODO """
    idx = int(args['idx'])

    err, ret = Web.command('device.delete', index=idx)
    if err:
        msg = 'Error "{0}" - Can not delete device task [{1}]'.format(err, idx)
        httpResponse.FlashMessage(msg, 'danger')
    else:
        err, ret = Web.command('save')
        msg = 'Device task deleted'
        httpResponse.FlashMessage(msg, 'info')

    return httpResponse.WriteResponseRedirect('/devices')

###################################################################################################
