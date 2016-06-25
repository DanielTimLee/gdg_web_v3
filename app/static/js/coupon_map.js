$(document).ready(function() {

    function initialize() {

      var company = $('#company-data').data('company');
      var company_addr = $('#company-data').data('company-addr');
      var company_phone = $('#company-data').data('company-phone');
      var company_open_hour = $('#company-data').data('company-open_hour');
      var company_desc = $('#company-data').data('company-desc');
      if ($("#google_map").length) {

        var mapOptions = { //구글 맵 옵션 설정
          zoom: 16, //기본 확대율
          scrollwheel: false, //마우스 휠로 확대 축소 사용 여부
          mapTypeControl: false //맵 타입 컨트롤 사용 여부
        };

        var map = new google.maps.Map(document.getElementById('google_map'), mapOptions); //구글 맵을 사용할 타겟

        var address = company_addr; // DB에서 주소 가져와서 검색하거나 왼쪽과 같이 주소를 바로 코딩.
        var marker = null;
        var geocoder = new google.maps.Geocoder();
        geocoder.geocode( { 'address': address}, function(results, status) {
          if (status == google.maps.GeocoderStatus.OK) {
            map.setCenter(results[0].geometry.location);
            marker = new google.maps.Marker({
              map: map,
              position: results[0].geometry.location
            });

            infowindow = new google.maps.InfoWindow({
              content: '<h4>'+ company +'</h4>' +
              company_desc+'<br>' +
              company_phone+'<br>' +
              '<br>'+company_addr+'<br>'
            });

            infowindow.open(map, marker);

          } else {
            alert("Geocode was not successful for the following reason: " + status);
          }
        });

        google.maps.event.addDomListener(window, "resize", function () { //리사이즈에 따른 마커 위치
          var center = map.getCenter();
          google.maps.event.trigger(map, "resize");
          map.setCenter(center);
        });
      }//if-end
    }//function-end
    google.maps.event.addDomListener(window, 'load', initialize);
  }
);
