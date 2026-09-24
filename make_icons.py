#!/usr/bin/env python3
"""
Auto-generate PWA icons (192x192, 512x512) using pure Python.
No dependencies needed — works on any Python install.
"""
import struct
import zlib
import math
from pathlib import Path

ROOT = Path.cwd()
ASSETS = ROOT / "assets"

def create_icon(size):
    """Create ToolCrate icon as RGBA pixel array."""
    pixels = []
    cx, cy = size / 2, size / 2
    pad = size * 0.06
    radius = size * 0.20

    for y in range(size):
        row = []
        for x in range(size):
            # Check if inside rounded square
            inside = False
            if pad <= x <= size - pad and pad <= y <= size - pad:
                # Check corners
                corner_ok = True
                corners = [
                    (pad + radius, pad + radius),                       # top-left
                    (size - pad - radius, pad + radius),                # top-right
                    (pad + radius, size - pad - radius),                # bottom-left
                    (size - pad - radius, size - pad - radius),         # bottom-right
                ]
                # Top-left corner
                if x < pad + radius and y < pad + radius:
                    if (x - corners[0][0])**2 + (y - corners[0][1])**2 > radius**2:
                        corner_ok = False
                # Top-right
                elif x > size - pad - radius and y < pad + radius:
                    if (x - corners[1][0])**2 + (y - corners[1][1])**2 > radius**2:
                        corner_ok = False
                # Bottom-left
                elif x < pad + radius and y > size - pad - radius:
                    if (x - corners[2][0])**2 + (y - corners[2][1])**2 > radius**2:
                        corner_ok = False
                # Bottom-right
                elif x > size - pad - radius and y > size - pad - radius:
                    if (x - corners[3][0])**2 + (y - corners[3][1])**2 > radius**2:
                        corner_ok = False
                inside = corner_ok

            if not inside:
                row.append((0, 0, 0, 0))  # transparent
                continue

            # Background gradient (emerald → teal, top-left to bottom-right)
            t = (x + y) / (2 * size)
            r = int(16 + (20 - 16) * t)
            g = int(185 + (184 - 185) * t)
            b = int(129 + (166 - 129) * t)

            # Leaf shapes (top half)
            leaf_y_start = cy - size * 0.38
            leaf_y_end = cy - size * 0.08
            if leaf_y_start <= y <= leaf_y_end:
                # Two leaves, symmetric
                left_leaf_center = cx - size * 0.09
                right_leaf_center = cx + size * 0.09

                # Distance to leaf curve
                def in_leaf(lx):
                    dy = (y - leaf_y_start) / (leaf_y_end - leaf_y_start)
                    # Leaf width peaks in middle
                    width = math.sin(dy * math.pi) * size * 0.12
                    # Leaf position
                    center_x = lx - size * 0.04 * dy if lx < cx else lx + size * 0.04 * dy
                    return abs(x - center_x) <= width

                if in_leaf(left_leaf_center) or in_leaf(right_leaf_center):
                    r, g, b = 255, 255, 255  # white leaves
                    row.append((r, g, b, 245))
                    continue

            # Crate body (bottom rectangle)
            crate_top = cy + size * 0.02
            crate_bottom = cy + size * 0.28
            crate_left = cx - size * 0.24
            crate_right = cx + size * 0.24

            if crate_left <= x <= crate_right and crate_top <= y <= crate_bottom:
                # Slight gradient in crate
                t2 = (y - crate_top) / (crate_bottom - crate_top)
                r, g, b = 255, 255, 255

                # Handle slot (dark cutout)
                slot_top = cy + size * 0.13
                slot_bottom = cy + size * 0.20
                slot_left = cx - size * 0.09
                slot_right = cx + size * 0.09
                if slot_left <= x <= slot_right and slot_top <= y <= slot_bottom:
                    r, g, b = 16, 140, 100  # darker emerald for slot

                row.append((r, g, b, 250))
                continue

            # Background only
            row.append((r, g, b, 255))
        pixels.append(row)

    return pixels

def pixels_to_png(pixels, width, height):
    """Convert RGBA pixels to PNG bytes."""
    # Filter type 0 for each row
    raw = b''
    for row in pixels:
        raw += b'\x00'  # filter byte
        for (r, g, b, a) in row:
            raw += bytes([r, g, b, a])

    # Compress
    compressed = zlib.compress(raw, 9)

    # Build chunks
    def chunk(chunk_type, data):
        return (
            struct.pack('>I', len(data)) +
            chunk_type +
            data +
            struct.pack('>I', zlib.crc32(chunk_type + data) & 0xffffffff)
        )

    # Signature
    png = b'\x89PNG\r\n\x1a\n'

    # IHDR: width, height, bit depth, color type, compression, filter, interlace
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
    png += chunk(b'IHDR', ihdr_data)

    # IDAT
    png += chunk(b'IDAT', compressed)

    # IEND
    png += chunk(b'IEND', b'')

    return png

# ============================================================
# Generate both icons
# ============================================================
print("=" * 60)
print("Generating PWA icons (no dependencies)")
print("=" * 60)
print()

ASSETS.mkdir(exist_ok=True)

for size in [192, 512]:
    print(f"Generating {size}x{size} icon...", end=" ", flush=True)
    pixels = create_icon(size)
    png_data = pixels_to_png(pixels, size, size)

    output_path = ASSETS / f"icon-{size}.png"
    output_path.write_bytes(png_data)

    kb = len(png_data) / 1024
    print(f"OK  ({kb:.1f} KB)")

print()
print("=" * 60)
print("DONE!")
print("=" * 60)
print()
print("Files created:")
print(f"  assets/icon-192.png")
print(f"  assets/icon-512.png")
print()
print("Verify:")
print(f"  1. Open assets/icon-192.png (double-click)")
print(f"  2. Should see ToolCrate green icon")
print()
print("Next:")
print("  git add .")
print('  git commit -m "Add PWA icons"')
print("  git push")
print()
input("Press Enter to close...")