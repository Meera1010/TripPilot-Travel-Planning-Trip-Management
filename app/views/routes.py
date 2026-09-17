from flask import Blueprint, render_template, redirect, url_for
from app.services.auth_service import AuthService

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    user = AuthService.get_current_user()
    if user:
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')

@main_bp.route('/login')
def login():
    return render_template('auth/login.html')

@main_bp.route('/register')
def register():
    return render_template('auth/register.html')

@main_bp.route('/dashboard')
def dashboard():
    user = AuthService.get_current_user()
    if not user:
        return redirect(url_for('main.login'))
    return render_template('dashboard/index.html', user=user)

@main_bp.route('/trips')
def trips():
    user = AuthService.get_current_user()
    if not user:
        return redirect(url_for('main.login'))
    return render_template('trips/index.html', user=user)

@main_bp.route('/itinerary')
def itinerary():
    user = AuthService.get_current_user()
    if not user:
        return redirect(url_for('main.login'))
    return render_template('itinerary/index.html', user=user)

@main_bp.route('/expenses')
def expenses():
    user = AuthService.get_current_user()
    if not user:
        return redirect(url_for('main.login'))
    return render_template('expenses/index.html', user=user)

@main_bp.route('/packing')
def packing():
    user = AuthService.get_current_user()
    if not user:
        return redirect(url_for('main.login'))
    return render_template('packing/index.html', user=user)

@main_bp.route('/journal')
def journal():
    user = AuthService.get_current_user()
    if not user:
        return redirect(url_for('main.login'))
    return render_template('journal/index.html', user=user)

@main_bp.route('/analytics')
def analytics():
    user = AuthService.get_current_user()
    if not user:
        return redirect(url_for('main.login'))
    return render_template('analytics/index.html', user=user)

@main_bp.route('/admin')
def admin():
    user = AuthService.get_current_user()
    if not user or user.role != 'admin':
        return redirect(url_for('main.dashboard'))
    return render_template('admin/index.html', user=user)
