"""
...TODO
"""
from flask import request, session, g, redirect, url_for, abort, render_template, flash, escape
from G import APP

###################################################################################################

@APP.route('/login', methods=['GET', 'POST'])
def login():
    """ TODO """
    error = None
    if request.method == 'POST':
        if request.form['username'] != APP.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != APP.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            session['username'] = request.form['username']
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

###################################################################################################

@APP.route('/logout')
def logout():
    """ TODO """
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))

###################################################################################################
