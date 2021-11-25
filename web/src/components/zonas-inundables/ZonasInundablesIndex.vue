<template>
<div>
  <form class="form">
    <l-map style="height: 300px" :zoom="zoom" :center="center">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <div v-for="(zona,index) in zonas" :key="zona.id">
        <l-polygon :lat-lngs="zona.coordenadas" :color="zona.color" :fill="true" :fillColor="zona.color"></l-polygon>
        {{zona.nombre}} {{index}}
      </div>
    </l-map>
    <ul>
      <li v-for="(zona) in zonas" :key="zona.id">
        {{zona.nombre}}
      </li>
    </ul>
  </form>
</div>
</template>

<script>
import { LMap, LTileLayer, LPolygon } from '@vue-leaflet/vue-leaflet'

export default {
  components: {
    LMap,
    LTileLayer,
    LPolygon
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 13,
      center: [-34.9187, -57.956],
      zonas: []
    }
  },
  created () {
    fetch('https://admin-grupo18.proyecto2021.linti.unlp.edu.ar/api/zonas-inundables/').then((response) => {
      return response.json()
    }).then((json) => {
      this.zonas = json.zonas
    }).catch((e) => {
      console.log(e)
    })
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
</style>
