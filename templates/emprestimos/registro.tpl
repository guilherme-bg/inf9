{% extends 'base.tpl' %}
{% from 'bootstrap/form.html' import render_field %}
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


{{ render_field(form.livro) }}
 </div>
</div>
{% endblock %}
