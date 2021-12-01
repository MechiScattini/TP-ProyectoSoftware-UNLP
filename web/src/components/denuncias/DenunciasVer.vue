<template>
<div>
  <div v-if = denuncias>
    <form class="form">
        <l-map style="height: 300px" :zoom="zoom" :center="center">
        <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
        <div v-for="(denuncia) in denuncias" :key="denuncia.id">
            <l-marker :lat-lng="denuncia.coordenadas[0]" >
                <l-popup>{{denuncia.titulo}}</l-popup>
            </l-marker>
        </div>
        </l-map>
        <ul>
        <li v-for="(denuncia) in denuncias" :key="denuncia.id">
            {{denuncia.titulo}}
            <router-link to= "/" class="link">Ver detalles</router-link>
        </li>
        </ul>
    </form>
    <button v-if="page>1" @click=decrement>Ant</button>
    <p>{{page}}</p>
    <button @click=increment>Siguiente</button>
  </div>
  <div v-else>
    No hay denuncias
  </div>
</div>
</template>

<script>
import { LMap, LTileLayer, LMarker, LPopup } from '@vue-leaflet/vue-leaflet'

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 13,
      center: [-34.9187, -57.956],
      denuncias: [],
      page: 1
    }
  },
  methods: {
    // a computed getter
    increment () {
      // `this` points to the vm instance
      this.page++
    },
    decrement () {
      // `this` points to the vm instance
      this.page--
    }
  },
  async created () {
    //  centra el mapa en la localización del usuario
    if ('geolocation' in navigator) {
      var self = this
      navigator.geolocation.getCurrentPosition(function (position) {
        self.center = [position.coords.latitude, position.coords.longitude]
      })
    } else {
      alert('Para centrar el mapa en su zona, habilite la localización de su navegador')
    }
    //  hace la petición a la api
    try {
      const response = await fetch('https://admin-grupo18.proyecto2021.linti.unlp.edu.ar/api/denuncias/')
      const json = await response.json()
      this.denuncias = json.denuncias
      //    this.page = json.pagina
    } catch (e) {
      alert(e)
    }
  }
}
</script>

<style scoped>
.form{
text-align: center;
width: 40%;
height: 80%;
padding:16px;
border-radius:10px;
margin: 0 auto;
margin-top: 30px;
background-color:#ccc;
}
.link {
  text-transform: uppercase;
  font-size: 10px;
  background-color: #92a4ad;
  padding: 10px 15px;
  border-radius: 0;
  color: white;
  display: inline-block;
  margin-right: 5px;
  margin-bottom: 5px;
  line-height: 1.5;
  text-decoration: none;
  letter-spacing: 1px;
}
</style>
