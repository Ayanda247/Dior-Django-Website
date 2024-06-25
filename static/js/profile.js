// Initialize and display the map with nearby Dior stores
function initMap() {
    // Default location (replace with user's geolocation if available)
    const userLocation = { lat: 40.7128, lng: -74.006 };

    // Create the map centered at user's location
    const map = new google.maps.Map(document.getElementById("map"), {
        center: userLocation,
        zoom: 12,  // Zoom level for map
    });

    // Add markers for Dior stores (replace with actual store locations)
    const diorStores = [
        { lat: 40.7128, lng: -74.006, name: "Dior Store - New York" },
        { lat: 34.0522, lng: -118.2437, name: "Dior Store - Los Angeles" },
        { lat: 51.5074, lng: -0.1278, name: "Dior Store - London" },
        // Add more store locations as needed
    ];

    diorStores.forEach(store => {
        new google.maps.Marker({
            position: { lat: store.lat, lng: store.lng },
            map: map,
            title: store.name
        });
    });
}
