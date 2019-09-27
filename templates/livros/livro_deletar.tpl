{% extends 'base.tpl' %}
{% from 'bootstrap/form.html' import render_form %}
 
{% block title %} Deletar {% endblock %}
 
{% block content %}
{{ super() }}
<ul class="nav">
	  <li class="nav-item">
	    <a class="nav-link" href="/">Home</a>
	  </li>
	  <li class="nav-item">
	    <a class="nav-link" href="/sobre">Sobre</a>
	  </li>
	  <li class="nav-item">
	    <a class="nav-link" href="/contato">Contato</a>
	  </li>
	  <li class="nav-item">
	    <a class="nav-link" href="/usuarios">Usuários</a>
	  </li>
 	  <li class="nav-item">
	    <a class="nav-link" href="/registrar">Registre-se</a>
	  </li>
	  <li class="nav-item">
	    <a class="nav-link" href="/login">Fazer Login</a>
	  </li>
	   <li class="nav-item">
             <a class="nav-link" href="/livros">Livros</a>
           </li>
	   <li class="nav-item">
              <a class="nav-link" href="/registrarlivro">Registrar livro</a>
            </li>  	  
	</ul>
	<h1> Deletar o Livro </h1>
	<table class="table">	
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
	{{ render_form(form) }}

{% endblock %}
