/**
 * Designer Portfolio Module Controller
 */
document.addEventListener('DOMContentLoaded', async () => {
  const container = document.getElementById('portfolio-items-grid');
  if (!container) return;

  try {
    const res = await API.get('/portfolios/2'); // Sample Sabyasachi Portfolio ID
    if (res.success && res.data) {
      document.getElementById('portfolio-designer-name').textContent = res.data.designer_name;
      document.getElementById('portfolio-bio').textContent = res.data.bio;

      if (res.data.items) {
        container.innerHTML = res.data.items.map(item => `
          <div class="card">
            <div style="height:200px;background:#181924;border-radius:var(--radius-md);margin-bottom:12px;display:flex;align-items:center;justify-content:center;">
              <i class="ph-bold ph-sparkle" style="font-size:3.5rem;color:var(--accent-gold);"></i>
            </div>
            <h3 style="font-size:1.1rem;font-weight:600;margin-bottom:4px;">${item.title}</h3>
            <p style="font-size:0.85rem;color:var(--text-secondary);">${item.category}</p>
            <div style="display:flex;gap:6px;margin-top:12px;">
              ${(item.press_mentions || []).map(p => `<span class="badge badge-approved">${p}</span>`).join('')}
            </div>
          </div>
        `).join('');
      }
    }
  } catch (err) {
    console.error('Error loading portfolio:', err);
  }
});
