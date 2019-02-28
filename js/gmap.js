function initMap() {
  var Detroit = {lat: 42.35, lng: -83.09},
      Wayne = {lat: 42.24, lng: -83.22},
      Kent = {lat: 43.03, lng: -85.53},
      Muskegon = {lat: 43.30, lng: -86.17},
      Washtenaw = {lat: 42.25, lng: -83.84};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: Wayne,
  });
  // Need to run a simple http server to get loadGeoJson working (python -m http.server 5000)
  map.data.loadGeoJson('../data/geojson/Wayne.geojson');
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
