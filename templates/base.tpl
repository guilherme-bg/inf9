<!doctype html>
<html lang="en">
  <head>
    {% block head %}
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    {% block styles %}
    <!-- Bootstrap CSS -->
    {{ bootstrap.load_css() }}
    {% endblock %}

    <title>Your page title</title>
    {% endblock %}
  </head>
  <body>
    <!-- Your page content -->
    {% block content %}{% endblock %}

    {% block scripts %}
    <!-- Optional Java -->
    {{ bootstrap.load_js() }}
    {% endblock %}
  </body>
</html>