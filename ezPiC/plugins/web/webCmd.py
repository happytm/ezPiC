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

@APP.route('/cmd/', methods=['GET', 'POST'])
def web_cmd():
    """ TODO """
    ret = '?'
    cmd = ''
    if request.method == 'POST':
        cmd = request.form['cmd']
    else: # GET
        if 'cmd' in request.args:
            cmd = request.args.get('cmd')

    if cmd:
        print(cmd)
        ret = Cmd.excecute(cmd)
        ret = str(ret) + '<a>&äüöÄÖÜß|'
        #ret = html.escape(ret)
        t = 'Cmd ' + cmd + ' -> ' + str(ret)
        logging.debug(t)

    return render_template('cmd.html', menu='tools', cmd=cmd, ret=ret)

###################################################################################################
