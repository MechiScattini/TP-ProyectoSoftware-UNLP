<template>
    <div>
        <h2>Estadisticas</h2>
        <h2>{{estadisticas.cantidad_puntos}}</h2>
    </div>
</template>
<script>
export default {
    data () {
        return {
            estadisticas: {}
        }
    },
    async created () {
        try {
            const response = await fetch('https://admin-grupo18.proyecto2021.linti.unlp.edu.ar/api/estadisticas/')
            console.log(response)
            const json = await response.json()
            this.estadisticas = json.estadisticas
            console.log(this.estadisticas)
        }     
        catch (e) {
            alert(e)
        }
    }
  }
</script>
