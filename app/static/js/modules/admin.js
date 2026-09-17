/**
 * Admin Panel & Audit Trail Controller
 */
document.addEventListener('DOMContentLoaded', async () => {
  const tableBody = document.getElementById('audit-logs-tbody');
  if (!tableBody) return;

  try {
    const res = await API.get('/admin/audit-logs');
    if (res.success && res.data.items) {
      tableBody.innerHTML = res.data.items.map(log => `
        <tr>
          <td><span class="audit-action-tag">${log.action}</span></td>
          <td><strong>${log.username}</strong></td>
          <td>${log.entity_type}</td>
          <td>${log.entity_id || '-'}</td>
          <td>${log.ip_address}</td>
          <td style="font-size:0.8rem;color:var(--text-muted);">${new Date(log.timestamp).toLocaleString()}</td>
        </tr>
      `).join('');
    }
  } catch (err) {
    console.error('Error loading audit logs:', err);
  }
});
