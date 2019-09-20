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
	<h1> Lista de Usuarios </h1>
	<table class="table">	
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