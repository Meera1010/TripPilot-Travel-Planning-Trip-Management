document.addEventListener('DOMContentLoaded', async () => {
    const select = document.getElementById('select-active-trip');
    const daysContainer = document.getElementById('itinerary-days-container');

    try {
        const tripsData = await API.get('/api/trips');
        if (tripsData.trips && tripsData.trips.length > 0) {
            select.innerHTML = tripsData.trips.map(t => `<option value="${t.id}">${t.title} (${t.primary_destination})</option>`).join('');
            loadItinerary(tripsData.trips[0].id);
        } else {
            daysContainer.innerHTML = '<div class="empty-state">No trips available for itinerary planning.</div>';
        }
    } catch (err) {
        console.error('Itinerary error:', err);
    }

    async function loadItinerary(tripId) {
        try {
            const data = await API.get(`/api/itineraries/trip/${tripId}`);
            if (data.days && data.days.length > 0) {
                daysContainer.innerHTML = data.days.map(d => `
                    <div class="day-card">
                        <h4>Day ${d.day_number}: ${d.title} (${d.date})</h4>
                        <div class="activities-list">
                            ${d.activities && d.activities.length > 0 ? d.activities.map(a => `
                                <div class="activity-item">
                                    <div>
                                        <strong>${a.title}</strong><br>
                                        <small style="color:var(--text-secondary);">${a.start_time || 'All Day'} • 📍 ${a.location_name || 'Destination'}</small>
                                    </div>
                                    <span class="badge" style="background:var(--bg-input); color:var(--accent-blue);">$${a.estimated_cost}</span>
                                </div>
                            `).join('') : '<small style="color:var(--text-muted);">No activities scheduled for this day yet.</small>'}
                        </div>
                    </div>
                `).join('');

                if (document.getElementById('itinerary-map')) {
                    const mapEngine = new MapEngine('itinerary-map', [35.6762, 139.6503], 12);
                    mapEngine.addPin(35.6586, 139.7454, 'Tokyo Tower', 'Day 1 Sightseeing');
                    mapEngine.addPin(35.7148, 139.7967, 'Senso-ji Temple', 'Day 2 Cultural Heritage');
                    mapEngine.fitBounds();
                }
            }
        } catch (err) {
            console.error('Error loading itinerary:', err);
        }
    }

    if (select) {
        select.onchange = (e) => loadItinerary(e.target.value);
    }
});
