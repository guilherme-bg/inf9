from flask import render_template
from . import home

@home.route('/')
def index():
    return render_template('home/index.tpl')
@home.route('/sobre')
def sobre():
    return render_template('home/about.tpl')
@home.route('/contato')
def contato():
    return render_template('home/contact.tpl')