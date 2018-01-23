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
    err, ret = Cmd.excecute(cmd)
    if err:
        msg = 'Error "{0}" - Can not add device "{1}"'.format(err, duid)
        flash(msg, 'danger')
    else:
        msg = 'Device "{}" added'.format(duid)
        flash(msg, 'info')

    return redirect(url_for('web_devices'))

###################################################################################################

@APP.route('/devices/edit/<int:idx>/')
def web_device_edit(idx=-1):
    """ TODO """
    cmd = 'device[{}] edit'.format(idx)
    err, ret = Cmd.excecute(cmd)
    if err:
        msg = 'Error "{0}" - Can not edit device task [{1}]'.format(err, idx)
        flash(msg, 'danger')
        return redirect(url_for('web_devices_list'))
    else:
        msg = 'Device "{}" edit'.format(idx)
        flash(msg, 'info')

    return redirect(url_for('web_devices_list'))

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
        msg = 'Device task deleted'
        flash(msg, 'info')

    return redirect(url_for('web_devices'))

###################################################################################################
