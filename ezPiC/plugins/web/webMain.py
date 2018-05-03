"""
...TODO
"""
from MicroWebSrv.microWebSrv import MicroWebSrv
import Cmd

###################################################################################################

@MicroWebSrv.route('/xxx')
@MicroWebSrv.route('/')
def web_index(httpClient, httpResponse):
    """ TODO """
    queryParams  = httpClient.GetRequestQueryParams()
    if queryParams and 'cmd' in queryParams:
        cmd = queryParams.get('cmd')
        err, ret = Cmd.excecute(cmd)
        json = {'error': err, 'result': ret}
        return httpResponse.WriteResponseJSONOk(json)

    vars = {'error': None, 'message': None}
    vars['menu'] = ''

    return httpResponse.WriteResponsePyHTMLFile('www/index.pyhtml', headers=None, vars=vars)

###################################################################################################

#@APP.errorhandler(404)
#def web_error(error):
#    """ TODO """
#    return render_template('error.html', error=error), 404

###################################################################################################

@MicroWebSrv.route('/main')
def web_main(httpClient, httpResponse):
    """ TODO """
    vars = {'error': None, 'message': None}
    vars['menu'] = 'main'

    return httpResponse.WriteResponsePyHTMLFile('www/main.pyhtml', headers=None, vars=vars)

###################################################################################################

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
