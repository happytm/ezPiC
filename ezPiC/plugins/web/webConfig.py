"""
...TODO
"""
from flask import request, session, g, redirect, url_for, abort, render_template, flash, escape
import logging, time
import html
from G import APP
import Tool
import Cmd

###################################################################################################

@APP.route('/config/', methods=['GET', 'POST'])
def web_config():
    """ TODO """
    params = {}
    params['name'] = 'Test-Name'
    params['info'] = 'BlaBla'
    #params.update(ret)

    if request.method == 'POST':
        name = request.form['name']
        for key, value in params.items():
            if key in request.form:
                params[key] = request.form[key]
        #cmd = 'device[{}] set {}'.format(idx, Tool.params_to_str(params))
        #err, ret = Cmd.excecute(cmd)
    else: # GET
        if 'cmd' in request.args:
            cmd = request.args.get('cmd')

    cmd = 'info'
    err, ret = Cmd.excecute(cmd)

    return render_template('config.html', menu='config', **params)

###################################################################################################
