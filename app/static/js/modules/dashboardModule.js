document.addEventListener('DOMContentLoaded', async () => {
    try {
        const data = await API.get('/api/analytics/dashboard');
        const stats = data.analytics;

        document.getElementById('stat-active-trips').textContent = stats.total_trips;
        document.getElementById('stat-total-spent').textContent = `$${stats.total_spent_usd.toFixed(2)}`;
        document.getElementById('stat-destinations').textContent = stats.completed_trips + 2;
        document.getElementById('stat-co2').textContent = `${(stats.total_spent_usd * 0.15).toFixed(1)} kg`;

        // Load trips list
        const tripsData = await API.get('/api/trips');
        const container = document.getElementById('dashboard-trips-container');
        if (tripsData.trips && tripsData.trips.length > 0) {
            container.innerHTML = tripsData.trips.map(t => `
                <div class="trip-item-preview" style="padding:12px 0; border-bottom:1px solid var(--border-color); display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <strong>${t.title}</strong><br>
                        <small style="color:var(--text-secondary);">${t.primary_destination} • ${t.duration_days} Days</small>
                    </div>
                    <span class="badge badge-${t.status}">${t.status}</span>
                </div>
            `).join('');
        } else {
            container.innerHTML = '<div class="empty-state">No active trips found. Create one to get started!</div>';
        }

        // Initialize Map
        if (document.getElementById('dashboard-map')) {
            const mapEngine = new MapEngine('dashboard-map', [35.6762, 139.6503], 3);
            mapEngine.addPin(35.6762, 139.6503, 'Tokyo', 'Tokyo Cherry Blossom Expedition');
            mapEngine.addPin(48.8566, 2.3522, 'Paris', 'EuroTrip Summer');
            mapEngine.addPin(27.9881, 86.9250, 'Everest Base Camp', 'Himalayan Trekking Run');
            mapEngine.fitBounds();
        }
    } catch (err) {
        console.error('Dashboard load error:', err);
    }
});
