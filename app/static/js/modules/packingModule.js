document.addEventListener('DOMContentLoaded', async () => {
    const container = document.getElementById('packing-lists-container');
    const autoPackBtn = document.getElementById('btn-auto-pack');

    async function loadPackingRecommendations() {
        try {
            const data = await API.post('/api/packing/recommend', { climate: 'warm', duration_days: 7 });
            if (data.recommendations) {
                container.innerHTML = `
                    <div class="card" style="padding:20px; grid-column: span 2;">
                        <h3>✨ Smart Auto-Generated Packing Checklist</h3>
                        <div style="display:grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap:12px; margin-top:16px;">
                            ${data.recommendations.map(item => `
                                <div style="display:flex; align-items:center; gap:10px; padding:10px; background:var(--bg-secondary); border-radius:var(--radius-md);">
                                    <input type="checkbox">
                                    <span>${item.item_name} (x${item.quantity})</span>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `;
            }
        } catch (err) {
            console.error('Packing error:', err);
        }
    }

    if (autoPackBtn) {
        autoPackBtn.onclick = loadPackingRecommendations;
    }

    loadPackingRecommendations();
});
