  function initMap() {

    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: zoom,
      center: center,
    });
    // Need to run a simple http server to get loadGeoJson working (python -m http.server 5000)
    map.data.loadGeoJson(geojson_file);
    map.data.setStyle({
      fillColor: 'black',
      fillOpacity: 0.1,
      strokeWeight: 3,
    })
    var icon = {
      url: 'https://maps.google.com/mapfiles/kml/paddle/blu-blank.png',
      size: new google.maps.Size(64, 64),
      origin: new google.maps.Point(0, 0),
      anchor: new google.maps.Point(21, 42), // scaledSize coordinates
      scaledSize: new google.maps.Size(42, 42),
    }
    event_pts.forEach((d,i) => {
      var marker = new google.maps.Marker({
        position: new google.maps.LatLng(d.lat, d.lng),
        icon: icon,
        map: map,
        opacity: d.opacity,
      })     
    });
  };

