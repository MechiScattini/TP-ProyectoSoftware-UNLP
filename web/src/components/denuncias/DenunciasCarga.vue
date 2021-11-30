<template>
  <div>
  <form name="form-denunciaCarga" id="form-denunciaCarga" v-on:submit.prevent="agregarDenuncia();">
  <h2 style="display: flex; justify-content: center;">Crear una denuncia</h2>
  <p>
    Titulo: <input type="text" name="titulo" placeholder="Titulo" class="form-control" required v-model="denuncia.titulo">
  </p>
  <p>
    Descripcion: <input type="text" name="descripcion" placeholder="Descripcion" class="form-control" required maxlength="80" v-model="denuncia.descripcion">
  </p>
  <p>
    Apellido Denunciante: <input type="text" name="apellido_denunciante" placeholder="Apellido Denunciante" class="form-control" required v-model="denuncia.apellido_denunciante">
  </p>
  <p>
    Nombre Denunciante: <input type="text" name="nombre_denunciante" placeholder="Nombre Denunciante" class="form-control" required v-model="denuncia.nombre_denunciante">
  </p>
  <p>
    Telefono Denunciante: <input type="text" name="telefono_denunciante" placeholder="Telefono Denunciante" class="form-control" required maxlength="8" v-model="denuncia.telefono_denunciante">
  </p>
  <p>
    Email Denunciante: <input type="email" name="email_denunciante" placeholder="Email Denunciante" class="form-control" required v-model="denuncia.email_denunciante">
  </p>
  <select name="categoria" v-model="denuncia.categoria">
    <option value= 1 >Urgente</option>
    <option value= 2>Advertencia</option>
    <option value= 3>Poco probable</option>
  </select>
  <l-map style="height: 300px" :zoom="zoom" :center="center" @click="onClick">
    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
    <l-marker :lat-lng="markerLatLng"></l-marker>
  </l-map>
  <div>
    <button type="submit">Crear</button>
  </div>
  </form>
  </div>
</template>
<script>
import { LMap, LTileLayer, LMarker } from '@vue-leaflet/vue-leaflet'
export default {
  name: 'DenunciaComponent',
  components: {
    LMap,
    LTileLayer,
    LMarker
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      zoom: 13,
      center: [-34.9187, -57.956],
      markerLatLng: [-34.9187, -57.956],
      denuncia: {
        titulo: '',
        descripcion: '',
        apellido_denunciante: '',
        nombre_denunciante: '',
        telefono_denunciante: '',
        email_denunciante: '',
        categoria: ''
      }
    }
  },
  methods: {
    agregarDenuncia () {
      const coords = [this.markerLatLng.lat, this.markerLatLng.lng]
      var datosEnviar = {
        titulo: this.denuncia.titulo,
        descripcion: this.denuncia.descripcion,
        apellido_denunciante: this.denuncia.apellido_denunciante,
        nombre_denunciante: this.denuncia.nombre_denunciante,
        telefono_denunciante: this.denuncia.telefono_denunciante,
        email_denunciante: this.denuncia.email_denunciante,
        categoria: this.denuncia.categoria,
        coordenadas: coords
      }
      console.log(coords)
      fetch('http://localhost:5000/api/denuncias', {
        method: 'POST',
        body: JSON.stringify(datosEnviar)
      })
        .then(respuesta => respuesta.json())
        .then(datosRespuesta => {
          console.log(datosRespuesta)
        })
    },
    onClick (e) {
      if (e.latlng) {
        this.markerLatLng = e.latlng
      }
    }
  }
}
</script>
