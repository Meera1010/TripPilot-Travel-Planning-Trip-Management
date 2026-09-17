import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

EXTENSIONS = {'.py', '.js', '.css', '.html', '.md', '.txt'}
EXCLUDE_DIRS = {'__pycache__', '.pytest_cache', 'instance', 'uploads', 'exports', '.git', 'venv'}

def count_file_loc(filepath):
    """Count non-blank lines in a file."""
    loc = 0
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if line.strip():
                    loc += 1
    except Exception as e:
        pass
    return loc

def run_loc_audit():
    total_files = 0
    total_loc = 0
    breakdown = {}

    for root, dirs, files in os.walk(PROJECT_ROOT):
        # Remove excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in EXTENSIONS:
                filepath = os.path.join(root, file)
                relpath = os.path.relpath(filepath, PROJECT_ROOT)
                loc = count_file_loc(filepath)
                total_files += 1
                total_loc += loc
                breakdown[relpath] = loc

    print("=" * 60)
    print("STYLEFORGE SAAS - LINES OF CODE (LOC) AUDIT REPORT")
    print("=" * 60)
    print(f"Total Source Files: {total_files}")
    print(f"Verified Meaningful LOC: {total_loc:,}")
    print("-" * 60)
    
    # Extension summary
    ext_summary = {}
    for path, loc in breakdown.items():
        ext = os.path.splitext(path)[1].lower()
        ext_summary[ext] = ext_summary.get(ext, 0) + loc

    print("LOC Breakdown by Language / File Extension:")
    for ext, loc in sorted(ext_summary.items(), key=lambda x: x[1], reverse=True):
        print(f"  {ext:<10} : {loc:>6,} LOC")

    print("=" * 60)
    return total_files, total_loc, breakdown

if __name__ == '__main__':
    run_loc_audit()
