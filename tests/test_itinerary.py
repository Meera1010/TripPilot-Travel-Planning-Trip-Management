def test_get_itinerary(client):
    client.post('/api/auth/register', json={
        'username': 'itin_user',
        'email': 'itin@example.com',
        'password': 'Pass@123',
        'full_name': 'Itin User'
    })
    client.post('/api/auth/login', json={'username': 'itin_user', 'password': 'Pass@123'})
    trip_res = client.post('/api/trips', json={
        'title': 'Kyoto Expedition',
        'primary_destination': 'Kyoto',
        'start_date': '2026-05-01',
        'end_date': '2026-05-05'
    })
    trip_id = trip_res.json['trip']['id']
    res = client.get(f'/api/itineraries/trip/{trip_id}')
    assert res.status_code == 200
    assert 'days' in res.json

def test_add_activity(client):
    client.post('/api/auth/register', json={
        'username': 'itin_user2',
        'email': 'itin2@example.com',
        'password': 'Pass@123',
        'full_name': 'Itin User 2'
    })
    client.post('/api/auth/login', json={'username': 'itin_user2', 'password': 'Pass@123'})
    trip_res = client.post('/api/trips', json={
        'title': 'Osaka Food Run',
        'primary_destination': 'Osaka',
        'start_date': '2026-05-06',
        'end_date': '2026-05-08'
    })
    trip_id = trip_res.json['trip']['id']
    itin_res = client.get(f'/api/itineraries/trip/{trip_id}')
    day_id = itin_res.json['days'][0]['id']

    res = client.post('/api/itineraries/activities', json={
        'day_id': day_id,
        'title': 'Visit Dotonbori',
        'category': 'food',
        'start_time': '18:00',
        'end_time': '20:00',
        'estimated_cost': 35.0
    })
    assert res.status_code == 201
    assert res.json['activity']['title'] == 'Visit Dotonbori'
