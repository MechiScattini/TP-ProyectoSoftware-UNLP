
import { MapaZona as Map } from './Map.js';

const submitHandler = (event, map) => {
    event.preventDefault();
    if(!map.hasValidZone()) {
        alert('debes seleccionar una zona en el mapa');
    }
    else{
        latlng = map.marker.getLatLng();
        document.getElementById('lat').setAttribute('value',latlng.lat);
        document.getElementById('lng').setAttribute('value',latlng.lng);
    }
}

window.onload = () =>{

    console.log(coord)

    const map = new Map({
        selector: 'mapid',
        coordenadas: coord,
        //color:color,
        addSearch: true
    });

    const form = document.getElementById('id-punto-form');
    form.addEventListener('submit',(event) => submitHandler(event,map));
}