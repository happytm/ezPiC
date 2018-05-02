"""
...TODO
"""
from flask import request, session, g, redirect, url_for, abort, render_template, flash, escape
from G import APP
from G import MWS
from MicroWebSrv.microWebSrv import MicroWebSrv
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

@MicroWebSrv.route('/main')
def web_mainx(httpClient, httpResponse):
    """ TODO """
    return httpResponse.WriteResponsePyHTMLFile('www/main.pyhtml', headers=None)

@MicroWebSrv.route('/test')
def _httpHandlerTestGet(httpClient, httpResponse) :
	content = """\
	<!DOCTYPE html>
	<html lang=en>
        <head>
        	<meta charset="UTF-8" />
            <title>TEST GET</title>
        </head>
        <body>
            <h1>TEST GET</h1>
            Client IP address = %s
            <br />
			<form action="/test" method="post" accept-charset="ISO-8859-1">
				First name: <input type="text" name="firstname"><br />
				Last name: <input type="text" name="lastname"><br />
				<input type="submit" value="Submit">
			</form>
        </body>
    </html>
	""" % httpClient.GetIPAddr()
	httpResponse.WriteResponseOk( headers		 = None,
								  contentType	 = "text/html",
								  contentCharset = "UTF-8",
								  content 		 = content )


###################################################################################################
