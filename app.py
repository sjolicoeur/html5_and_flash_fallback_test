from flask import Flask, g, request, redirect, url_for, Response, session, abort, flash
from flask.ext.login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin, AnonymousUser,
                            confirm_login, fresh_login_required)
from flask import render_template
from flask.ext.wtf import Form, TextField, Required, EqualTo, ValidationError
from flask import send_from_directory

import flask_sijax
import os, re
from werkzeug import secure_filename
import re
import glob
from flaskext.autoindex import AutoIndex
import os.path 

def getint(name):
    found = re.match("\S+\-(\d+).jpg", name)
    if found :
        num = found.group(1)
        return int(num)
    return 0

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


app = Flask(__name__)
#AutoIndex(app, browse_root=os.path.curdir)

SECRET_KEY = "aa yeah, not actually a secret"
DEBUG = True
sijax_path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')

UPLOAD_FOLDER = os.path.join('.', os.path.dirname(__file__), 'static/tmp_uploads/')
ALLOWED_EXTENSIONS = set(['ppt', 'pdf', 'pptx', 'doc'])

app.config['SECRET_KEY'] = "aa yeah, not actually a secret"
app.config['DEBUG'] = True
app.config['SIJAX_STATIC_PATH'] = sijax_path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

flask_sijax.Sijax(app)
presentation_path = os.path.join('.', os.path.dirname(__file__), 'static/converted_docs/') 

@app.route('/', methods=['GET'])
def index():
    #return "te"
    return render_template("player.html")

@app.route('/nfb', methods=['GET'])
def index_nfb():
    #return "te"
    return render_template("player_onf.html")

@app.route('/van', methods=['GET'])
def index_van():
    #return "te"
    return render_template("player_vanilla.html")
 
@app.route('/crossdomain.xml', methods=['GET'])
def crossdomain():
    return """<?xml version="1.0"?>
        <!DOCTYPE cross-domain-policy SYSTEM "http://www.macromedia.com/xml/dtds/cross-domain-policy.dtd">
        <cross-domain-policy>
            <allow-access-from domain="*" />
            <param name="allowNetworking" value="all" />
            <site-control permitted-cross-domain-policies="master-only"/>
            <allow-http-request-headers-from domain="*.onf.ca" headers="X-NFB*"/> 
            <allow-http-request-headers-from domain="*.nfb.ca" headers="X-NFB*"/>
            <allow-http-request-headers-from domain="localhost" headers="X-NFB*"/>
            <allow-http-request-headers-from domain="*.facebook.com" headers="X-NFB*"/>
        </cross-domain-policy>
        """

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8989)
