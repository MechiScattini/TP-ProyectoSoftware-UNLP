<template>
  <div class="container mt-5">
  <div class="row">
    <div class="col-sm-4">

      <div class="conteiner-info">
        <h2>Todo sobre denuncias</h2>
        <div class="fakeimg">Fake Image</div>
        <p>Some text about me in culpa qui officia deserunt mollit anim..</p>
        <a class="nav-link" href="#">Link</a>
      </div>

      <div class="conteiner-info">
        <h2 class="mt-5">
          <router-link to="/denuncias-carga" class="nav-link">Realizar Denuncia</router-link>
        </h2>
        <p>Si desea realizar una denuncia ingrese.</p>
      </div>

      <div class="conteiner-info">
      <h3 class="mt-4">Links de interes</h3>
      <p>Lorem ipsum dolor sit ame.</p>
      <ul class="nav nav-pills flex-column">
        <li class="nav-item">
          <a class="nav-link active" href="#">Active</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#">Disabled</a>
        </li>
      </ul>
      <hr class="d-sm-none">
      </div>
    </div>
    <div class="col-sm-8">
      <div class="conteiner-info">
        <h2>Puntos de Encuentro</h2>
        <div class="fakeimg">Fake Image</div>
        <p>Sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p>
        <a class="nav-link active" href="#">Ver mas</a>
      </div>
      <div class="conteiner-info">
        <h2 class="mt-5">
          <router-link to="/zonas-inundables" class="nav-link">Zonas inundables</router-link>
        </h2>
        <p>Información y visualización de las zonas inundables de La Plata.</p>
        <!-- <img src="../../../app/static/img/mapa.png"> -->
      </div>
      <div class="conteiner-info">
        <h2 class="mt-5">Recorridos de evacuacion</h2>
        <div class="fakeimg">Fake Image</div>
        <p>Vea los recorridos de evacuación.</p>
        <a class="nav-link active" href="#">Ver mas</a>
      </div>
    </div>
  </div>
</div>
</template>
