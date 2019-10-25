{% extends 'base.tpl' %}
{% import 'bootstrap/wtf.html' as wtf %}
{% block title %} Registrar {% endblock %}
 
{% block content %}
{{ super() }}
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
 <h1>Registrar empréstimo</h1>
<form action="{{url_for('emprestimos.emprestimo_cadastro_post')}}" method="post">
<div class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title">Livros</h3>
  </div>
  <div class="panel-body">
    {{ form.livro }}
  </div>
</div>
<div class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title">Usuários</h3>
  </div>
  <div class="panel-body">
    {{ form.usuario }}
  </div>
</div>
{{ form.csrf_token }}
<button class= "btn btn-succes">Enviar</button<
</form>
 </div>
</div>
{% endblock %}

