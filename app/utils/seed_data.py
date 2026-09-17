from datetime import datetime, timedelta
from app.models import (
    db, User, Role, UserPreference, GarmentTemplate, Fabric, Material, Supplier,
    Collection, RunwayShow, Design, DesignVersion, CanvasLayer, CostingSheet, CostItem,
    SpecSheet, MeasurementProfile, Moodboard, MoodboardAsset, ColorPalette, Sketchbook,
    SketchPage, SketchAnnotation, ApprovalWorkflow, ApprovalStep, StatusHistory, Team,
    TeamMember, Workspace, SharedDesign, DesignComment, ActivityFeed, CalendarEvent,
    TaskItem, Portfolio, PortfolioItem, Notification, NotificationPreference, AnalyticsSnapshot
)
from app.utils.svg_library import SVG_GARMENTS, SVG_ACCESSORIES
from app.services.costing_engine import CostingEngineService
from app.services.sizing_engine import SizingEngineService

def seed_database():
    """Populate database with comprehensive fashion design SaaS seed data."""
    
    # 1. Roles
    admin_role = Role(name='admin', description='System Administrator', permissions={'all': True})
    lead_role = Role(name='lead_designer', description='Lead Fashion Designer', permissions={'approve': True, 'edit': True})
    designer_role = Role(name='designer', description='Fashion Designer', permissions={'edit': True})
    prod_role = Role(name='production_manager', description='Production & Inventory Manager', permissions={'inventory': True, 'costing': True})
    client_role = Role(name='client', description='Client & Reviewer', permissions={'view': True, 'comment': True})

    db.session.add_all([admin_role, lead_role, designer_role, prod_role, client_role])
    db.session.flush()

    # 2. Users
    admin = User(username='admin', email='admin@styleforge.com', full_name='Elena Rostova (Admin)', role='admin', brand_name='StyleForge HQ')
    admin.set_password('Admin@123')

    lead_designer = User(username='sabyasachi', email='sabya@styleforge.com', full_name='Sabyasachi Mukherjee', role='lead_designer', brand_name='Sabyasachi Atelier', bio='Master Couture Designer specializing in royal bridal heritage.')
    lead_designer.set_password('Sabya@123')

    designer_2 = User(username='aria', email='aria@styleforge.com', full_name='Aria Vance', role='designer', brand_name='Vance Haute Couture', bio='Contemporary eveningwear specialist.')
    designer_2.set_password('Aria@123')

    prod_mgr = User(username='marcus', email='marcus@styleforge.com', full_name='Marcus Sterling', role='production_manager', brand_name='Sterling Garments', bio='Production director managing fabric supply chains.')
    prod_mgr.set_password('Marcus@123')

    client_user = User(username='sophia', email='sophia@styleforge.com', full_name='Sophia Laurent', role='client', brand_name='Laurent Luxury', bio='Bespoke haute couture client.')
    client_user.set_password('Sophia@123')

    db.session.add_all([admin, lead_designer, designer_2, prod_mgr, client_user])
    db.session.flush()

    # Add preferences
    for u in [admin, lead_designer, designer_2, prod_mgr, client_user]:
        pref = UserPreference(user_id=u.id, theme='dark', default_currency='USD', measurement_unit='inches')
        notif_pref = NotificationPreference(user_id=u.id)
        db.session.add_all([pref, notif_pref])

    # 3. Garment Templates
    for key, g in SVG_GARMENTS.items():
        tmpl = GarmentTemplate(
            name=g['name'],
            category=g['category'],
            svg_path_data=g['svg_path'],
            default_colors=g['default_colors'],
            available_subcomponents=g['subcomponents'],
            description=f"Standard vector template for {g['name']}"
        )
        db.session.add(tmpl)

    for key, a in SVG_ACCESSORIES.items():
        tmpl = GarmentTemplate(
            name=a['name'],
            category=a['category'],
            svg_path_data=a['svg_path'],
            default_colors=a['default_colors'],
            description=f"Luxury accessory vector template for {a['name']}"
        )
        db.session.add(tmpl)

    db.session.flush()

    # 4. Suppliers
    sup1 = Supplier(name='Royal Silk Mills Varanasi', contact_person='Rajesh Kumar', email='rajesh@varanasisilk.com', phone='+91 98765 43210', address='Ghat Road, Varanasi, India', rating=4.9, lead_time_days=10)
    sup2 = Supplier(name='Milano Textile Atelier', contact_person='Gianna Rossi', email='gianna@milanotextiles.it', phone='+39 02 5555 0192', address='Via Montenapoleone 12, Milan, Italy', rating=4.8, lead_time_days=14)
    sup3 = Supplier(name='EcoThread Organics', contact_person='Sarah Jenkins', email='sarah@ecothread.com', phone='+1 415 555 0188', address='Market St, San Francisco, CA', rating=4.6, lead_time_days=7)

    db.session.add_all([sup1, sup2, sup3])
    db.session.flush()

    # 5. Fabrics & Materials
    f1 = Fabric(code='FAB-SILK-01', name='Raw Banarasi Zari Silk', fabric_type='silk', composition='100% Mulberry Silk with Real Gold Zari', weight_gsm=180.0, width_inches=44.0, color_name='Royal Crimson', color_hex='#d90429', pattern_type='jacquard', unit_price=45.0, current_stock=250.0, minimum_stock=40.0, supplier_id=sup1.id, eco_friendly=True)
    f2 = Fabric(code='FAB-VELVET-02', name='Italian Midnight Velvet', fabric_type='velvet', composition='100% Cotton Velvet', weight_gsm=320.0, width_inches=54.0, color_name='Deep Navy', color_hex='#1d3557', pattern_type='solid', unit_price=32.0, current_stock=180.0, minimum_stock=30.0, supplier_id=sup2.id)
    f3 = Fabric(code='FAB-COTTON-03', name='Organic Egyptian Cotton Lawn', fabric_type='cotton', composition='100% GOTS Certified Cotton', weight_gsm=110.0, width_inches=60.0, color_name='Pure Pearl White', color_hex='#ffffff', pattern_type='solid', unit_price=16.5, current_stock=500.0, minimum_stock=50.0, supplier_id=sup3.id, eco_friendly=True)
    f4 = Fabric(code='FAB-ORGANZA-04', name='Sheer Floral Printed Organza', fabric_type='organza', composition='100% Silk Organza', weight_gsm=45.0, width_inches=54.0, color_name='Blush Pink', color_hex='#ffb703', pattern_type='floral', unit_price=28.0, current_stock=15.0, minimum_stock=25.0, supplier_id=sup1.id) # Low stock alert!

    db.session.add_all([f1, f2, f3, f4])

    m1 = Material(code='TRIM-ZAP-01', name='Antique Gold YKK Zipper 12"', category='zipper', color='Gold', unit='pieces', unit_price=2.5, current_stock=400.0, minimum_stock=50.0, supplier_id=sup2.id)
    m2 = Material(code='TRIM-BTN-02', name='Mother of Pearl Shirts Buttons 14mm', category='button', color='White Pearl', unit='pieces', unit_price=0.8, current_stock=1200.0, minimum_stock=200.0, supplier_id=sup3.id)
    m3 = Material(code='TRIM-LCE-03', name='French Chantilly Lace Border', category='lace', color='Ivory', unit='meters', unit_price=12.0, current_stock=85.0, minimum_stock=20.0, supplier_id=sup2.id)

    db.session.add_all([m1, m2, m3])
    db.session.flush()

    # 6. Collections
    col1 = Collection(name='Royal Heritage Bridal 2026', code='COL-BRD-2026', season='Bridal/Couture', year=2026, description='Extravagant royal heritage bridal sarees, lehengas, and gowns woven with gold zari.', user_id=lead_designer.id, theme='Maharani Elegance', status='active', target_launch_date=datetime.now().date() + timedelta(days=60), total_budget=150000.0)
    col2 = Collection(name='Urban Sophistication SS26', code='COL-SS26', season='Spring/Summer', year=2026, description='Crisp tailored suits, shirt dresses, and pleated midi skirts for modern professionals.', user_id=designer_2.id, theme='Architectural Minimalism', status='planning', target_launch_date=datetime.now().date() + timedelta(days=90), total_budget=80000.0)

    db.session.add_all([col1, col2])
    db.session.flush()

    # 7. Runway Show
    show1 = RunwayShow(title='Paris Fashion Week Couture Presentation', collection_id=col1.id, location='Grand Palais, Paris', event_date=datetime.now() + timedelta(days=60), live_stream_url='https://live.styleforge.com/paris-ss26', status='scheduled', total_looks=24)
    db.session.add(show1)

    # 8. Measurement Profiles
    mp1 = MeasurementProfile(name='Standard US Female Size M', user_id=lead_designer.id, gender='female', bust_chest=36.0, waist=28.0, hips=38.0, inseam=30.0, shoulder_width=15.0, height=66.0, is_standard_size=True, standard_size_code='M')
    mp2 = MeasurementProfile(name='Sophia Laurent - Bespoke Measurements', user_id=client_user.id, gender='female', bust_chest=35.5, waist=26.5, hips=37.0, inseam=31.0, shoulder_width=14.8, height=68.0, body_shape='hourglass', is_standard_size=False, standard_size_code='Custom')
    db.session.add_all([mp1, mp2])
    db.session.flush()

    # 9. Sample Designs
    d1 = Design(
        title='Imperial Crimson Banarasi Saree Outfit',
        slug='imperial-crimson-banarasi-saree-outfit',
        description='Royal Varanasi silk saree paired with a heavy zari embroidered blouse and pleated shoulder pallu.',
        category='saree',
        user_id=lead_designer.id,
        collection_id=col1.id,
        status='approved',
        width=800,
        height=1000,
        tags=['saree', 'banarasi', 'bridal', 'zari', 'couture'],
        views_count=142,
        likes_count=38,
        is_public=True,
        canvas_data={
            'version': '1.0.0',
            'dimensions': {'width': 800, 'height': 1000},
            'background': {'color': '#181924', 'gridVisible': True},
            'layers': [
                {'id': 'l1', 'type': 'garment', 'label': 'Banarasi Saree Drape', 'visible': True, 'color': '#d90429', 'transform': {'x': 200, 'y': 250, 'scaleX': 1.0, 'scaleY': 1.0, 'rotation': 0}},
                {'id': 'l2', 'type': 'accessory', 'label': 'Diamond Choker', 'visible': True, 'color': '#ffd166', 'transform': {'x': 350, 'y': 220, 'scaleX': 1.0, 'scaleY': 1.0, 'rotation': 0}}
            ]
        }
    )

    d2 = Design(
        title='Azure Silk Anarkali Kurti Suite',
        slug='azure-silk-anarkali-kurti-suite',
        description='Flared silk kurti with intricate side slits and hand-embroidered neckline.',
        category='kurti',
        user_id=lead_designer.id,
        collection_id=col1.id,
        status='in_review',
        width=800,
        height=1000,
        tags=['kurti', 'anarkali', 'silk', 'festive'],
        views_count=89,
        likes_count=19,
        is_public=True,
        canvas_data={'version': '1.0.0', 'dimensions': {'width': 800, 'height': 1000}, 'layers': []}
    )

    d3 = Design(
        title='Architectural Pleated Midi Shirt Dress',
        slug='architectural-pleated-midi-shirt-dress',
        description='Contemporary shirt dress with sharp spread collar and contrasting accordion pleated skirt.',
        category='dress',
        user_id=designer_2.id,
        collection_id=col2.id,
        status='draft',
        width=800,
        height=1000,
        tags=['dress', 'minimalist', 'tailored', 'urban'],
        views_count=45,
        likes_count=11,
        is_public=False,
        canvas_data={'version': '1.0.0', 'dimensions': {'width': 800, 'height': 1000}, 'layers': []}
    )

    db.session.add_all([d1, d2, d3])
    db.session.flush()

    # Build versions, costing, specs, approval workflow for design 1 & 2
    CostingEngineService.generate_default_costing_for_design(d1)
    CostingEngineService.generate_default_costing_for_design(d2)
    CostingEngineService.generate_default_costing_for_design(d3)

    SizingEngineService.create_default_spec_sheet(d1)
    SizingEngineService.create_default_spec_sheet(d2)
    SizingEngineService.create_default_spec_sheet(d3)

    # 10. Approval Workflows
    wf1 = ApprovalWorkflow(design_id=d1.id, current_step=3, total_steps=3, status='approved', priority='high')
    db.session.add(wf1)
    db.session.flush()

    s1 = ApprovalStep(workflow_id=wf1.id, step_number=1, step_name='Concept & Design Review', reviewer_id=lead_designer.id, reviewer_role='lead_designer', status='approved', comments='Exquisite traditional drape concept.', reviewed_at=datetime.utcnow() - timedelta(days=5))
    s2 = ApprovalStep(workflow_id=wf1.id, step_number=2, step_name='BOM Costing & Fabric Verification', reviewer_id=prod_mgr.id, reviewer_role='production_manager', status='approved', comments='Fabric stock in Varanasi warehouse verified.', reviewed_at=datetime.utcnow() - timedelta(days=3))
    s3 = ApprovalStep(workflow_id=wf1.id, step_number=3, step_name='Executive Final Sign-off', reviewer_id=admin.id, reviewer_role='admin', status='approved', comments='Approved for Paris Fashion Week runway production.', reviewed_at=datetime.utcnow() - timedelta(days=1))

    db.session.add_all([s1, s2, s3])

    # 11. Moodboards & Color Palettes
    mb1 = Moodboard(title='Royal Varanasi Inspiration Board', description='Zari weaves, antique brass architecture, and Mughal garden motifs.', user_id=lead_designer.id, collection_id=col1.id, background_color='#181924')
    db.session.add(mb1)
    db.session.flush()

    cp1 = ColorPalette(name='Royal Zari Heritage', moodboard_id=mb1.id, hex_codes=['#d90429', '#e9c46a', '#1d3557', '#8338ec', '#ffffff'], pantone_codes=['PANTONE 19-1763 TCX', 'PANTONE 14-0955 TCX', 'PANTONE 19-4024 TCX', 'PANTONE 18-3838 TCX', 'PANTONE Bright White'], primary_hex='#d90429')
    db.session.add(cp1)

    ma1 = MoodboardAsset(moodboard_id=mb1.id, asset_type='text', text_content='Heritage Mughal Architecture & Golden Zari Threads', position_x=40, position_y=40, width=300, height=100)
    ma2 = MoodboardAsset(moodboard_id=mb1.id, asset_type='color', color_hex='#d90429', position_x=40, position_y=160, width=120, height=120, caption='Royal Crimson')
    ma3 = MoodboardAsset(moodboard_id=mb1.id, asset_type='color', color_hex='#e9c46a', position_x=180, position_y=160, width=120, height=120, caption='Pure Gold Zari')
    db.session.add_all([ma1, ma2, ma3])

    # 12. Digital Sketchbook
    sb1 = Sketchbook(title='Couture Silhouette Studies 2026', description='Quick croquis vector sketches of sleeve cuts and skirt volumes.', user_id=lead_designer.id, cover_color='#4a3e3d', total_pages=2)
    db.session.add(sb1)
    db.session.flush()

    sp1 = SketchPage(sketchbook_id=sb1.id, page_number=1, title='Pleated Saree Pallu Geometry', background_grid='fashion_croquis', notes='Focus on structural weight of Varanasi silk fold.')
    db.session.add(sp1)

    # 13. Team & Collaboration
    team1 = Team(name='StyleForge Atelier Paris', description='Core design and production team for Paris Fashion Week.', owner_id=lead_designer.id, plan_tier='enterprise')
    db.session.add(team1)
    db.session.flush()

    tm1 = TeamMember(team_id=team1.id, user_id=lead_designer.id, role='owner')
    tm2 = TeamMember(team_id=team1.id, user_id=designer_2.id, role='editor')
    tm3 = TeamMember(team_id=team1.id, user_id=prod_mgr.id, role='admin')
    tm4 = TeamMember(team_id=team1.id, user_id=client_user.id, role='reviewer')
    db.session.add_all([tm1, tm2, tm3, tm4])

    ws1 = Workspace(team_id=team1.id, name='Bridal Couture Workspace', description='Collaborative hub for royal heritage collection.')
    db.session.add(ws1)

    cm1 = DesignComment(design_id=d1.id, user_id=client_user.id, comment_text='The gold zari border on the pallu is stunning! Can we make the blouse sleeves slightly longer?', canvas_x=360, canvas_y=320)
    db.session.add(cm1)

    af1 = ActivityFeed(team_id=team1.id, user_id=lead_designer.id, action_type='approved_design', entity_name=d1.title, entity_type='Design', entity_id=d1.id, description='Design approved for runway production.')
    db.session.add(af1)

    # 14. Calendar & Tasks
    ev1 = CalendarEvent(title='Paris Fashion Week Fitting Session', description='Final fitting with lead models for Couture collection.', event_type='fitting', start_date=datetime.now() + timedelta(days=20), end_date=datetime.now() + timedelta(days=20, hours=4), collection_id=col1.id, user_id=lead_designer.id, location='Grand Palais Studio 4')
    db.session.add(ev1)
    db.session.flush()

    t1 = TaskItem(event_id=ev1.id, design_id=d1.id, title='Prepare Spec Sheet & Sample Garment', assigned_to_id=prod_mgr.id, status='in_progress', priority='high', due_date=datetime.now() + timedelta(days=15))
    db.session.add(t1)

    # 15. Designer Portfolio
    port1 = Portfolio(user_id=lead_designer.id, title='Sabyasachi Mukherjee Couture Portfolio', bio='Celebrated Indian fashion designer renowned for pioneering heritage textiles and royal bridal couture globally.', theme_style='haute_couture', views_count=1240)
    db.session.add(port1)
    db.session.flush()

    pi1 = PortfolioItem(portfolio_id=port1.id, design_id=d1.id, title='Imperial Crimson Banarasi Saree', category='Bridal Couture', featured_image='/static/assets/sample-saree.jpg', description='Pure silk Banarasi saree woven in gold zari.', client_name='Royal Wedding House', press_mentions=['Vogue India', "Harper's Bazaar", 'Elle'])
    db.session.add(pi1)

    # 16. Notifications
    n1 = Notification(user_id=lead_designer.id, type='approval_request', title='Design Approved', message=f'Imperial Crimson Banarasi Saree has been fully approved by Executive Sign-off.', link_url=f'/studio?id={d1.id}')
    n2 = Notification(user_id=prod_mgr.id, type='stock_low', title='Low Stock Alert', message='Sheer Floral Printed Organza is below threshold (15m remaining).', link_url='/inventory')
    db.session.add_all([n1, n2])

    # 17. Analytics Snapshot
    AnalyticsSnapshot(snapshot_date=datetime.now().date(), total_designs=3, total_collections=2, total_fabrics=4, active_users=5, total_cost_calculated=4500.0, popular_garments={'Saree': 1, 'Kurti': 1, 'Dress': 1})

    db.session.commit()
    print("Database successfully seeded with StyleForge fashion SaaS sample data!")
