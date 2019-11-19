{% extends 'base.tpl' %}
{% block content %}
	{{ super() }}
	<h1> Lista de Livros </h1>
	<table class="table table-bordered">	
	<tr>
		<th> id</th>
		<th>Titulo</th>
		<th>Autor</th>
		<th>ISBN</th>
		<th>Ano</th>
		<th>Editora</th>
		<th>Sinopse</th>
		<th>Data Empréstimo</th>
		<th>Data Estimada</th>

	<tr>
	{% for dado in dados %}
	<tr>
		<td>{{dado.id}}</td>
		<td>{{dado.titulo}}</td>
		<td>{{dado.autor}}</td>
		<td>{{dado.isbn}}</td>
		<td>{{dado.ano}}</td>
		<td>{{dado.editora}}</td>
		<td>{{dado.sinopse}}</td>
		<td>{{dados_emprestimo.data_emprestimo}}</td>
		<td>{{dados_emprestimo.data_estimada}}</td>                
	</tr>
	{% endfor %}
	</table>
{% endblock %}