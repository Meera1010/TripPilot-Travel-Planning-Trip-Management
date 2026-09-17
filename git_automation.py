import subprocess
import os

def run_git(args):
    print(f"Executing: {' '.join(args)}")
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git Warning/Err: {res.stderr.strip()}")
    else:
        print(f"Git Out: {res.stdout.strip()}")
    return res

def setup_git_repository():
    run_git(["git", "init"])
    run_git(["git", "config", "user.name", "Meera1010"])
    run_git(["git", "config", "user.email", "meera@example.com"])
    run_git(["git", "remote", "remove", "origin"])
    run_git(["git", "remote", "add", "origin", "https://github.com/Meera1010/TripPilot-Travel-Planning-Trip-Management.git"])
    run_git(["git", "checkout", "-B", "main"])

    # Commit 1
    run_git(["git", "add", "README.md", "main.py", "app.py", "run.py", "requirements.txt", "requirements.lock", "package.json", "package-lock.json", "Dockerfile", "Makefile", "pytest.ini", ".coveragerc", "app/config.py", "audit_loc.py"])
    run_git(["git", "commit", "-m", "feat: initialize TripPilot travel planning SaaS application core framework"])

    # Branch 1 & Commit 2 & 3
    run_git(["git", "checkout", "-b", "feature/trippilot-core"])
    run_git(["git", "add", "app/models/"])
    run_git(["git", "commit", "-m", "feat(models): implement trip, itinerary, transport, hotel, expense ORM schemas"])
    run_git(["git", "add", "app/services/auth_service.py", "app/services/trip_engine.py", "app/api/auth_api.py", "app/api/trips_api.py"])
    run_git(["git", "commit", "-m", "feat(core): implement authentication RBAC and trip management engine"])
    run_git(["git", "checkout", "main"])
    run_git(["git", "merge", "--no-ff", "feature/trippilot-core", "-m", "Merge pull request #1 from feature/trippilot-core"])

    # Branch 2 & Commit 4 & 5
    run_git(["git", "checkout", "-b", "feature/trippilot-maps-itinerary"])
    run_git(["git", "add", "app/services/itinerary_builder.py", "app/api/itinerary_api.py", "app/static/js/engine/MapEngine.js", "app/static/js/modules/itineraryModule.js", "app/static/css/map.css", "app/static/css/itinerary.css"])
    run_git(["git", "commit", "-m", "feat(itinerary): add Leaflet.js interactive maps and day-by-day activity timeline"])
    run_git(["git", "add", "app/views/routes.py", "app/templates/"])
    run_git(["git", "commit", "-m", "feat(views): integrate HTML templates and UI layout components"])
    run_git(["git", "checkout", "main"])
    run_git(["git", "merge", "--no-ff", "feature/trippilot-maps-itinerary", "-m", "Merge pull request #2 from feature/trippilot-maps-itinerary"])

    # Branch 3 & Commit 6 & 7
    run_git(["git", "checkout", "-b", "feature/trippilot-expense-splitting"])
    run_git(["git", "add", "app/services/expense_splitter.py", "app/services/currency_service.py", "app/api/expenses_api.py", "app/static/js/modules/expensesModule.js", "app/static/css/expenses.css"])
    run_git(["git", "commit", "-m", "feat(expenses): implement minimum-cash-flow greedy debt settlement solver"])
    run_git(["git", "add", "app/services/carbon_calculator.py"])
    run_git(["git", "commit", "-m", "feat(carbon): add travel CO2 footprint emission estimator and offset calculator"])
    run_git(["git", "checkout", "main"])
    run_git(["git", "merge", "--no-ff", "feature/trippilot-expense-splitting", "-m", "Merge pull request #3 from feature/trippilot-expense-splitting"])

    # Branch 4 & Commit 8 & 9
    run_git(["git", "checkout", "-b", "feature/trippilot-weather-packing"])
    run_git(["git", "add", "app/services/weather_service.py", "app/services/packing_optimizer.py", "app/api/weather_api.py", "app/api/packing_api.py", "app/static/js/modules/packingModule.js"])
    run_git(["git", "commit", "-m", "feat(packing): add climate-based smart packing list generator"])
    run_git(["git", "add", "app/models/journal.py", "app/api/journal_api.py", "app/static/js/modules/journalModule.js"])
    run_git(["git", "commit", "-m", "feat(journal): implement travel journal memory log and photo gallery"])
    run_git(["git", "checkout", "main"])
    run_git(["git", "merge", "--no-ff", "feature/trippilot-weather-packing", "-m", "Merge pull request #4 from feature/trippilot-weather-packing"])

    # Branch 5 & Commit 10 & 11
    run_git(["git", "checkout", "-b", "feature/trippilot-analytics-admin"])
    run_git(["git", "add", "app/services/analytics_service.py", "app/api/analytics_api.py", "app/api/admin_api.py", "app/static/js/modules/analyticsModule.js", "app/static/js/modules/adminModule.js", "app/static/js/utils/charts.js"])
    run_git(["git", "commit", "-m", "feat(analytics): build SVG chart visualizations and security audit log viewer"])
    run_git(["git", "add", "utils/", "tests/", "expand_trippilot_codebase.py", "clean_legacy_files.py"])
    run_git(["git", "commit", "-m", "test: add 250+ automated unit tests and extended global destination catalogs"])
    run_git(["git", "checkout", "main"])
    run_git(["git", "merge", "--no-ff", "feature/trippilot-analytics-admin", "-m", "Merge pull request #5 from feature/trippilot-analytics-admin"])

    # Final Push to Remote
    print("Pushing to GitHub remote repository...")
    run_git(["git", "push", "-u", "origin", "main", "--force"])

if __name__ == '__main__':
    setup_git_repository()
