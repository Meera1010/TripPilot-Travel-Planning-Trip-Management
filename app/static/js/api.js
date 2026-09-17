const API = {
    async request(endpoint, options = {}) {
        const defaultHeaders = {
            'Content-Type': 'application/json'
        };

        const config = {
            method: options.method || 'GET',
            headers: { ...defaultHeaders, ...options.headers }
        };

        if (options.body) {
            config.body = JSON.stringify(options.body);
        }

        try {
            const response = await fetch(endpoint, config);
            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'API Request Failed');
            }
            return data;
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    },

    get(endpoint) { return this.request(endpoint, { method: 'GET' }); },
    post(endpoint, body) { return this.request(endpoint, { method: 'POST', body }); },
    put(endpoint, body) { return this.request(endpoint, { method: 'PUT', body }); },
    delete(endpoint) { return this.request(endpoint, { method: 'DELETE' }); }
};
