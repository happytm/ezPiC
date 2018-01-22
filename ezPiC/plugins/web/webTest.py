"""
...TODO
"""
#import sys
#sys.path.append('../')
#from ezPiC import app
from flask import request, session, g, redirect, url_for, abort, render_template, flash, escape
from G import APP

#app = G.app
#app = Flask(__name__)
#app = Flask('ezPiC')

XXX = 1
print(APP)
print(globals)
#print(G)

###################################################################################################

@APP.route('/hello/')
@APP.route('/hello/<name>')
def hello(name=None):
    """ TODO """
    return render_template('hello.html', name=name)

###################################################################################################
