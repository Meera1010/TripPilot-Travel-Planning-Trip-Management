/**
 * SaaS Analytics Page Module Controller
 */
document.addEventListener('DOMContentLoaded', async () => {
  const container = document.getElementById('analytics-page-wrapper');
  if (!container) return;

  try {
    const res = await API.get('/analytics/dashboard');
    if (res.success && res.data) {
      ChartEngine.renderDonutChart('analytics-status-chart', res.data.statusBreakdown);
      ChartEngine.renderBarChart('analytics-category-chart', res.data.categoryDistribution, '#3a86ff');
    }
  } catch (err) {
    console.error('Error loading analytics page metrics:', err);
  }
});
