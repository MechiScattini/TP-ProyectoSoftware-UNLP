<template>
<div>
<form class="form">
    <l-map style="height: 300px" :zoom="zoom" :center="center">
        <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
        <div>
            <l-marker :lat-lngs="markerLngLat" :fill="true" >
            </l-marker>
            {{punto.nombre}}
        </div>
    </l-map>
    <ul>
        <li> nombre:         {{punto.nombre}}       </li>
        <li> dirección:         {{punto.direccion}}       </li>
        <li> teléfono:          {{punto.telefono}}       </li>
        <li> email:          {{punto.email}}       </li>
    </ul>
    <router-link to="/puntosRecorridos" class="link">Volver</router-link>
</form>
</div>
</template>

<script>
import { LMap, LTileLayer, LMarker } from '@vue-leaflet/vue-leaflet'



export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 13,
      center: [-34.9187, -57.956],
      markerLngLat: [punto.coordenadas] 
      id: 0
    }
  },
  async created () {
    this.id = this.$route.params.id //  pone como id el pasado como parámetro de la URL

    //  hace el fetch a la api
    try {
      const response = await fetch('https://admin-grupo18.proyecto2021.linti.unlp.edu.ar/api/puntos-encuentro/' + this.id)
      const json = await response.json()
      this.punto = json[1]
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
