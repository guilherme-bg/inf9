{% extends 'base.tpl' %}
{% block content %}
	{{ super() }}
	<h1> Lista de Empréstimos </h1>
	<table class="table table-bordered">	
	<tr>
		<th> id</th>
		<th>Titulo</th>
		<th>Autor</th>
		<th>ISBN</th>
		<th>Ano</th>
		<th>Editora</th>
		<th>Sinopse</th>
	<tr>
	{%for dado in dados %}
	{% if dado.status == 1 %}
	<tr>
		<td>{{dado.id}}</td>
		<td>{{dado.titulo}}</td>
		<td>{{dado.autor}}</td>
		<td>{{dado.isbn}}</td>
		<td>{{dado.ano}}</td>
		<td>{{dado.editora}}</td>
		<td>{{dado.sinopse}}</td>		
		<td><a href="/devolveremprestimo/{{dado.id}}" class='btn btn-danger'> Devolver</a></td>
	</tr>
	{% endif %}
	{% endfor %}
	</table>
{% endblock %}