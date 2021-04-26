window.addEventListener('load', function () {

    function getLocation() {
        navigator.geolocation.getCurrentPosition(updateMarker);
    }

    function updateMarker(position) {
        address_field = document.getElementById("address");
        lat = position.coords.latitude;
        lon = position.coords.longitude;
        // var L = window.L;
        var l = L.latLng(lat, lon);

        map.setView(l, 15)
        myMarker.setLatLng(l);


        lat_field = document.getElementsByName("lat")[0]
        lon_field = document.getElementsByName("lon")[0]

        lat_field.value = myMarker.getLatLng().lat;
        lon_field.value = myMarker.getLatLng().lng;
    };

    function getMap() {
        for (obj of Object.keys(window.window["0"])) {
            if (obj.includes("map_")) {
                return window.window["0"][obj]
            }
        }
    };


    var lat = 51.3396955
    var lon = 12.3730747
    var map = L.map('mappid').setView([lat, lon], 12);





    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>'
    }).addTo(map);

    var redMarker = L.AwesomeMarkers.icon({
        icon: 'trash',
        markerColor: 'red',
        prefix: "bi"
    });

    var blueMarker = L.AwesomeMarkers.icon({
        icon: 'trash',
        markerColor: 'blue',
        prefix: "bi"
    });


    myMarker = L.marker([lat, lon], { draggable: true, autoPan: true,icon: redMarker,zIndexOffset:10000 });
    myMarker.addTo(map);

    fetch('fetch')
  .then(response => response.json())
  .then(function(response){
         const obj = JSON.parse(response);
         for (let o of obj){
            L.marker([o.fields.lat, o.fields.lon], {icon: blueMarker }).addTo(map);
         }
  });


    btn_findme = document.getElementById("findme");

    lat_field = document.getElementsByName("lat")[0]
    lon_field = document.getElementsByName("lon")[0]


    myMarker.addEventListener("dragend", function () {
        lat_field.value = this.getLatLng().lat;
        lon_field.value = this.getLatLng().lng;
    });

    btn_findme.addEventListener("click", function () {
        getLocation();
    });

});