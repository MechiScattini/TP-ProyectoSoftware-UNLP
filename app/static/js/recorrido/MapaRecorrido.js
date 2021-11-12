const initialLat = -34.9187
const initialLng = -57.956
//const mapLayerUrl = 'https://{s}.title.openstreetmap.org/{z}/{x}/{y}.png'
const mapLayerUrl = 'https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=OzyKbXmvXxFkPLosWDvP'


export class MapaRecorrido {
    #drawnItems;

    constructor({selector}){
        this.#drawnItems = new L.FeatureGroup();

        // this.#initializeMap(selector, coordenadas);
        this.#initializeMap(selector)
        this.map.on(L.Draw.Event.CREATED, (e) =>{
            this.#eventHandler(e, this.map, this.#drawnItems, this.editControls, this.createControls)
        });
        this.map.on('draw:deleted', () =>{
            this.#deleteHandler(this.map, this.editControls, this.createControls)
        });
    }

    #initializeMap(selector){
        this.map = L.map(selector).setView([initialLat,initialLng], 13);
        L.tileLayer(mapLayerUrl).addTo(this.map);

        // let polyline=L.polygon(coordenadas,{color:'red'});
        // polygon.addTo(this.map);

        this.map.addLayer(this.#drawnItems);

        this.map.addControl(this.createControls);
    }

    #eventHandler(e, map, drawnItems, editControls, createControls){
        const existingZones = Object.values(drawnItems._layers);

        if (existingZones.length == 0){
            const type = e.layerType;
            const layer = e.layer;

            if (type === 'marker'){
                //
            }
            layer.editing.enable();
            drawnItems.addLayer(layer);
            editControls.addTo(map);
            createControls.remove();
        }
    }

    #deleteHandler(map, editControls, createControls) {
        createControls.addTo(map);
        editControls.remove();
    }

    hasValidzone() {
        return this.drawnlayers.length === 1;
    }

    get drawnlayers() {
        return Object.values (this.drawnItems._layers);
    }

    get editControls() {
        return this.editControlsToolbar ||= new L.Control.Draw({
            draw: false,
            edit: {
                featureGroup: this.#drawnItems
            }
        });
    }

    get createControls() {
        return this.createControlsToolbar ||= new L.Control.Draw({
            draw: {
                circle: false,
                marker: false,
                polygon: false,
            }
        });
    }
}
