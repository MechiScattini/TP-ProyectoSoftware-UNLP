<template>

  <div>
  <h2 style="display:flex; justify-content: center">Puntos de encuentro y recorridos de evacuación</h2>
  <div class="form">
    <l-map style="height: 300px" :zoom="zoom" :center="center">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <div v-for="(punto) in puntos" :key="punto.id">
        <l-marker :lat-lng="punto.coordenadas[0]" :fill="true" >
        <l-popup>
          <ul>
            <li> Nombre:         {{punto.nombre}}       </li>
            <li> Dirección:         {{punto.direccion}}       </li>
            <li> Teléfono:          {{punto.telefono}}       </li>
            <li> Email:          {{punto.email}}       </li>
          </ul>
        </l-popup>
        </l-marker>
      </div>
      <div v-for="(recorrido) in recorridos" :key="recorrido.id">
        <l-polyline :lat-lngs="recorrido.coordenadas">
          <l-popup>
            <ul>
              <li> Nombre:         {{recorrido.nombre}}       </li>
              <li> Descripción:         {{recorrido.descripcion}}       </li>
              <li v-if="recorrido.estado"> Estado:          Publicado       </li>
              <li v-else> Estado:          Despublicado       </li>
            </ul>
          </l-popup>
        </l-polyline>
      </div>
    </l-map>
    <div>
      <ul>
        <h3> Recorridos de evacuación: </h3>
        <li v-for="(recorrido) in recorridos" :key="recorrido.id">
          {{recorrido.nombre}}
        </li>
      </ul>
      <div style="display:flex; justify-content:center">
        <button v-if="pageRecorridos>1" @click=decrementPageR v-on:click="getDataRecorridos">&laquo;</button>
          <p>página:{{pageRecorridos}}</p>
        <button v-if= recorridos @click=incrementPageR v-on:click="getDataRecorridos">&raquo;</button>
      </div>
    </div>
    <div>
      <ul>
        <h3> Puntos de encuentro:  </h3>
        <li v-for="(punto) in puntos" :key="punto.id">
          {{punto.nombre}}
        </li>
      </ul>
      <div style="display:flex; justify-content:center">
        <button v-if="pagePuntos>1" @click=decrementPageP v-on:click="getDataPuntos">&laquo;</button>
          <p>página:{{pagePuntos}}</p>
        <button v-if= puntos @click=incrementPageP v-on:click="getDataPuntos">&raquo;</button>
      </div>
    </div>
  </div>
</div>

</template>
<script>
import { LMap, LTileLayer, LPolyline, LMarker, LPopup } from '@vue-leaflet/vue-leaflet'
export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPolyline,
    LPopup
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 13,
      markerLngLat: [],
      center: [-34.92149, -57.954597],
      polyline: [],
      puntos: {},
      recorridos: {},
      pagePuntos: 1,
      pageRecorridos: 1
    }
  },
  methods: {
    incrementPageP () {
      this.pagePuntos++
    },
    decrementPageP () {
      this.pagePuntos--
    },
    incrementPageR () {
      this.pageRecorridos++
    },
    decrementPageR () {
      this.pageRecorridos--
    },
    async getDataPuntos () {
      try {
        const response = await fetch('https://admin-grupo18.proyecto2021.linti.unlp.edu.ar/api/puntos-encuentro/?page=' + this.pagePuntos)
        const json = await response.json()
        this.puntos = json.puntos
      } catch (e) {
        alert(e)
      }
    },
    async getDataRecorridos () {
      try {
        const response2 = await fetch('https://admin-grupo18.proyecto2021.linti.unlp.edu.ar/api/recorridos-evacuacion/?page=' + this.pageRecorridos)
        const json2 = await response2.json()
        this.recorridos = json2.recorridos
      } catch (e) {
        alert(e)
      }
    }
  },
  async created () {
    //  hace la petición a la api
    try {
      //  peticion a los puntos
      const response = await fetch('https://admin-grupo18.proyecto2021.linti.unlp.edu.ar/api/puntos-encuentro/?page=' + this.page)
      const json = await response.json()
      this.puntos = json.puntos
      //  peticion a recorridos
      const response2 = await fetch('https://admin-grupo18.proyecto2021.linti.unlp.edu.ar/api/recorridos-evacuacion/?page=' + this.page)
      const json2 = await response2.json()
      this.recorridos = json2.recorridos
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
