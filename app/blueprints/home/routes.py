from flask import render_template
from . import home

@home.route('/')
def index():
    return "HOME"