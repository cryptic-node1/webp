#!/usr/bin/env python3
"""
WebP Converter — single or batch JPG/PNG → WebP
Usage: python tool.py
"""

from PIL import Image
from pathlib import Path
import sys


# ── Config ────────────────────────────────────────────────────────────────────

OUTPUT_FOLDER = Path("webp_output")   # change this to your preferred output folder
SUPPORTED = {".jpg", ".jpeg", ".png"}


# ── Helpers ───────────────────────────────────────────────────────────────────

def convert(src: Path, dest_folder: Path, quality: int) -> Path:
    """Convert a single image to WebP and save to dest_folder."""
    dest_folder.mkdir(parents=True, exist_ok=True)
    dest = dest_folder / (src.stem + ".webp")

    img = Image.open(src)

    # Preserve transparency for RGBA PNGs; strip alpha for JPEGs
    if img.mode in ("RGBA", "LA"):
        img.save(dest, "WEBP", quality=quality, lossless=False)
    else:
        img.convert("RGB").save(dest, "WEBP", quality=quality)

    return dest


def ask_quality() -> int:
    raw = input("Quality (0–100) [default: 80]: ").strip()
    if raw == "":
        return 80
    try:
        q = int(raw)
        if 0 <= q <= 100:
            return q
        print("  ✗ Out of range. Using default 80.")
        return 80
    except ValueError:
        print("  ✗ Invalid input. Using default 80.")
        return 80


def separator():
    print("─" * 50)


# ── Modes ─────────────────────────────────────────────────────────────────────

def single_convert():
    separator()
    print("SINGLE FILE CONVERT")
    separator()

    # File input
    while True:
        raw = input("File path: ").strip().strip('"').strip("'")
        src = Path(raw)
        if not src.exists():
            print(f"  ✗ File not found: {src}")
            continue
        if src.suffix.lower() not in SUPPORTED:
            print(f"  ✗ Unsupported format '{src.suffix}'. Accepted: jpg, jpeg, png")
            continue
        break

    quality = ask_quality()

    print(f"\nConverting  →  {src.name}  (quality={quality})")
    try:
        dest = convert(src, OUTPUT_FOLDER, quality)
        print(f"  ✓ Saved: {dest.resolve()}")
    except Exception as e:
        print(f"  ✗ Failed: {e}")


def batch_convert():
    separator()
    print("BATCH CONVERT")
    separator()

    # Folder input
    while True:
        raw = input("Folder path: ").strip().strip('"').strip("'")
        folder = Path(raw)
        if not folder.exists() or not folder.is_dir():
            print(f"  ✗ Folder not found: {folder}")
            continue
        break

    # Collect matching files
    files = [f for f in folder.iterdir() if f.suffix.lower() in SUPPORTED]
    if not files:
        print(f"  ✗ No JPG or PNG files found in: {folder}")
        return

    print(f"\nFound {len(files)} file(s):")
    for f in files:
        print(f"    {f.name}")

    quality = ask_quality()

    # Output folder: sibling of input folder, named <folder>_webp
    out_folder = folder.parent / (folder.name + "_webp")

    separator()
    print(f"Output folder: {out_folder.resolve()}")
    print(f"Quality: {quality}\n")

    success, failed = 0, 0
    for src in files:
        try:
            dest = convert(src, out_folder, quality)
            print(f"  ✓ {src.name}  →  {dest.name}")
            success += 1
        except Exception as e:
            print(f"  ✗ {src.name}  →  {e}")
            failed += 1

    separator()
    print(f"Done. {success} converted, {failed} failed.")
    if success:
        print(f"Output: {out_folder.resolve()}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print()
    print("  WebP Converter")
    print()
    print("  [1] Single file")
    print("  [2] Batch folder")
    print()

    choice = input("Select: ").strip()

    if choice == "1":
        single_convert()
    elif choice == "2":
        batch_convert()
    else:
        print("  ✗ Invalid choice. Enter 1 or 2.")
        sys.exit(1)

    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAborted.")
        sys.exit(0)
