document.addEventListener('DOMContentLoaded', async () => {
    const tbody = document.getElementById('admin-audit-tbody');

    try {
        const data = await API.get('/api/admin/audit-logs');
        if (data.audit_logs && data.audit_logs.length > 0) {
            tbody.innerHTML = data.audit_logs.map(log => `
                <tr>
                    <td>${log.timestamp}</td>
                    <td>User #${log.user_id}</td>
                    <td><span class="badge" style="background:var(--bg-input); color:var(--accent-blue);">${log.action}</span></td>
                    <td>${log.resource_type} #${log.resource_id}</td>
                    <td>${log.details}</td>
                </tr>
            `).join('');
        } else {
            tbody.innerHTML = '<tr><td colspan="5" style="text-align:center; color:var(--text-muted);">No audit logs available.</td></tr>';
        }
    } catch (err) {
        console.error('Admin logs error:', err);
    }
});
