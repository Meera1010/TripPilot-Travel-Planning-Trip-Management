class TravelCharts {
    static renderDonutChart(containerId, data) {
        const container = document.getElementById(containerId);
        if (!container) return;

        const total = Object.values(data).reduce((acc, val) => acc + val, 0);
        if (total === 0) {
            container.innerHTML = '<div class="empty-state">No chart data available</div>';
            return;
        }

        const colors = ['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6', '#f43f5e', '#14b8a6'];
        let currentAngle = 0;
        let svgPaths = '';
        let legendHtml = '<div class="chart-legend">';

        Object.entries(data).forEach(([key, val], idx) => {
            const pct = val / total;
            const sliceAngle = pct * 360;
            const color = colors[idx % colors.length];

            legendHtml += `
                <div class="legend-item">
                    <span class="legend-dot" style="background:${color};"></span>
                    <span class="legend-label">${key.toUpperCase()}: $${val.toFixed(2)} (${(pct * 100).toFixed(0)}%)</span>
                </div>
            `;
        });
        legendHtml += '</div>';

        container.innerHTML = `
            <div class="donut-chart-wrapper" style="display:flex; align-items:center; gap:20px;">
                <svg viewBox="0 0 100 100" width="160" height="160">
                    <circle cx="50" cy="50" r="40" fill="transparent" stroke="#374151" stroke-width="15"/>
                    <circle cx="50" cy="50" r="40" fill="transparent" stroke="#3b82f6" stroke-width="15" stroke-dasharray="180 250"/>
                </svg>
                ${legendHtml}
            </div>
        `;
    }
}
