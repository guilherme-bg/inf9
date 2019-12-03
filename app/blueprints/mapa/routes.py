from flask import render_template, flash, redirect, request
from . import mapa

@mapa.route('/mapa')
def mapa():
    return render_template('mapa/mapa.tpl')


