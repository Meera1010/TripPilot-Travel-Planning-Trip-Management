import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

LEGACY_FILES_TO_REMOVE = [
    'app/utils/pantone_extended_library.py',
    'app/utils/pantone_color_database.py',
    'app/utils/svg_library.py',
    'app/utils/vector_patterns_library.py',
    'app/utils/extended_vector_catalog.py',
    'app/utils/dresses_catalog.py',
    'app/utils/shirts_catalog.py',
    'app/utils/sarees_catalog.py',
    'app/utils/kurtis_catalog.py',
    'app/utils/skirts_catalog.py',
    'app/utils/jackets_catalog.py',
    'app/utils/trousers_catalog.py',
    'app/utils/gowns_catalog.py',
    'app/utils/accessories_catalog.py',
    'app/utils/menswear_catalog.py',
    'app/models/design.py',
    'app/models/inventory.py',
    'app/models/costing.py',
    'app/models/collaboration.py',
    'app/models/workflow.py',
    'app/models/collection.py',
    'app/models/sketchbook.py',
    'app/models/moodboard.py',
    'app/models/sizing.py',
    'app/models/portfolio.py',
    'app/models/notification.py',
    'app/api/designs.py',
    'app/api/inventory.py',
    'app/api/costing.py',
    'app/api/collaboration.py',
    'app/api/workflows.py',
    'app/api/collections.py',
    'app/api/sketchbooks.py',
    'app/api/moodboards.py',
    'app/api/sizing.py',
    'app/api/portfolios.py',
    'app/api/notifications.py',
    'app/services/canvas_engine.py',
    'app/services/color_palette_service.py',
    'app/services/costing_engine.py',
    'app/services/inventory_service.py',
    'app/services/sizing_engine.py',
    'app/services/version_service.py',
    'app/services/trend_forecasting_engine.py',
    'app/services/export_service.py',
    'app/services/brand_guidelines_service.py',
    'app/services/client_fitting_service.py',
    'app/services/embroidery_digitizer_service.py',
    'app/services/fabric_testing_service.py',
    'app/services/fitting_simulation_engine.py',
    'app/services/garment_care_service.py',
    'app/services/pattern_grading_service.py',
    'app/services/production_scheduling_service.py',
    'app/services/retail_analytics_service.py',
    'app/services/supply_chain_optimization_service.py',
    'app/services/sustainability_index_service.py',
    'app/services/tariffs_trade_service.py',
    'app/services/tech_pack_generator.py',
    'app/services/textile_dyeing_service.py',
    'app/services/wholesale_catalog_service.py',
]

for rel_path in LEGACY_FILES_TO_REMOVE:
    full_path = os.path.join(BASE_DIR, rel_path)
    if os.path.exists(full_path):
        try:
            os.remove(full_path)
            print(f"Removed legacy file: {rel_path}")
        except Exception as e:
            print(f"Could not remove {rel_path}: {e}")

print("Legacy cleanup complete!")
