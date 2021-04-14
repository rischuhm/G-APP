function getLocation() {
    navigator.geolocation.getCurrentPosition(updateMarker);
}

function updateMarker(position) {
    address_field = document.getElementById("address");
    marker = getMarker();
    map = getMap();
    lat = position.coords.latitude;
    lon = position.coords.longitude;
    var L = window.L;
    var l = L.latLng(lat, lon);

    map.setView(l, 15)
    marker.setLatLng(l);

    
    lat_field = document.getElementsByName("lat")[0]
    lon_field = document.getElementsByName("lon")[0]

    lat_field.value = marker.getLatLng().lat;
    lon_field.value = marker.getLatLng().lng;

    catchAddressData(address_field,lat_field.value,lon_field.value)


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

function catchAddressData(address_field,lat,lon){
    fetch('https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat='+lat+"&lon="+lon)
    .then(response => response.json())
    .then(data => address_field.innerHTML = data.address.road +" "+ (data.address.house_number ? data.address.house_number:"")   );

}


window.addEventListener('load', function () {
    btn_findme = document.getElementById("findme");
    address_field = document.getElementById("address");
    marker = getMarker();

    lat_field = document.getElementsByName("lat")[0]
    lon_field = document.getElementsByName("lon")[0]

    lat_field.value = marker.getLatLng().lat;
    lon_field.value = marker.getLatLng().lng;


    marker.addEventListener("dragend", function () {
        addr_text = document.getElementById("address-text");
        addr_text.classList.remove("d-none");
        lat_field.value = marker.getLatLng().lat;
        lon_field.value = marker.getLatLng().lng;
        catchAddressData(address_field,lat_field.value,lon_field.value)

        

    });

    btn_findme.addEventListener("click", function () {
        addr_text = document.getElementById("address-text");
        addr_text.classList.remove("d-none");
        getLocation();
        
        
    });

});