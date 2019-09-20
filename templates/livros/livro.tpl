{% extends 'base.tpl' %}
{% block content %}
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
	<h1> Lista de Livros </h1>
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
	{%for dado in dados %}
	<tr>
		<td>{{dado.id}}</td>
		<td>{{dado.titulo}}</td>
		<td>{{dado.autor}}</td>
		<td>{{dado.isbn}}</td>
		<td>{{dado.ano}}</td>
		<td>{{dado.editora}}</td>
		<td>{{dado.sinopse}}</td>
		<td><a href="/livro/{{dado.id}}"> Visualizar</a></td>
	</tr>
	{% endfor %}
	</table>
{% endblock %}