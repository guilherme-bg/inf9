{% extends 'base.tpl' %}
{% block content %}
	<h1> Detalhes do Usuario </h1>
	<table>	
	<tr>
		<th> id</th>
		<th>Nome</th>
		<th>Email</th>
		<th>Password</th>
	<tr>
	<tr>
		<td>{{dado.id}}</td>
		<td>{{dado.nome}}</td>
		<td>{{dado.email}}</td>
		<td>{{dado.password_hash}}</td>		
	</tr>
	</table>
{% endblock %}