"""
...TODO
"""
from flask import request, session, g, redirect, url_for, abort, render_template, flash, escape
from G import APP
import Tool
import Cmd

###################################################################################################

@APP.route('/devices/')
def web_devices():
    """ TODO """
    err, ret = Cmd.excecute('device[] list')
    if err:
        ret = []

    return render_template('devices.html', menu='devices', device_list=ret)

###################################################################################################

@APP.route('/devices/list/')
def web_devices_list():
    """ TODO """
    err, ret = Cmd.excecute('device list')
    if err:
        ret = []

    return render_template('devices_list.html', menu='devices', device_list=ret)

###################################################################################################

@APP.route('/devices/add/<duid>/')
def web_device_add(duid=None):
    """ TODO """
    cmd = 'device[] add {}'.format(duid)
    err, idx = Cmd.excecute(cmd)
    if err:
        msg = 'Error "{0}" - Can not add device "{1}"'.format(err, duid)
        flash(msg, 'danger')
    else:
        err, ret = Cmd.excecute('save')
        msg = 'Device "{}" added'.format(duid)
        flash(msg, 'info')

    return redirect(url_for('web_device_edit', idx = idx))
    # return render_template(html, menu='devices', **params)

###################################################################################################

@APP.route('/devices/edit/<int:idx>/', methods=['GET', 'POST'])
def web_device_edit(idx=-1):
    """ TODO """
    cmd = 'device[{}] get'.format(idx)
    err, ret = Cmd.excecute(cmd)
    if err:
        msg = 'Error "{0}" - Can not get params from device [{1}]'.format(err, idx)
        flash(msg, 'danger')
        return redirect(url_for('web_devices'))

    params = {}
    params['name'] = 'Test-Name'
    params.update(ret)

    cmd = ''
    err = ''
    ret = ''

    if request.method == 'POST':
        for key, value in params.items():
            if key in request.form:
                params[key] = request.form[key]
        #params.update(request.form)
        cmd = 'device[{}] set {}'.format(idx, Tool.params_to_str(params))
        err, ret = Cmd.excecute(cmd)
        err, ret = Cmd.excecute('save')
    else: # GET
        if 'cmd' in request.args:
            cmd = request.args.get('cmd')

    cmd = 'device[{}] html'.format(idx)
    err, html = Cmd.excecute(cmd)

    params['index'] = idx
    
    return render_template(html, menu='devices', **params)

###################################################################################################

@APP.route('/devices/del/<int:idx>/')
def web_device_del(idx=-1):
    """ TODO """
    cmd = 'device[{}] del'.format(idx)
    err, ret = Cmd.excecute(cmd)
    if err:
        msg = 'Error "{0}" - Can not delete device task [{1}]'.format(err, idx)
        flash(msg, 'danger')
        return redirect(url_for('web_devices_list'))
    else:
        err, ret = Cmd.excecute('save')
        msg = 'Device task deleted'
        flash(msg, 'info')

    return redirect(url_for('web_devices'))

###################################################################################################
