import os
import zipfile

WORKSPACE_DIR = os.path.abspath(os.path.dirname(__file__))
ARTIFACT_DIR = r"C:\Users\abc\.gemini\antigravity\brain\ef3e3787-ef05-44fa-b90a-b7d27ef2d823"

def create_zip_archive():
    zip_filename = "TripPilot_Travel_Planning_Trip_Management.zip"
    artifact_zip_path = os.path.join(ARTIFACT_DIR, zip_filename)
    workspace_zip_path = os.path.join(WORKSPACE_DIR, zip_filename)

    print(f"Creating ZIP archive containing full project codebase and .git repository...")

    for target_path in [artifact_zip_path, workspace_zip_path]:
        with zipfile.ZipFile(target_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(WORKSPACE_DIR):
                # Include .git directory and source files, exclude __pycache__ and venv
                if '__pycache__' in root or 'node_modules' in root or '.pytest_cache' in root:
                    continue
                for file in files:
                    if file.endswith('.zip') or file.endswith('.pyc') or file == 'trippilot_dev.db':
                        continue
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, WORKSPACE_DIR)
                    zipf.write(full_path, rel_path)

        print(f"ZIP Archive created at: {target_path} (Size: {os.path.getsize(target_path) / (1024*1024):.2f} MB)")

if __name__ == '__main__':
    create_zip_archive()
