function createMap() {
  if (address) {
    const map = new google.maps.Map(document.getElementById('map'), {
      zoom: 18,
      center: address,
    });
    const marker = new google.maps.Marker({
      position: address,
      map: map,
      animation: google.maps.Animation.DROP,
    });
  }
}
