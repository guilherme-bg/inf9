from flask import render_template, flash, redirect, request
from . import mapa
from geopy.geocoders import Nominatim
from .forms import FormEndereco

@mapa.route('/mapa')
def mapa():
    x = request.args()
    print(x)
    return render_template('mapa/mapa.tpl')

@mapa.route('/mapa/busca', methods=['GET'])
def endereco_get():
    form = FormEndereco()
    return render_template('mapa/mapa.tpl', form=form)

@mapa.route('/mapa/busca', methods=['POST'])
def endereco_get():
    form = FormEndereco()
    if form.validate_on_submit():
        locator = Nominatim(user_agent="Intro Geocode")
        location = locator.geocode(form.endereco.data)
    return redirect(url_for('mapa', lat = location.latitude, lng = location.longitude))
