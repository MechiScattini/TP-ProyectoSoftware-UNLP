const initialLat = -34.9187;
const initialLng = -57.956;
const mapLayerUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';

export function Map({selector}){
    let marker;
    let map;

    //Instansiación del mapa
    initializeMap(selector);

    //Creación del mapa
    function initializeMap(selector){
        map = L.map(selector).setView([initialLat,initialLng], 13);
        L.tileLayer(mapLayerUrl).addTo(map);
    };

    return {
        get marker() {return marker},
        addMarker: addMarker
    };
}