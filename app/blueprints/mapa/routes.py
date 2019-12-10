from flask import render_template, flash, redirect, request, url_for
from . import mapa
from geopy.geocoders import Nominatim
from .forms import FormEndereco

@mapa.route('/mapa')
def mapa_principal():
    x = request.args['lat']
    y = request.args['lng']
    a = request.args['address']
    print(x)
    print(y)
    return render_template('mapa/mapa.tpl', lat = x, lng = y, ad = a)

@mapa.route('/mapa/busca', methods=['GET'])
def end_get():
    form = FormEndereco()
    return render_template('mapa/mapa_busca.tpl', form=form)

@mapa.route('/mapa/busca', methods=['POST'])
def end_post():
    form = FormEndereco()    
    if form.validate_on_submit():
        locator = Nominatim(user_agent="Intro Geocode")
        location = locator.geocode(form.endereco.data)
        print(location.latitude)
        print(location.longitude)        
        return redirect(url_for('mapa.mapa_principal', lat = location.latitude, lng = location.longitude, address = form.endereco.data))
    else:
        flash('Ferrou! ' + str(e), 'danger')
        return redirect(url_for('mapa.end_get'))