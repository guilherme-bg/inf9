{% extends 'base.tpl' %}
{% import 'bootstrap/wtf.html' as wtf %}
{% block styles %}

{{ super() }}

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css" />
<style>
	#mapid { height: 500px; }
</style>

{% endblock %}


{% block content %}
	{{ super() }}
	<h1>Buscar Endereço</h1>
 	{{ wtf.quick_form(form) }} 	
{% endblock %}