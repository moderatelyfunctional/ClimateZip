function initMap() {
	const currLatLon = {lat: curr_lat, lng: curr_lon};
	const futureLatLon = {lat: future_lat, lng: future_lon};
	const center = {lat: (curr_lat + future_lat) / 2, lng: (curr_lon + future_lon) / 2}
	map = new google.maps.Map(document.getElementById('map'), {
		center: center,
		zoom: 6
	});

	var marker = new google.maps.Marker({
		position: currLatLon,
		map: map,
		title: 'Curr Location'
	});

	var other_marker = new google.maps.Marker({
		position: futureLatLon,
		map: map,
		title: 'Future Location'
	});
}