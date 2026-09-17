# Database Schema Documentation - StyleForge SaaS

StyleForge utilizes SQLite with SQLAlchemy ORM. Below is the relational schema overview:

## Core Tables

1. **users**: Primary user accounts.
2. **roles**: User RBAC role definitions and permissions.
3. **audit_logs**: Security & system activity logs.
4. **user_preferences**: UI theme, currency, grid size, auto-save settings.
5. **designs**: Outfit designs with JSON canvas state.
6. **design_versions**: Historical canvas snapshots.
7. **canvas_layers**: Layer definitions for garments, accessories, patterns.
8. **garment_templates**: Vector SVG preset library.
9. **collections**: Runway collections and season groupings.
10. **runway_shows**: Event details for fashion shows.
11. **fabrics**: Fabric inventory stock, composition, width, weight, prices.
12. **materials**: Trims, buttons, zippers inventory.
13. **suppliers**: Fabric & trim supplier directory.
14. **inventory_movements**: Stock movement log.
15. **costing_sheets**: Bill of Materials (BOM) master sheet.
16. **cost_items**: Itemized fabric, labor, and overhead cost lines.
17. **measurement_profiles**: Standard & custom body measurement profiles.
18. **spec_sheets**: Technical specification sheets & points of measure (POM).
19. **moodboards**: Visual inspiration boards.
20. **moodboard_assets**: Moodboard text, color, image cards.
21. **color_palettes**: Hex & Pantone color palettes.
22. **sketchbooks**: Digital fashion sketchbooks.
23. **sketch_pages**: Vector croquis drawing pages.
24. **approval_workflows**: Approval pipeline stages.
25. **approval_steps**: Reviewer sign-off steps.
26. **teams**: Team workspaces.
27. **team_members**: User team memberships.
28. **design_comments**: Canvas coordinate comments.
29. **activity_feeds**: Live team activity stream.
30. **calendar_events**: Production deadlines & events.
31. **portfolios**: Designer haute couture showcases.
32. **notifications**: In-app alert notifications.
33. **analytics_snapshots**: Daily analytical metrics records.
