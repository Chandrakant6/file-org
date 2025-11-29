import os
import shutil
import sys

# ---------- RULES ----------
RULES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".md"],
    "Spreadsheets": [".xlsx", ".xls", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".json"],
}

OTHERS = "Others"
# ----------------------------


def ensure_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


def match_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in RULES.items():
        if ext in extensions:
            return category
    return OTHERS


def organize(target_folder):
    print(f"Organizing: {target_folder}\n")

    for item in os.listdir(target_folder):
        item_path = os.path.join(target_folder, item)

        if os.path.isdir(item_path):
            continue

        category = match_category(item)
        dest_folder = os.path.join(target_folder, category)

        ensure_folder(dest_folder)

        dest_path = os.path.join(dest_folder, item)

        if os.path.exists(dest_path):
            print(f"⚠️ Skipped (already exists): {item}")
            continue

        shutil.move(item_path, dest_path)
        print(f"📁 Moved: {item} → {category}/")

    print("\n✨ Done organizing!\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python file_org.py <target-folder-path>")
        sys.exit(1)

    target_path = sys.argv[1]

    if not os.path.exists(target_path):
        print("❌ Error: Provided path does not exist.")
        sys.exit(1)

    organize(target_path)
