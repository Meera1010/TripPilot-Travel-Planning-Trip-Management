class MapEngine {
    constructor(elementId, center = [35.6762, 139.6503], zoom = 5) {
        this.elementId = elementId;
        this.map = L.map(elementId).setView(center, zoom);
        
        // OpenStreetMap Tile Layer
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 18,
            attribution: '© OpenStreetMap contributors'
        }).addTo(this.map);

        this.markers = [];
    }

    addPin(lat, lng, title, popupText = '') {
        const marker = L.marker([lat, lng]).addTo(this.map);
        if (popupText) {
            marker.bindPopup(`<b>${title}</b><br>${popupText}`);
        }
        this.markers.push(marker);
        return marker;
    }

    fitBounds() {
        if (this.markers.length > 0) {
            const group = new L.featureGroup(this.markers);
            this.map.fitBounds(group.getBounds().pad(0.2));
        }
    }
}
