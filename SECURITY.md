# Security Policy & Implementation - StyleForge SaaS

StyleForge adheres to modern security standards for enterprise SaaS applications:

## 1. Authentication & Password Security
- Passwords are securely hashed using Werkzeug's `generate_password_hash` (PBKDF2 with SHA-256 and random salts).
- Plaintext passwords are never stored in the database.

## 2. Authorization & RBAC
- Role-based access control enforces strict role boundaries: `admin`, `lead_designer`, `designer`, `production_manager`, `client`.
- API endpoints are protected using `@login_required_api` and `@role_required_api` decorators.

## 3. Input Validation & Sanitization
- All payload inputs pass through `InputValidator` checks (email regex, username rules, hex color verification, HTML tag stripping).

## 4. Audit Logging & Accountability
- Critical actions (user registration, logins, design creation/updates, fabric movements, workflow approvals) are recorded in the immutable `audit_logs` table with timestamp and IP address.
