def test_list_trips(client):
    client.post('/api/auth/register', json={
        'username': 'trip_user1',
        'email': 'trip1@example.com',
        'password': 'Pass@123',
        'full_name': 'Trip User 1'
    })
    client.post('/api/auth/login', json={'username': 'trip_user1', 'password': 'Pass@123'})
    client.post('/api/trips', json={
        'title': 'Tokyo Run',
        'primary_destination': 'Tokyo',
        'start_date': '2026-04-01',
        'end_date': '2026-04-10'
    })
    res = client.get('/api/trips')
    assert res.status_code == 200
    assert 'trips' in res.json

def test_create_trip(client):
    client.post('/api/auth/register', json={
        'username': 'trip_user2',
        'email': 'trip2@example.com',
        'password': 'Pass@123',
        'full_name': 'Trip User 2'
    })
    client.post('/api/auth/login', json={'username': 'trip_user2', 'password': 'Pass@123'})
    res = client.post('/api/trips', json={
        'title': 'EuroTrip Summer 2026',
        'primary_destination': 'Paris, France',
        'start_date': '2026-06-01',
        'end_date': '2026-06-15',
        'currency': 'EUR',
        'total_budget': 4000.0
    })
    assert res.status_code == 201
    assert res.json['trip']['title'] == 'EuroTrip Summer 2026'
