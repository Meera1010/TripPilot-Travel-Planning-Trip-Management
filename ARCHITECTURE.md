# Architecture Documentation - StyleForge SaaS

## 1. System Overview

StyleForge is architected as a modular Flask SaaS application using the Application Factory pattern, RESTful API blueprints, SQLAlchemy ORM, and a Vanilla JavaScript Canvas Studio design engine.

```
+-----------------------------------------------------------------------+
|                            Browser UI                                 |
|   HTML5 / Vanilla CSS3 / Canvas Studio Engine / Pure JS Visualizers   |
+-----------------------------------------------------------------------+
                                   |
                          REST API (JSON)
                                   |
+-----------------------------------------------------------------------+
|                          Flask Backend                                |
|  API Blueprints | Security RBAC | Business Logic Engines | Audit Log  |
+-----------------------------------------------------------------------+
                                   |
                            SQLAlchemy ORM
                                   |
+-----------------------------------------------------------------------+
|                          SQLite Database                              |
+-----------------------------------------------------------------------+
```

## 2. Component Layers

### 2.1 Backend Core
- `app/config.py`: Environment configuration management.
- `app/__init__.py`: App factory, database initialization, error handlers.
- `app/models/`: SQLAlchemy ORM definitions across 15 domains.
- `app/services/`: Pure business logic engines (Costing, Canvas, Sizing, Color Palette, Inventory, Versioning, Audit, Analytics).
- `app/api/`: REST API controllers.

### 2.2 Studio Engine
- `CanvasStudio.js`: Coordinates rendering, hit testing, drag-and-drop, zoom/pan, and state saving.
- `Layer.js`: Encapsulates layer transformation, opacity, and path properties.
- `GarmentRenderer.js`: Rasterizes vector SVG paths and textures onto HTML5 Canvas 2D.
- `TransformController.js`: Renders bounding box outlines, scale knobs, and rotation handles.
- `UndoManager.js`: Manages undo/redo state history stack.
