document.addEventListener('DOMContentLoaded', async () => {
    try {
        const data = await API.get('/api/analytics/dashboard');
        if (data.analytics && data.analytics.category_breakdown) {
            TravelCharts.renderDonutChart('chart-spend-breakdown', data.analytics.category_breakdown);
        }

        const carbonData = {
            'Short Flight': 255.0,
            'Long Flight': 600.0,
            'High-Speed Train': 35.0,
            'Rental Car': 170.0
        };
        TravelCharts.renderDonutChart('chart-carbon-footprint', carbonData);
    } catch (err) {
        console.error('Analytics error:', err);
    }
});
