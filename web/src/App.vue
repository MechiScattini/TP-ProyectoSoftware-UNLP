<template>
<div>
  <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-uWxY/CJNBR+1zjPWmfnSnVxwRheevXITnMqoEIeG1LJrdI0GlVs/9cVSyPYXdcSF" crossorigin="anonymous">
    <title>Home</title>
  </head>

  <div id="nav" class="navbar navbar-expand-lg navbar-dark bg-dark navbar-fixed-top">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Logotipo</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarScroll">
          <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
            <li class="nav-item">
              <router-link to="/" class="nav-link">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/iniciar-sesion" class="nav-link">Iniciar Sesion</router-link>
            </li>
          </ul>
        </div>
    </div>
  </div>
  <router-view/>
  <footer>
    <h4 class="title"> Bomberos: 100 - Seguridad: 911 - Ambulancia: 107 - Prefectura: 106 -</h4>
    <p>Copyright © 2021. LPSoft.</p>
  </footer>
</div>
</template>
