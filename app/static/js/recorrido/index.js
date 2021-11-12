
import { MapaZona } from './MapaZona.js';

const submitHandler = (event, map) => {
    event.preventDefault();
    if(!map.hasValidZone()) {
        alert('debes seleccionar un recorrido en el mapa');
    }
    else{
        const name = document.querySelector('#recorrorido_name').value;
        const coordinates = map.drawnlayers[0].getLatLngs().flat().map(coordinate => {
            return {lat: coordinate.lat, lng: coordinate.lng }
        });
        const formData = new FormData();
        formData.append('name',name);
        formData.append('coordinates',JSON.stringify(coordinates));
        fetch('/recorridos',{
            method: 'POST',
            body: formData
        })

        latlng = map.marker.getLatLng();
        document.getElementById('lat').setAttribute('value',latlng.lat);
        document.getElementById('lng').setAttribute('value',latlng.lng);
    }
}

window.onload = () =>{
    const map = new MapaZona({
        selector: 'mapid',
        // coordenadas: coord,
        //color:color,
        addSearch: true
    });

    const form = document.getElementById('#id-recorrido-form');
    form.addEventListener('submit',(event) => submitHandler(event,map));
}
