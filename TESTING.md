# Testing Guide - StyleForge SaaS

StyleForge features an automated Pytest test suite covering authentication, API endpoints, design canvas operations, costing calculations, size grading, inventory movements, approval workflows, and administrative audit logging.

## Running Tests

Execute pytest from project root:
```bash
pytest -v
```

## Test Modules Overview

- `tests/test_auth.py`: Tests registration, login, session auth, invalid passwords.
- `tests/test_designs.py`: Tests design creation, listing, updating canvas state.
- `tests/test_collections.py`: Tests collection creation and runway show lists.
- `tests/test_inventory.py`: Tests fabric stock listing and stock movement tracking.
- `tests/test_costing.py`: Tests Bill of Materials (BOM) creation and margin formulas.
- `tests/test_sizing.py`: Tests measurement profiles and points-of-measure spec sheets.
- `tests/test_moodboards.py`: Tests moodboard listing and Pantone color harmony generation.
- `tests/test_workflows.py`: Tests approval pipeline step actions.
- `tests/test_collaboration.py`: Tests canvas comments and activity feeds.
- `tests/test_analytics.py`: Tests dashboard metrics aggregations.
- `tests/test_admin.py`: Tests audit log retrieval and system status endpoint.
