/**
 * SaaS Dashboard Module Controller
 */
document.addEventListener('DOMContentLoaded', async () => {
  const overviewContainer = document.getElementById('dashboard-overview');
  if (!overviewContainer) return;

  try {
    const metricsRes = await API.get('/analytics/dashboard');
    const designsRes = await API.get('/designs?page=1');

    if (metricsRes.success) {
      const overview = metricsRes.data.overview;
      document.getElementById('stat-total-designs').textContent = overview.total_designs || 0;
      document.getElementById('stat-total-collections').textContent = overview.total_collections || 0;
      document.getElementById('stat-total-fabrics').textContent = overview.total_fabrics || 0;
      document.getElementById('stat-low-stock').textContent = overview.low_stock_alerts || 0;

      // Render Charts
      ChartEngine.renderDonutChart('status-chart', metricsRes.data.statusBreakdown);
      ChartEngine.renderBarChart('category-chart', metricsRes.data.categoryDistribution);
    }

    if (designsRes.success && designsRes.data.items) {
      renderRecentDesigns(designsRes.data.items);
    }
  } catch (err) {
    console.error('Dashboard load error:', err);
  }
});

function renderRecentDesigns(designs) {
  const container = document.getElementById('recent-designs-grid');
  if (!container) return;

  if (designs.length === 0) {
    container.innerHTML = '<div style="color:var(--text-muted);grid-column:1/-1;">No designs created yet. Click "New Outfit Design" to begin!</div>';
    return;
  }

  container.innerHTML = designs.slice(0, 6).map(d => `
    <div class="card" onclick="window.location.href='/studio?id=${d.id}'" style="cursor:pointer;">
      <div style="height:140px;background:#181924;border-radius:var(--radius-md);margin-bottom:12px;display:flex;align-items:center;justify-content:center;">
        <i class="ph-bold ph-coat-hanger" style="font-size:3rem;color:var(--text-muted);"></i>
      </div>
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
        <span class="badge badge-${d.status}">${d.status}</span>
        <span style="font-size:0.75rem;color:var(--text-muted);">${d.category.toUpperCase()}</span>
      </div>
      <h4 style="font-size:1rem;font-weight:600;margin-bottom:4px;">${d.title}</h4>
      <p style="font-size:0.8rem;color:var(--text-secondary);">${d.author_name}</p>
    </div>
  `).join('');
}
