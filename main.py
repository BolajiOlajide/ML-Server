from __future__ import absolute_import, division, print_function, \
    unicode_literals
import os

from flask import Flask, g, jsonify, request, session, redirect
from dotenv import load, get as getEnv
from flask_openid import OpenID
# from flask_login import login_user, logout_user, current_user, login_required

from helper import emulate_ml_model

load()

app = Flask(__name__)

env = getEnv('ENV')

if env:
    app.config['DEBUG'] = True
app.config['SECRET_KEY'] = getEnv('SECRET')

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
# lm = LoginManager()
# lm.init_app(app)
oid = OpenID(app, os.path.join(BASE_DIR, 'tmp'), safe_roots=[])


@app.before_request
def lookup_current_user():
    g.user = None
    if 'openid' in session:
        g.user = session['openid']
        # g.user = User.query.filter_by(openid=openid).first()


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None:
        return redirect(oid.get_next_url())
    if request.method == 'POST':
        openid = request.json.get('openid')
        if openid:
            return oid.try_login(openid, ask_for=['email', 'nickname'],
                                ask_for_optional=['fullname'])
    return jsonify({'error': 'No valid Open ID provider specified'}), 400


@oid.after_login
def set_user_session_login(resp):
    session['openid'] = resp.identity_url
    return redirect(oid.get_next_url())


@app.route('/')
def index():
    print(session)
    return 'API is working!'


@app.route('/ml', methods=['POST'])
def ml():
    json_input = request.json
    output_data = emulate_ml_model(json_input)
    return jsonify({'data': output_data})


@app.route('/logout')
def logout():
    session.pop('openid', None)
    return redirect(oid.get_next_url())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=getEnv('PORT', 8080))
