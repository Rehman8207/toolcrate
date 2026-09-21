#!/usr/bin/env python3
"""
Clean up extra/temporary files from ToolCrate project.
Shows what will be deleted, asks for confirmation.
"""
from pathlib import Path
import shutil

ROOT = Path.cwd()

# ============================================================
# Files to check for deletion
# ============================================================

# Temporary Python scripts (one-time fixes)
TEMP_SCRIPTS = [
    "fix_all.py",
    "fix_meta.py",
    "fix_meta2.py",
    "fix_select.py",
    "fix_broken_links.py",
    "bing_fix.py",
    "green_theme.py",
    "update_colors.py",
    "update_colors2.py",
    "optimize.py",
    "optimize2.py",
    "colorize.py",
    "fix.py",
    "fix2.py",
    "fix3.py",
    "fix4.py",
    "fix5.py",
    "fix_nav.py",
    "fix_nav2.py",
    "polish_ui.py",
    "add_homepage_faq.py",
    "update_blogs_urdu.py",
    "setup.py",
]

# Extra/duplicate files
EXTRA_FILES = [
    "pdf-merger.html",           # duplicate of pdf-merge.html
    "assets/style.pretty.css",   # old unused backup
    "style.pretty.css",          # if exists in root
    "30-day-plan.html",          # was for PDF generation
    "wrangler.jsonc",            # if not used
]

# Backup folders (start with _backup_)
BACKUP_PATTERN = "_backup_*"

# ============================================================
# Scan for what exists
# ============================================================
print("=" * 70)
print("🧹 CLEANUP SCAN")
print("=" * 70)
print()

to_delete = []
total_size = 0

# Check temp scripts
print("📄 Temporary Python scripts:")
found_scripts = []
for script in TEMP_SCRIPTS:
    fp = ROOT / script
    if fp.exists():
        size = fp.stat().st_size
        found_scripts.append((script, size))
        total_size += size
        print(f"   ✓ {script} ({size:,} bytes)")
        to_delete.append(fp)

if not found_scripts:
    print("   (none)")

# Check extra files
print()
print("📄 Extra/duplicate files:")
found_extras = []
for f in EXTRA_FILES:
    fp = ROOT / f
    if fp.exists():
        size = fp.stat().st_size
        found_extras.append((f, size))
        total_size += size
        print(f"   ✓ {f} ({size:,} bytes)")
        to_delete.append(fp)

if not found_extras:
    print("   (none)")

# Check backup folders
print()
print("📁 Backup folders:")
found_backups = []
for bp in ROOT.glob(BACKUP_PATTERN):
    if bp.is_dir():
        size = sum(f.stat().st_size for f in bp.rglob("*") if f.is_file())
        found_backups.append((bp.name, size))
        total_size += size
        print(f"   ✓ {bp.name}/ ({size:,} bytes)")
        to_delete.append(bp)

if not found_backups:
    print("   (none)")

# ============================================================
# Summary
# ============================================================
print()
print("=" * 70)
print(f"📊 TOTAL: {len(to_delete)} items, {total_size:,} bytes (~{total_size/1024:.1f} KB)")
print("=" * 70)
print()

if not to_delete:
    print("✨ Project already clean!")
    input("Press Enter to close...")
    exit(0)

# ============================================================
# Confirmation
# ============================================================
print("⚠️  The following will be DELETED:")
for fp in to_delete:
    if fp.is_dir():
        print(f"   🗑️  {fp.name}/ (folder)")
    else:
        print(f"   🗑️  {fp.relative_to(ROOT)}")
print()

confirm = input("Delete all these files? (yes/no): ").strip().lower()

if confirm not in ("yes", "y"):
    print("\n❌ Cancelled. No files deleted.")
    input("Press Enter to close...")
    exit(0)

# ============================================================
# Delete
# ============================================================
print()
print("Deleting...")

deleted_count = 0
errors = []

for fp in to_delete:
    try:
        if fp.is_dir():
            shutil.rmtree(fp)
            print(f"   ✅ Deleted folder: {fp.name}/")
        else:
            fp.unlink()
            print(f"   ✅ Deleted: {fp.relative_to(ROOT)}")
        deleted_count += 1
    except Exception as e:
        errors.append((fp.name, str(e)))
        print(f"   ❌ Error deleting {fp.name}: {e}")

# ============================================================
# Final summary
# ============================================================
print()
print("=" * 70)
print(f"🎉 CLEANUP COMPLETE!")
print(f"   Deleted: {deleted_count} items")
print(f"   Freed: ~{total_size/1024:.1f} KB")
if errors:
    print(f"   Errors: {len(errors)}")
print("=" * 70)
print()
print("Next steps:")
print("  1. python -m http.server 8000")
print("  2. Test homepage + a few tools")
print("  3. If everything works:")
print("     git add .")
print("     git commit -m 'Cleanup: remove temp scripts and duplicate files'")
print("     git push")
print()
input("Press Enter to close...")