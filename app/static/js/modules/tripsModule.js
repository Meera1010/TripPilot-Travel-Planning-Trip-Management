document.addEventListener('DOMContentLoaded', () => {
    const grid = document.getElementById('trips-grid-container');
    const modal = document.getElementById('create-trip-modal');
    const openBtn = document.getElementById('btn-open-create-modal');
    const closeBtn = document.getElementById('close-trip-modal');
    const cancelBtn = document.getElementById('btn-cancel-trip');
    const form = document.getElementById('form-create-trip');

    async function loadTrips() {
        try {
            const data = await API.get('/api/trips');
            if (data.trips && data.trips.length > 0) {
                grid.innerHTML = data.trips.map(t => `
                    <div class="trip-card">
                        <div class="trip-card-cover" style="background-image: url('${t.cover_image_url}'); background-color: var(--bg-card-hover);">
                            <span class="badge badge-${t.status}" style="position:absolute; top:12px; right:12px;">${t.status}</span>
                        </div>
                        <div class="trip-card-content">
                            <h4 class="trip-card-title">${t.title}</h4>
                            <div class="trip-meta">
                                <span>📍 ${t.primary_destination}</span>
                                <span>⏳ ${t.duration_days} Days</span>
                            </div>
                            <div class="trip-meta" style="margin-top:4px;">
                                <span>💰 Budget: $${t.total_budget}</span>
                                <span>📅 ${t.start_date}</span>
                            </div>
                        </div>
                    </div>
                `).join('');
            } else {
                grid.innerHTML = '<div class="empty-state">No trips planned yet. Click "+ Create New Trip" to get started!</div>';
            }
        } catch (err) {
            console.error('Error loading trips:', err);
        }
    }

    if (openBtn) openBtn.onclick = () => modal.style.display = 'flex';
    if (closeBtn) closeBtn.onclick = () => modal.style.display = 'none';
    if (cancelBtn) cancelBtn.onclick = () => modal.style.display = 'none';

    if (form) {
        form.onsubmit = async (e) => {
            e.preventDefault();
            const payload = {
                title: document.getElementById('trip-title').value,
                primary_destination: document.getElementById('trip-destination').value,
                start_date: document.getElementById('trip-start-date').value,
                end_date: document.getElementById('trip-end-date').value,
                currency: document.getElementById('trip-currency').value,
                total_budget: document.getElementById('trip-budget').value
            };

            try {
                await API.post('/api/trips', payload);
                modal.style.display = 'none';
                loadTrips();
            } catch (err) {
                alert(err.message || 'Failed to create trip');
            }
        };
    }

    loadTrips();
});
