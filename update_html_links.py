import re
from pathlib import Path

ROOT = Path.cwd()

root_files = sorted(ROOT.glob("*.html"))
blog_files = sorted((ROOT / "blog").glob("*.html"))

print(f"Found {len(root_files)} root HTML files and {len(blog_files)} blog HTML files.")

def update_root_html(file_path):
    content = file_path.read_text(encoding="utf-8")
    
    # Remove any existing mobile.css or responsive.css link tags
    content = re.sub(r'\s*<link[^>]+href=["\']assets/(?:mobile|responsive)\.css[^"\']*["\'][^>]*>', '', content)
    
    # Look for assets/style.css
    style_pattern = re.compile(r'(<link[^>]+href=["\']assets/style\.css["\'][^>]*>)', re.IGNORECASE)
    
    new_links = (
        r'\1\n'
        r'  <link rel="stylesheet" href="assets/mobile.css?v=2">\n'
        r'  <link rel="stylesheet" href="assets/responsive.css?v=2">'
    )
    
    if style_pattern.search(content):
        updated = style_pattern.sub(new_links, content, count=1)
        file_path.write_text(updated, encoding="utf-8")
        print(f"  OK root: {file_path.name}")
        return True
    else:
        print(f"  WARNING: style.css not found in {file_path.name}")
        return False

def update_blog_html(file_path):
    content = file_path.read_text(encoding="utf-8")
    
    # Remove any existing ../assets/mobile.css or ../assets/responsive.css link tags
    content = re.sub(r'\s*<link[^>]+href=["\']\.\./assets/(?:mobile|responsive)\.css[^"\']*["\'][^>]*>', '', content)
    
    style_pattern = re.compile(r'(<link[^>]+href=["\']\.\./assets/style\.css["\'][^>]*>)', re.IGNORECASE)
    
    new_links = (
        r'\1\n'
        r'    <link rel="stylesheet" href="../assets/mobile.css?v=2">\n'
        r'    <link rel="stylesheet" href="../assets/responsive.css?v=2">'
    )
    
    if style_pattern.search(content):
        updated = style_pattern.sub(new_links, content, count=1)
        file_path.write_text(updated, encoding="utf-8")
        print(f"  OK blog: {file_path.name}")
        return True
    else:
        print(f"  WARNING: ../assets/style.css not found in {file_path.name}")
        return False

success_count = 0
for f in root_files:
    if update_root_html(f):
        success_count += 1

for f in blog_files:
    if update_blog_html(f):
        success_count += 1

print(f"\nCompleted: {success_count}/{len(root_files) + len(blog_files)} files updated.")
