{% extends 'base.tpl' %}
{% from 'bootstrap/form.html' import render_form %}
 
{% block title %} Login {% endblock %}
 
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
<div class="container">
 <div class="row">
 {% with messages = get_flashed_messages(with_categories=true) %}
 <!-- Categories: success (green), info (blue), warning (yellow), danger (red) -->
 {% if messages %}
 {% for category, message in messages %}
 <div class="alert alert-{{ category }} alert-dismissible" role="alert">
 <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
 <!-- <strong>Title</strong> --> {{ message }}
 </div>
 {% endfor %}
 {% endif %}
 {% endwith %}
 <h1>Login</h1>
 {{ render_form(form) }}
 </div>
</div>
{% endblock %}
