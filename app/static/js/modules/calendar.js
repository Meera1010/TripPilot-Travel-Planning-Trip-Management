/**
 * Fashion Calendar & Production Task List Module Controller
 */
document.addEventListener('DOMContentLoaded', async () => {
  const container = document.getElementById('calendar-events-list');
  if (!container) return;

  try {
    const res = await API.get('/calendar/events');
    if (res.success && res.data) {
      container.innerHTML = res.data.map(e => `
        <div class="card" style="margin-bottom:16px;border-left:4px solid ${e.color_tag};">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
            <span class="badge badge-approved">${e.event_type.toUpperCase()}</span>
            <span style="font-size:0.8rem;color:var(--text-muted);">${new Date(e.start_date).toLocaleDateString()}</span>
          </div>
          <h3 style="font-size:1.1rem;font-weight:600;">${e.title}</h3>
          <p style="font-size:0.85rem;color:var(--text-secondary);">${e.description || 'No description'}</p>
          <span style="font-size:0.8rem;color:var(--text-muted);display:block;margin-top:8px;">Location: ${e.location || 'Atelier'}</span>
        </div>
      `).join('');
    }
  } catch (err) {
    console.error('Error loading calendar events:', err);
  }
});
