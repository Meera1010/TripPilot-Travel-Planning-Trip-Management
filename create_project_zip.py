import os
import zipfile
import shutil

SOURCE_DIR = r"e:\Virtual Outfit Designer"
OUTPUT_ZIP_WORKSPACE = os.path.join(SOURCE_DIR, "StyleForge_Virtual_Outfit_Designer.zip")
ARTIFACT_DIR = r"C:\Users\abc\.gemini\antigravity\brain\ef3e3787-ef05-44fa-b90a-b7d27ef2d823"
OUTPUT_ZIP_ARTIFACT = os.path.join(ARTIFACT_DIR, "StyleForge_Virtual_Outfit_Designer.zip")

def make_zip():
    print(f"Creating ZIP archive from {SOURCE_DIR}...")
    with zipfile.ZipFile(OUTPUT_ZIP_WORKSPACE, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(SOURCE_DIR):
            # Skip existing zip file to avoid recursion
            if "StyleForge_Virtual_Outfit_Designer.zip" in files:
                files.remove("StyleForge_Virtual_Outfit_Designer.zip")
            if ".pytest_cache" in dirs:
                dirs.remove(".pytest_cache")
            if "__pycache__" in dirs:
                dirs.remove("__pycache__")
                
            for file in files:
                if file.endswith('.pyc') or file == "StyleForge_Virtual_Outfit_Designer.zip":
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, SOURCE_DIR)
                zipf.write(file_path, arcname)

    print(f"Zip created successfully at {OUTPUT_ZIP_WORKSPACE}")
    file_size_mb = os.path.getsize(OUTPUT_ZIP_WORKSPACE) / (1024 * 1024)
    print(f"Archive size: {file_size_mb:.2f} MB")

    # Copy to artifacts directory
    if os.path.exists(ARTIFACT_DIR):
        shutil.copy2(OUTPUT_ZIP_WORKSPACE, OUTPUT_ZIP_ARTIFACT)
        print(f"Copied archive to artifact directory: {OUTPUT_ZIP_ARTIFACT}")

if __name__ == '__main__':
    make_zip()
