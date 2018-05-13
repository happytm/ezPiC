"""
Web Plugin for Device-Pages
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
        Web.flash_error(httpResponse, err, ret)
        ret = []

    vars = {}
    vars['menu'] = 'devices'
    vars['device_list'] = ret

    return httpResponse.WriteResponsePyHTMLFile('www/devices.html', vars=vars)

###################################################################################################

@MicroWebSrv.route('/devices/list/')
def web_devices_list(httpClient, httpResponse):
    """ TODO """

    err, ret = Web.command('plugin.device.list')
    if err:
        Web.flash_error(httpResponse, err, ret)
        ret = []

    vars = {}
    vars['menu'] = 'devices'
    vars['device_list'] = ret

    return httpResponse.WriteResponsePyHTMLFile('www/devices_list.html', vars=vars)

###################################################################################################

@MicroWebSrv.route('/devices/add/<duid>/')
def web_device_add(httpClient, httpResponse, args):
    """ TODO """
    duid = args['duid']

    params = {'duid': duid}
    err, ret = Web.command('device.add', items=params)
    if err:
        Web.flash_error(httpResponse, err, ret, duid)
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
        Web.flash_error(httpResponse, err, ret, idx)
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
        if err:
            Web.flash_error(httpResponse, err, ret, idx)
        err, ret = Web.command('save')
    else: # GET
        pass

    vars = {}
    vars['menu'] = 'devices'
    #vars['name'] = 'TEST'
    vars['index'] = idx
    vars.update(params)

    err, html = Web.command('device.gethtml', index=idx)

    return httpResponse.WriteResponsePyHTMLFile(html, vars=vars)

###################################################################################################

@MicroWebSrv.route('/devices/del/<idx>/')
def web_device_del(httpClient, httpResponse, args):
    """ TODO """
    idx = int(args['idx'])

    err, ret = Web.command('device.delete', index=idx)
    if err:
        Web.flash_error(httpResponse, err, ret, idx)
    else:
        err, ret = Web.command('save')
        msg = 'Device task deleted'
        httpResponse.FlashMessage(msg, 'info')

    return httpResponse.WriteResponseRedirect('/devices')

###################################################################################################
