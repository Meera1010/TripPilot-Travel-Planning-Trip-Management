# StyleForge - Virtual Outfit Designer SaaS

StyleForge is an enterprise-grade Virtual Outfit Designer SaaS web application built with Python Flask, SQLite, HTML5, Vanilla CSS3, Vanilla JavaScript, and an HTML5 2D Canvas & SVG vector outfit design engine.

## Key Features

- **Virtual Outfit Studio**: Interactive 2D canvas with vector garments (sarees, kurtis, dresses, shirts, skirts, jackets, trousers, gowns, bags, shoes, jewelry).
- **Garment Customization**: Custom color swatches, fabric textures, pattern overlays (stripes, polka dots), layering, move/resize/rotate handles, and undo/redo state history.
- **Production Cost Calculator**: Itemized Bill of Materials (BOM), fabric yield estimator, cutting waste allowance, labor hours, and wholesale/retail profit margin formulas.
- **Tech Spec Exporter**: Automated technical specification sheets for factory production and pattern makers.
- **Measurements & Custom Sizing**: Body measurement profiles, points of measure (POM), seam allowances, and standard size grading matrix (XS to XXL).
- **Fabric & Material Inventory**: Fabric stock yardage tracking, trim inventory, supplier lead times, and low stock threshold alerts.
- **Design Approval Workflows**: Multi-stage sign-off pipeline (Concept Review → BOM Fabric Verification → Executive Approval) with audit history.
- **Inspiration Moodboards & Sketchbooks**: Freeform visual canvas boards with Pantone color harmony generators and croquis vector sketching tools.
- **Fashion Collections & Runway Shows**: Season grouping (Spring/Summer, Autumn/Winter, Bridal/Couture), lookbook ordering, and runway event scheduling.
- **Team Collaboration & Activity Feed**: Atelier workspaces, live design canvas comments, and team audit logs.
- **Security & RBAC**: Role-based access control (Admin, Lead Designer, Fashion Designer, Production Manager, Client), session security, input validation, and audit logging.

## Tech Stack

- **Backend**: Python 3.10+, Flask, SQLAlchemy, SQLite, Werkzeug.
- **Frontend**: HTML5, Vanilla CSS3 (Custom Design Tokens), Vanilla JavaScript (ES6+).
- **Design Engine**: HTML5 Canvas 2D, SVG Path Rasterizer, Transformation Handles, UndoManager.
- **Testing**: Pytest, Pytest-Flask.

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Seed the database with sample fashion data:
   ```bash
   flask --app run.py seed-db
   ```

3. Run the development server:
   ```bash
   python run.py
   ```
   Open `http://localhost:5000` in your web browser.

4. Demo Accounts:
   - **Lead Designer**: `sabyasachi` / `Sabya@123`
   - **Admin**: `admin` / `Admin@123`
