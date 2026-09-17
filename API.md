# REST API Documentation - StyleForge SaaS

All API endpoints return JSON responses using the standard payload format:
```json
{
  "success": true,
  "data": {},
  "message": "Optional status message"
}
```

## 1. Authentication (`/api/auth`)
- `POST /api/auth/register`: Create new designer account.
- `POST /api/auth/login`: Authenticate credentials.
- `POST /api/auth/logout`: Clear session.
- `GET /api/auth/me`: Get current user details and preferences.

## 2. Outfit Designs (`/api/designs`)
- `GET /api/designs`: List designs with search, category, status filters.
- `POST /api/designs`: Create new design canvas.
- `GET /api/designs/<id>`: Get design details & canvas state.
- `PUT /api/designs/<id>`: Save canvas state & update metadata.
- `DELETE /api/designs/<id>`: Delete design.
- `GET /api/designs/<id>/versions`: List historical versions.
- `POST /api/designs/<id>/rollback/<version_id>`: Rollback canvas to version.

## 3. Production Costing (`/api/costing`)
- `GET /api/costing/<design_id>`: Get BOM costing sheet.
- `POST /api/costing/<design_id>/items`: Add fabric, trim, or labor item to BOM.
- `POST /api/costing/<design_id>/recalculate`: Recalculate margins and prices.

## 4. Sizing & Tech Specs (`/api/sizing`)
- `GET /api/sizing/profiles`: List body measurement profiles.
- `POST /api/sizing/profiles`: Create custom size profile.
- `GET /api/sizing/spec-sheets/<design_id>`: Get Points of Measure (POM) tech spec.

## 5. Inventory (`/api/inventory`)
- `GET /api/inventory/fabrics`: List fabrics in stock.
- `POST /api/inventory/fabrics`: Add fabric stock.
- `POST /api/inventory/movement`: Record inventory movement.

## 6. Approvals Workflow (`/api/workflows`)
- `GET /api/workflows/<design_id>`: Get approval pipeline status.
- `POST /api/workflows/step/action`: Approve or reject approval step.

## 7. Admin & Security (`/api/admin`)
- `GET /api/admin/audit-logs`: View system audit trail.
- `GET /api/admin/system-status`: System health metrics.
