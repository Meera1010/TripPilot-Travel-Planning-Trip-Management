from app.services.packing_optimizer import PackingOptimizerService

def test_packing_optimizer_recommendations():
    recs = PackingOptimizerService.generate_packing_recommendations('warm', 7)
    assert len(recs) >= 5
    assert any(i['item_name'] == 'Passport & Physical Visa Copies' for i in recs)
