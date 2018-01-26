"""
...TODO
"""
from flask import request, session, g, redirect, url_for, abort, render_template, flash, escape
from G import APP
import Cmd

###################################################################################################

@APP.route('/')
def web_index():
    """ TODO """
    error = None
    #if 'username' in session:
    #    pass #error = 'Logged in as %s' % escape(session['username'])
    #else:
    #    error = 'You are not logged in | ' + APP.config['USERNAME'] + ' | ' + APP.config['PASSWORD']

    if 'cmd' in request.args:
        cmd = request.args.get('cmd')
        err, ret = Cmd.excecute(cmd)
        if not err:
            err = 'OK'
        return '[{}] {}'.format(err, ret)

    return render_template('index.html', error=error)

###################################################################################################

@APP.errorhandler(404)
def web_error(error):
    """ TODO """
    return render_template('error.html', error=error), 404

###################################################################################################

@APP.route('/main/')
def web_main():
    """ TODO """
    return render_template('main.html', menu='main')

###################################################################################################
