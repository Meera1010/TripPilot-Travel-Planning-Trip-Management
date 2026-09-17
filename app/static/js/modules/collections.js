/**
 * Collections & Runway Show Module Controller
 */
document.addEventListener('DOMContentLoaded', async () => {
  const container = document.getElementById('collections-grid');
  if (!container) return;

  loadCollections();

  const createForm = document.getElementById('create-collection-form');
  if (createForm) {
    createForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const payload = {
        name: createForm.name.value,
        season: createForm.season.value,
        year: createForm.year.value,
        theme: createForm.theme.value,
        description: createForm.description.value
      };

      try {
        const res = await API.post('/collections', payload);
        if (res.success) {
          showToast('Collection created successfully', 'success');
          closeModal('modal-new-collection');
          loadCollections();
        }
      } catch (err) {
        showToast('Failed to create collection', 'error');
      }
    });
  }
});

async function loadCollections() {
  const container = document.getElementById('collections-grid');
  try {
    const res = await API.get('/collections');
    if (res.success && res.data.items) {
      container.innerHTML = res.data.items.map(c => `
        <div class="card">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
            <span class="badge badge-approved">${c.season} ${c.year}</span>
            <span style="font-size:0.8rem;color:var(--text-muted);">${c.code}</span>
          </div>
          <h3 style="font-size:1.15rem;font-weight:700;margin-bottom:6px;">${c.name}</h3>
          <p style="font-size:0.85rem;color:var(--text-secondary);margin-bottom:16px;">${c.description}</p>
          <div style="display:flex;justify-content:space-between;align-items:center;padding-top:12px;border-top:1px solid var(--border-color);">
            <span style="font-size:0.8rem;color:var(--text-muted);">${c.design_count} Designs</span>
            <span style="font-size:0.85rem;font-weight:600;color:var(--accent-gold);">$${c.total_budget.toLocaleString()}</span>
          </div>
        </div>
      `).join('');
    }
  } catch (err) {
    console.error('Error loading collections:', err);
  }
}
