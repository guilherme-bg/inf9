{% extends 'base.tpl' %}
{% block content %}
	<h1> Lista de Usuarios </h1>
	<table>	
	<tr>
		<th> id</th>
		<th>Nome</th>
		<th>Email</th>
		<th>Password</th>
	<tr>
	{%for dado in dados %}
	<tr>
		<td>{{dado.id}}</td>
		<td>{{dado.nome}}</td>
		<td>{{dado.email}}</td>
		<td>{{dado.password_hash}}</td>
		<td><a href="/usuario/{{dado.id}}"> Visualizar</a></td>
	</tr>
	{% endfor %}
	</table>
{% endblock %}