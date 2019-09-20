<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <title>dizzi</title>
    <link rel="icon" href="{{url_for('static',filename='img/favicon.png')}}" />
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="{{url_for('static',filename='css/bootstrap.min.css')}}" />
    <!-- animate CSS -->
    <link rel="stylesheet" href="{{url_for('static',filename='css/animate.css')}}" />
    <!-- owl carousel CSS -->
    <link rel="stylesheet" href="{{url_for('static',filename='css/owl.carousel.min.css')}}" />
    <!-- themify CSS -->
    <link rel="stylesheet" href="{{url_for('static',filename='css/themify-icons.css')}}" />
    <!-- flaticon CSS -->
    <link rel="stylesheet" href="{{url_for('static',filename='css/flaticon.css')}}" />
    <!-- font awesome CSS -->
    <link rel="stylesheet" href="{{url_for('static',filename='css/magnific-popup.css')}}" />
    <!-- swiper CSS -->
    <link rel="stylesheet" href="{{url_for('static',filename='css/slick.css')}}" />
    <!-- style CSS -->
    <link rel="stylesheet" href="{{url_for('static',filename='css/style.css')}}" />
  </head>

  <body>
    <!--::header part start::-->
    <header class="main_menu home_menu">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-12">
            <nav class="navbar navbar-expand-lg navbar-light">
              <a class="navbar-brand" href="index.html">
                <img src="{{url_for('static',filename='img/logo.png')}}" alt="logo" />
              </a>
              <button
                class="navbar-toggler"
                type="button"
                data-toggle="collapse"
                data-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent"
                aria-expanded="false"
                aria-label="Toggle navigation"
              >
                <span class="ti-menu"></span>
              </button>

              <div
                class="collapse navbar-collapse main-menu-item justify-content-center"
                id="navbarSupportedContent"
              >
                <ul class="navbar-nav align-items-center">
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
              </div>
              
            </nav>
          </div>
        </div>
      </div>
    </header>
    <!-- Header part end-->

    <!-- breadcrumb start-->
    <section class="breadcrumb breadcrumb_bg align-items-center">
        <div class="container">
            <div class="row align-items-center justify-content-between">
                <div class="col-sm-6">
                    <div class="breadcrumb_tittle">
                        <h2>Informações de Contato</h2>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- breadcrumb start-->

  <!-- ================ contact section start ================= -->
  <section class="about_part section_padding">
      <div class="container">
        <div class="row align-items-center justify-content-between">
          <div class="col-md-6">
            <div class="about_part_text">
              <h5>Contato</h5>
              <h2>Email: guilhermebritogasparini@gmail.com</h2>
            </div>
          </div>
          
        </div>
      </div>
    </section>
    <!-- jquery plugins here-->
    <script src="js/jquery-1.12.1.min.js"></script>
    <!-- popper js -->
    <script src="js/popper.min.js"></script>
    <!-- bootstrap js -->
    <script src="js/bootstrap.min.js"></script>
    <!-- easing js -->
    <script src="js/jquery.magnific-popup.js"></script>
    <!-- isotope js -->
    <script src="js/isotope.pkgd.min.js"></script>
    <!-- particles js -->
    <script src="js/owl.carousel.min.js"></script>
    <script src="js/jquery.nice-select.min.js"></script>
    <!--contact js-->
    <script src="js/contact.js"></script>
    <script src="js/jquery.ajaxchimp.min.js"></script>
    <script src="js/jquery.form.js"></script>
    <script src="js/jquery.validate.min.js"></script>
    <script src="js/mail-script.js"></script>
    <!-- custom js -->
    <script src="js/custom.js"></script>
</body>
</html>
  