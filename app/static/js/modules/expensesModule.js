document.addEventListener('DOMContentLoaded', async () => {
    try {
        const tripsData = await API.get('/api/trips');
        if (tripsData.trips && tripsData.trips.length > 0) {
            const tripId = tripsData.trips[0].id;
            loadExpenses(tripId);
        }
    } catch (err) {
        console.error('Expenses error:', err);
    }

    async function loadExpenses(tripId) {
        try {
            const data = await API.get(`/api/expenses/trip/${tripId}`);
            document.getElementById('exp-total').textContent = `$${data.total_spent.toFixed(2)}`;
            document.getElementById('exp-user-share').textContent = `$${(data.total_spent / 2).toFixed(2)}`;

            const tbody = document.getElementById('expenses-tbody');
            if (data.expenses && data.expenses.length > 0) {
                tbody.innerHTML = data.expenses.map(e => `
                    <tr>
                        <td>${e.date}</td>
                        <td><strong>${e.title}</strong></td>
                        <td><span class="badge" style="background:var(--bg-input);">${e.category}</span></td>
                        <td>${e.paid_by_name}</td>
                        <td>$${e.amount.toFixed(2)}</td>
                    </tr>
                `).join('');
            } else {
                tbody.innerHTML = '<tr><td colspan="5" style="text-align:center; color:var(--text-muted);">No expenses logged yet.</td></tr>';
            }

            const settlementsContainer = document.getElementById('settlements-container');
            if (data.settlements && data.settlements.length > 0) {
                document.getElementById('exp-settlements-count').textContent = `${data.settlements.length} Outstanding`;
                settlementsContainer.innerHTML = data.settlements.map(s => `
                    <div style="padding:12px; border:1px solid var(--border-color); border-radius:var(--radius-md); margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <strong>${s.from_user_name}</strong> owes <strong>${s.to_user_name}</strong>
                        </div>
                        <span style="color:var(--accent-green); font-weight:700;">$${s.amount.toFixed(2)}</span>
                    </div>
                `).join('');
            } else {
                document.getElementById('exp-settlements-count').textContent = '0 Outstanding';
                settlementsContainer.innerHTML = '<div style="color:var(--text-muted); font-size:13px;">All group debts are completely settled! 🎉</div>';
            }
        } catch (err) {
            console.error('Error loading expenses:', err);
        }
    }
});
