{% extends 'base.tpl' %}

{% block styles %}

{{ super() }}

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css" />
<style>
	#mapid { height: 500px; }
</style>

{% endblock %}


{% block content %}
	{{ super() }}
	 <div id="mapid"></div>
{% endblock %}

{% block scripts %}
	<script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"></script>

	<script>
		var mymap = L.map('mapid').setView([{{lat}}, {{lng}}], 18);
		 L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	maxZoom: 19,
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);
        L.marker([{{lat}}, {{lng}}]).addTo(mymap)
    .bindPopup('{{ad}}')
    .openPopup();

	</script>
{% endblock %}