"""
...TODO
"""
from flask import request, session, g, redirect, url_for, abort, render_template, flash, escape
from G import APP
import Tool

###################################################################################################

@APP.route('/devices/')
def devices():
    """ TODO """
    return render_template('devices.html', menu='devices')

###################################################################################################

@APP.route('/devices/list/')
def devices_list():
    """ TODO """
    device_list = []
    for dev_id in range(17):
        item = (dev_id, Tool.get_random_string(12), Tool.get_random_string(100))
        device_list.append(item)

    return render_template('devices_list.html', menu='devices', device_list=device_list)

###################################################################################################
