"""
...TODO
"""
from flask import request, session, g, redirect, url_for, abort, render_template, flash, escape
from G import APP

###################################################################################################

@APP.route('/')
def index():
    """ TODO """
    error = None
    if 'username' in session:
        pass #error = 'Logged in as %s' % escape(session['username'])
    else:
        error = 'You are not logged in | ' + APP.config['USERNAME'] + ' | ' + APP.config['PASSWORD']
    return render_template('index.html', error=error)

###################################################################################################

@APP.errorhandler(404)
def not_found(error):
    """ TODO """
    return render_template('error404.html', error=error), 404

###################################################################################################

@APP.route('/main/')
def main_():
    """ TODO """
    return render_template('main.html', menu='main')

###################################################################################################
