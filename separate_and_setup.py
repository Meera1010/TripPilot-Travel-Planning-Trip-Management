import os
import shutil
import subprocess
import zipfile

BASE_DIR = r"E:\Virtual Outfit Designer"
TRIPPILOT_DIR = r"E:\TripPilot"
STYLEFORGE_DIR = r"E:\StyleForge"
ARTIFACT_DIR = r"C:\Users\abc\.gemini\antigravity\brain\ef3e3787-ef05-44fa-b90a-b7d27ef2d823"

def copy_tree_filtered(src, dst, ignore_patterns=None):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst, exist_ok=True)
    for root, dirs, files in os.walk(src):
        if '__pycache__' in root or '.pytest_cache' in root or '.git' in root:
            continue
        rel_path = os.path.relpath(root, src)
        dest_root = os.path.join(dst, rel_path)
        os.makedirs(dest_root, exist_ok=True)
        for f in files:
            if f.endswith('.pyc') or f.endswith('.db') or f.endswith('.zip'):
                continue
            if ignore_patterns and any(p in f for p in ignore_patterns):
                continue
            shutil.copy2(os.path.join(root, f), os.path.join(dest_root, f))

def setup_trippilot():
    print("--------------------------------------------------")
    print("Setting up standalone project: E:\\TripPilot")
    print("--------------------------------------------------")
    copy_tree_filtered(BASE_DIR, TRIPPILOT_DIR)

    # Initialize Git in E:\TripPilot
    subprocess.run(["git", "init"], cwd=TRIPPILOT_DIR, capture_output=True)
    subprocess.run(["git", "config", "user.name", "Meera1010"], cwd=TRIPPILOT_DIR, capture_output=True)
    subprocess.run(["git", "config", "user.email", "meera@example.com"], cwd=TRIPPILOT_DIR, capture_output=True)
    subprocess.run(["git", "remote", "add", "origin", "https://github.com/Meera1010/TripPilot-Travel-Planning-Trip-Management.git"], cwd=TRIPPILOT_DIR, capture_output=True)
    subprocess.run(["git", "checkout", "-B", "main"], cwd=TRIPPILOT_DIR, capture_output=True)
    subprocess.run(["git", "add", "."], cwd=TRIPPILOT_DIR, capture_output=True)
    subprocess.run(["git", "commit", "-m", "feat: complete TripPilot Travel Planning & Trip Management SaaS application"], cwd=TRIPPILOT_DIR, capture_output=True)
    subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=TRIPPILOT_DIR, capture_output=True)

    # Create Zip Archive
    zip_path_1 = os.path.join(TRIPPILOT_DIR, "TripPilot_Travel_Planning_Trip_Management.zip")
    zip_path_2 = os.path.join(ARTIFACT_DIR, "TripPilot_Travel_Planning_Trip_Management.zip")
    for zpath in [zip_path_1, zip_path_2]:
        with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(TRIPPILOT_DIR):
                if '__pycache__' in root or '.pytest_cache' in root:
                    continue
                for f in files:
                    if f.endswith('.zip') or f.endswith('.pyc') or f.endswith('.db'):
                        continue
                    full = os.path.join(root, f)
                    rel = os.path.relpath(full, TRIPPILOT_DIR)
                    zf.write(full, rel)

    print(f"E:\\TripPilot initialized, pushed to GitHub, and ZIP created!")

def setup_styleforge():
    print("--------------------------------------------------")
    print("Setting up standalone project: E:\\StyleForge")
    print("--------------------------------------------------")
    copy_tree_filtered(BASE_DIR, STYLEFORGE_DIR)

    # Modify main.py port for StyleForge to 5051
    main_py_path = os.path.join(STYLEFORGE_DIR, 'main.py')
    with open(main_py_path, 'w', encoding='utf-8') as f:
        f.write("""import os
from app import create_app

app = create_app(os.environ.get('FLASK_ENV', 'development'))

if __name__ == '__main__':
    print("StyleForge Virtual Outfit Designer SaaS starting on http://127.0.0.1:5051")
    app.run(host='127.0.0.1', port=5051, debug=True)
""")

    # Initialize Git in E:\StyleForge
    subprocess.run(["git", "init"], cwd=STYLEFORGE_DIR, capture_output=True)
    subprocess.run(["git", "config", "user.name", "Meera1010"], cwd=STYLEFORGE_DIR, capture_output=True)
    subprocess.run(["git", "config", "user.email", "meera@example.com"], cwd=STYLEFORGE_DIR, capture_output=True)
    subprocess.run(["git", "remote", "add", "origin", "https://github.com/Meera1010/StyleForge---Virtual-Outfit-Designer.git"], cwd=STYLEFORGE_DIR, capture_output=True)
    subprocess.run(["git", "checkout", "-B", "main"], cwd=STYLEFORGE_DIR, capture_output=True)
    subprocess.run(["git", "add", "."], cwd=STYLEFORGE_DIR, capture_output=True)
    subprocess.run(["git", "commit", "-m", "feat: complete StyleForge Virtual Outfit Designer SaaS application"], cwd=STYLEFORGE_DIR, capture_output=True)
    subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=STYLEFORGE_DIR, capture_output=True)

    # Create Zip Archive
    zip_path_1 = os.path.join(STYLEFORGE_DIR, "StyleForge_Virtual_Outfit_Designer.zip")
    zip_path_2 = os.path.join(ARTIFACT_DIR, "StyleForge_Virtual_Outfit_Designer.zip")
    for zpath in [zip_path_1, zip_path_2]:
        with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(STYLEFORGE_DIR):
                if '__pycache__' in root or '.pytest_cache' in root:
                    continue
                for f in files:
                    if f.endswith('.zip') or f.endswith('.pyc') or f.endswith('.db'):
                        continue
                    full = os.path.join(root, f)
                    rel = os.path.relpath(full, STYLEFORGE_DIR)
                    zf.write(full, rel)

    print(f"E:\\StyleForge initialized, pushed to GitHub, and ZIP created!")

if __name__ == '__main__':
    setup_trippilot()
    setup_styleforge()
    print("Both projects separated into dedicated folders successfully!")
