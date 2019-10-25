{% extends 'base.tpl' %}
{% import 'bootstrap/wtf.html' as wtf %}
 
{% block title %} Deletar {% endblock %}
 
{% block content %}
{{ super() }}
	<h1> Deletar o Livro </h1>
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
	<tr>
		<td>{{dado.id}}</td>
		<td>{{dado.titulo}}</td>
		<td>{{dado.autor}}</td>
		<td>{{dado.isbn}}</td>
		<td>{{dado.ano}}</td>
		<td>{{dado.editora}}</td>
		<td>{{dado.sinopse}}</td>
	</tr>
	</table>
	<h2>Tem certeza que deseja excluir o livro?</h2>
	<!--<form action="/livros/excluir/{{dado.id}}"><input type="submit" class="btn btn-danger" value="Deletar"/></form>-->
	{{ wtf.quick_form(form) }}

{% endblock %}
