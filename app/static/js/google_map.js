function initMap() {
  var mapDiv = document.getElementById('map-canvas');
  var map = new google.maps.Map(mapDiv, {
    center: {lat: 37.494331, lng: 126.959300},
    zoom: 17
  });

  var markLocation = new google.maps.LatLng('37.494331', '126.959300');
  var size_x = 60;
  var size_y = 60;
  var marker;
  marker = new google.maps.Marker({
    position: markLocation,
    map: map,
    info: 'GDG SSU',
    title: 'GDG SSU'
  });
}
