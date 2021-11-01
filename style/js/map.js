$(function() {
    var map = L.map('map').setView([25.021749, 121.541591], 10);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.geoJSON(FreewayJson, {
        color: "#9999FF"
    }).addTo(map);

    L.geoJSON(points, {
        pointToLayer: function(feature, latlng) {
            roadcode = feature.properties.ROADCODE;
            icon = 'HW' + roadcode + '.png';
            return new L.Marker(latlng, {
                'icon': new L.Icon({
                    iconUrl: 'style/images/freeway-icon/' + icon,
                    iconSize: [25, 25]
                })
            })
        }
    }).addTo(map);
});