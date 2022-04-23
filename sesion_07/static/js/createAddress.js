let autocomplete
const address = {}
const form = document.querySelector('#hidden-form')
const button = document.querySelector('#submit-button')
const mapInput = document.querySelector("#map")

mapInput.style.display = 'none'

async function getCurrentPosition() {
  return new Promise(resolve => {
    const center = {};
    if ('geolocation' in navigator) {
      navigator.geolocation.getCurrentPosition(
        position => {
          center.lat = position.coords.latitude;
          center.lng = position.coords.longitude;
          resolve(center);
        }, // Success
        () => {
          center.lat = 19.432608;
          center.lng = -99.133209;
          resolve(center);
        } // El usuario me impidió la localización
      );
    } else {
      center.lat = 19.432608;
      center.lng = -99.133209;
      resolve(center);
    } // El usuario no tiene geolocalización
  });
}

async function startAutocomplete() {
  const center = await getCurrentPosition();
  // Create a bounding box with sides ~10km away from the center point
  const defaultBounds = {
    north: center.lat + 0.1,
    south: center.lat - 0.1,
    east: center.lng + 0.1,
    west: center.lng - 0.1,
  };
  const input = document.querySelector('#autocomplete-id');
  const options = {
    bounds: defaultBounds,
    componentRestrictions: { country: 'mx' },
    fields: ['address_components', 'geometry', 'formatted_address'],
    strictBounds: false,
    types: ['address'],
  };

  autocomplete = new google.maps.places.Autocomplete(input, options);
  autocomplete.addListener('place_changed', onPlaceChanged);
}

function onPlaceChanged() {
  let place = autocomplete.getPlace();
  for (const component of place.address_components) {
    const componentType = component.types[0];
    switch (componentType) {
      case 'route':
        address.street = component.long_name;
        break;
      case 'street_number':
        address.number = component.long_name;
        break;
      case 'postal_code':
        address.zipCode = component.long_name;
        break;
      case 'sublocality_level_1':
        address.suburb = component.long_name;
        break;
      case 'locality':
        address.city = component.long_name;
        break;
      case 'administrative_area_level_1':
        address.state = component.long_name;
        break;
      case 'country':
        address.country = component.long_name;
    }
  }

  address.lat = place.geometry.location.lat();
  address.lng = place.geometry.location.lng();

  address.fullAddress = place.formatted_address

  button.disabled = false;

  const map = new google.maps.Map(mapInput, {
    zoom: 18,
    center: address,
  });
  const marker = new google.maps.Marker({
    position: address,
    map: map,
    draggable: true,
    animation: google.maps.Animation.DROP,
  });

  mapInput.style.display = 'block'
  button.classList.add('mt-4')

  marker.addListener('click', () => {
    const infoWindow = new google.maps.InfoWindow({
      content: address.fullAddress
    });
    infoWindow.open({
      anchor: marker,
      map: map,
      shouldFocus: false,
    })
  })

  marker.addListener('drag', event => {
    address.lat = event.latLng.lat()
    address.lng = event.latLng.lng()
  })
}


function createAddress() {
  streetInput = form.querySelector('#street-id')
  numberInput = form.querySelector('#number-id')
  zipCodeInput = form.querySelector('#zip-code-id')
  suburbInput = form.querySelector('#suburb-id')
  cityInput = form.querySelector('#city-id')
  stateInput = form.querySelector('#state-id')
  countryInput = form.querySelector('#country-id')
  latitudeInput = form.querySelector('#latitude-id')
  longitudeInput = form.querySelector('#longitude-id')

  streetInput.value = address.street
  numberInput.value = address.number
  zipCodeInput.value = address.zipCode
  suburbInput.value = address.suburb
  cityInput.value = address.city
  stateInput.value = address.state
  countryInput.value = address.country
  latitudeInput.value = address.lat
  longitudeInput.value = address.lng

  form.submit()
}

button.addEventListener('click', createAddress)
