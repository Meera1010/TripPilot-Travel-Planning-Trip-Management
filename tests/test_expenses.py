from app.services.expense_splitter import ExpenseSplitterService

def test_expense_splitting_graph_solver():
    balances = {1: 150.0, 2: -100.0, 3: -50.0}
    settlements = ExpenseSplitterService.simplify_debts(balances)
    assert len(settlements) == 2
    assert settlements[0]['amount'] == 100.0
    assert settlements[1]['amount'] == 50.0

def test_get_expenses(client):
    client.post('/api/auth/register', json={
        'username': 'exp_user',
        'email': 'exp@example.com',
        'password': 'Pass@123',
        'full_name': 'Expense User'
    })
    client.post('/api/auth/login', json={'username': 'exp_user', 'password': 'Pass@123'})
    trip_res = client.post('/api/trips', json={
        'title': 'Bali Getaway',
        'primary_destination': 'Bali',
        'start_date': '2026-07-01',
        'end_date': '2026-07-07'
    })
    trip_id = trip_res.json['trip']['id']
    res = client.get(f'/api/expenses/trip/{trip_id}')
    assert res.status_code == 200
    assert 'expenses' in res.json
    assert 'settlements' in res.json
