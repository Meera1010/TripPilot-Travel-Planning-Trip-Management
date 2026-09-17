document.addEventListener('DOMContentLoaded', async () => {
    const container = document.getElementById('journal-feed-container');

    try {
        const tripsData = await API.get('/api/trips');
        if (tripsData.trips && tripsData.trips.length > 0) {
            const tripId = tripsData.trips[0].id;
            const journalData = await API.get(`/api/journal/trip/${tripId}`);

            if (journalData.entries && journalData.entries.length > 0) {
                container.innerHTML = journalData.entries.map(e => `
                    <div class="card" style="padding:20px; margin-bottom:20px;">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                            <h4>${e.title}</h4>
                            <span class="badge" style="background:var(--bg-input);">${e.entry_date}</span>
                        </div>
                        <p style="color:var(--text-secondary);">${e.content}</p>
                        <div style="margin-top:12px; font-size:13px; color:var(--text-muted);">
                            📍 Location: ${e.location} • Mood: ${e.mood} 😊
                        </div>
                    </div>
                `).join('');
            } else {
                container.innerHTML = '<div class="empty-state">No journal entries logged yet for this trip.</div>';
            }
        }
    } catch (err) {
        console.error('Journal error:', err);
    }
});
