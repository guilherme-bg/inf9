{% extends 'base.tpl' %}
{% block content %}
	{{ super() }}
	<h1> Detalhes do Livro </h1>
	<table class="table table-bordered">
	<thead>	
	<tr>
		<th> id</th>
		<th>Titulo</th>
		<th>Autor</th>
		<th>ISBN</th>
		<th>Ano</th>
		<th>Editora</th>
		<th>Sinopse</th>
	<tr>
	</thead>
	<tbody>
	<tr>
		<td>{{dado.id}}</td>
		<td>{{dado.titulo}}</td>
		<td>{{dado.autor}}</td>
		<td>{{dado.isbn}}</td>
		<td>{{dado.ano}}</td>
		<td>{{dado.editora}}</td>
		<td>{{dado.sinopse}}</td>
	</tr>
	</tbody>
	</table>
{% endblock %}