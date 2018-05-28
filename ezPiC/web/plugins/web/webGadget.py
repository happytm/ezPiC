"""
Web Plugin for Gadget-Pages
"""
from web.MicroWebSrv.microWebSrv import MicroWebSrv

import com.Tool as Tool
import web.Web as Web

#######

@MicroWebSrv.route('/gadgets')
def web_gadgets(httpClient, httpResponse):
    """ TODO """

    err, ret = Web.command('gadget.list')
    if err:
        Web.flash_error(httpResponse, err, ret)
        ret = []

    vars = {}
    vars['menu'] = 'gadgets'
    vars['gadget_list'] = ret

    return httpResponse.WriteResponsePyHTMLFile('web/www/gadgets.html', vars=vars)

#######

@MicroWebSrv.route('/gadgets/list/')
def web_gadgets_list(httpClient, httpResponse):
    """ TODO """

    err, ret = Web.command('plugin.gadget.list')
    if err:
        Web.flash_error(httpResponse, err, ret)
        ret = []

    vars = {}
    vars['menu'] = 'gadgets'
    vars['gadget_list'] = ret

    return httpResponse.WriteResponsePyHTMLFile('web/www/gadgets_list.html', vars=vars)

#######

@MicroWebSrv.route('/gadgets/add/<ggpid>/')
def web_gadget_add(httpClient, httpResponse, args):
    """ TODO """
    ggpid = args['ggpid']

    params = {'ggpid': ggpid}
    err, ret = Web.command('gadget.add', items=params)
    if err:
        Web.flash_error(httpResponse, err, ret, ggpid)
    else:
        Web.command('save')
        msg = 'Gadget "{}" added'.format(ggpid)
        httpResponse.FlashMessage(msg, 'info')

    return httpResponse.WriteResponseRedirect('/gadgets')

#######

@MicroWebSrv.route('/gadgets/edit/<idx>/')
@MicroWebSrv.route('/gadgets/edit/<idx>/', 'POST')
def web_gadget_edit(httpClient, httpResponse, args):
    """ TODO """
    idx = int(args['idx'])

    err, ret = Web.command('gadget.getparam', index=idx)
    if err:
        Web.flash_error(httpResponse, err, ret, idx)
        return httpResponse.WriteResponseRedirect('/gadgets')

    params = {}
    params.update(ret)

    if httpClient.GetRequestMethod() == 'POST':
        formParams = httpClient.ReadRequestPostedFormData()        
        if formParams:
            formParams['enable'] = 'enable' in formParams   # checkbox -> bool
            formParams['timer'] = int(formParams.get('timer', 0))
            for key, value in params.items():
                if key in formParams:
                    params[key] = formParams.get(key)
        err, ret = Web.command('gadget.setparam', index=idx, params=params)
        if err:
            Web.flash_error(httpResponse, err, ret, idx)
        err, ret = Web.command('save')
        httpResponse.FlashMessage('Settings saved', 'info')
    else: # GET
        pass

    vars = {}
    vars['menu'] = 'gadgets'
    vars['index'] = idx
    vars.update(params)

    err, html = Web.command('gadget.gethtml', index=idx)

    return httpResponse.WriteResponsePyHTMLFile(html, vars=vars)

#######

@MicroWebSrv.route('/gadgets/del/<idx>/')
def web_gadget_del(httpClient, httpResponse, args):
    """ TODO """
    idx = int(args['idx'])

    err, ret = Web.command('gadget.delete', index=idx)
    if err:
        Web.flash_error(httpResponse, err, ret, idx)
    else:
        err, ret = Web.command('save')
        msg = 'Gadget task deleted'
        httpResponse.FlashMessage(msg, 'info')

    return httpResponse.WriteResponseRedirect('/gadgets')

#######