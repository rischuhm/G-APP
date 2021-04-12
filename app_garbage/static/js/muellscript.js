function getLocation() {
        navigator.geolocation.getCurrentPosition(updateMarker);
}

function updateMarker(position) {
    marker = getMarker();
    map = getMap();
    lat = position.coords.latitude;
    lon = position.coords.longitude;
    var L = window.L;
    console.log(map);
    var l = L.latLng(lat, lon);

    map.setView(l,15)
    marker.setLatLng(l);

};

function getMarker() {
    for (obj of Object.keys(window.window["0"])) {
        if (obj.includes("marker_")) {
            return window.window["0"][obj]
        }
    }
};

function getMap() {
    for (obj of Object.keys(window.window["0"])) {
        if (obj.includes("map_")) {
            return window.window["0"][obj]
        }
    }
};


window.addEventListener('load', function () {
    btn_findme = document.getElementById("findme");
    
    marker = getMarker();

    lat_field = document.getElementsByName("lat")[0]
    lon_field = document.getElementsByName("lon")[0]

    lat_field.value = marker.getLatLng().lat;
    lon_field.value = marker.getLatLng().lng;
    // var x = document.getElementById("demo");


    marker.addEventListener("dragend", function () {
        lat_field.value = marker.getLatLng().lat;
        lon_field.value = marker.getLatLng().lng;

       
    });

    btn_findme.addEventListener("click",function(){
        getLocation(); 
       });

});