def test_dashboard_analytics(client):
    client.post('/api/auth/register', json={
        'username': 'analytics_user',
        'email': 'analytics@example.com',
        'password': 'Pass@123',
        'full_name': 'Analytics User'
    })
    client.post('/api/auth/login', json={'username': 'analytics_user', 'password': 'Pass@123'})
    res = client.get('/api/analytics/dashboard')
    assert res.status_code == 200
    assert 'analytics' in res.json
