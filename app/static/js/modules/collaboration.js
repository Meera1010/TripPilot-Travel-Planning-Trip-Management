/**
 * Team Workspace & Comments Module Controller
 */
document.addEventListener('DOMContentLoaded', async () => {
  const container = document.getElementById('collab-wrapper');
  if (!container) return;

  loadTeamMembers();
  loadActivityFeed();
});

async function loadTeamMembers() {
  const listEl = document.getElementById('team-members-list');
  if (!listEl) return;

  try {
    const res = await API.get('/collaboration/teams');
    if (res.success && res.data) {
      listEl.innerHTML = (res.data[0]?.members || []).map(m => `
        <div style="display:flex;align-items:center;justify-content:space-between;padding:12px;border-bottom:1px solid var(--border-color);">
          <div style="display:flex;align-items:center;gap:12px;">
            <div style="width:36px;height:36px;border-radius:50%;background:var(--accent-primary);display:flex;align-items:center;justify-content:center;font-weight:700;">
              ${m.full_name.charAt(0)}
            </div>
            <div>
              <strong style="display:block;font-size:0.9rem;">${m.full_name}</strong>
              <span style="font-size:0.75rem;color:var(--text-muted);">@${m.username}</span>
            </div>
          </div>
          <span class="badge badge-approved">${m.role}</span>
        </div>
      `).join('');
    }
  } catch (err) {
    console.error('Error loading team members:', err);
  }
}

async function loadActivityFeed() {
  const feedEl = document.getElementById('activity-feed-list');
  if (!feedEl) return;

  try {
    const res = await API.get('/collaboration/activity');
    if (res.success && res.data) {
      feedEl.innerHTML = res.data.map(a => `
        <div style="padding:12px 0;border-bottom:1px solid var(--border-color);font-size:0.85rem;">
          <strong>${a.user_name}</strong> ${a.description}
          <span style="display:block;font-size:0.75rem;color:var(--text-muted);margin-top:4px;">${new Date(a.timestamp).toLocaleString()}</span>
        </div>
      `).join('');
    }
  } catch (err) {
    console.error('Error loading activity feed:', err);
  }
}
