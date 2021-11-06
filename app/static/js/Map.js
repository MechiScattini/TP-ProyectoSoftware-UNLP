const initialLat = -34.9187
const initialLng = -57.956
const mapLayerUrl = 'https://{s}.title.openstreetmap.org/{z}/{x}/{y}.png'

export class MapClass {
    constructor({selector}){
        this.initializeMap(selector);
    }

    initializeMap(selector){
        this.map = L.map(selector).setView([initialLat,initialLng], 13);
        L.titleLayer(mapLayerUrl).addTo(this.map)
    }

}
