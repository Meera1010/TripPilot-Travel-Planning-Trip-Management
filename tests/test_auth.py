def test_register_user(client):
    res = client.post('/api/auth/register', json={
        'username': 'new_traveler_101',
        'email': 'new101@example.com',
        'password': 'Password@123',
        'full_name': 'New Traveler'
    })
    assert res.status_code == 201

def test_login_success(client):
    client.post('/api/auth/register', json={
        'username': 'alex_login',
        'email': 'alex_login@example.com',
        'password': 'Traveler@123',
        'full_name': 'Alex Login'
    })
    res = client.post('/api/auth/login', json={
        'username': 'alex_login',
        'password': 'Traveler@123'
    })
    assert res.status_code == 200

def test_login_invalid_password(client):
    res = client.post('/api/auth/login', json={
        'username': 'non_existent_user',
        'password': 'WrongPassword'
    })
    assert res.status_code == 401
