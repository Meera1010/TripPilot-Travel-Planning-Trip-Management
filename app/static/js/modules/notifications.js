/**
 * Topbar Notification Center Controller
 */
document.addEventListener('DOMContentLoaded', async () => {
  const notifContainer = document.getElementById('notif-badge-count');
  if (!notifContainer) return;

  try {
    const res = await API.get('/notifications');
    if (res.success && res.data) {
      const count = res.data.unread_count || 0;
      notifContainer.textContent = count;
      notifContainer.style.display = count > 0 ? 'inline-flex' : 'none';
      renderNotificationDropdown(res.data.notifications);
    }
  } catch (err) {
    console.error('Notification load error:', err);
  }
});

function renderNotificationDropdown(notifications) {
  const listEl = document.getElementById('notif-dropdown-list');
  if (!listEl) return;

  if (notifications.length === 0) {
    listEl.innerHTML = '<div style="padding:16px;text-align:center;color:var(--text-muted);font-size:0.85rem;">No notifications</div>';
    return;
  }

  listEl.innerHTML = notifications.slice(0, 5).map(n => `
    <div style="padding:12px 16px;border-bottom:1px solid var(--border-color);${!n.is_read ? 'background:rgba(230,57,70,0.05);' : ''}">
      <strong style="font-size:0.85rem;display:block;margin-bottom:2px;">${n.title}</strong>
      <p style="font-size:0.8rem;color:var(--text-secondary);margin:0;">${n.message}</p>
    </div>
  `).join('');
}
