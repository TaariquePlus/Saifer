#!/usr/bin/env python3
"""Apply Saifer Browser branding to an apktool-decoded Via Browser source tree.

Usage:
  python scripts/patch_branding.py /path/to/decoded-source /path/to/saifer-logo.png
Requires Pillow: python -m pip install Pillow

This script intentionally preserves the original package ID, manifest, adaptive icon
XML, monochrome icon, and all non-branding resources.
"""
from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image

LABEL_RESOURCE = "ce"
ICON_TARGETS = (
    ("res/drawable-xxxhdpi/cc.png", 192),
    ("res/mipmap-xxhdpi/ic_launcher.png", 144),
)


def patch_label(strings_file: Path) -> None:
    tree = ET.parse(strings_file)
    root = tree.getroot()
    target = next((node for node in root.findall("string") if node.get("name") == LABEL_RESOURCE), None)
    if target is None:
        raise ValueError(f"Could not find string resource name={LABEL_RESOURCE!r} in {strings_file}")
    target.text = "Saifer Browser"
    tree.write(strings_file, encoding="utf-8", xml_declaration=True)


def patch_icon(source: Path, target: Path, size: int) -> None:
    if not source.is_file():
        raise FileNotFoundError(f"Logo PNG not found: {source}")
    target.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as original:
        image = original.convert("RGBA")
        image.thumbnail((size, size), Image.Resampling.LANCZOS)
        # Center the complete logo on a transparent square; never crop foreground art.
        canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        canvas.alpha_composite(image, ((size - image.width) // 2, (size - image.height) // 2))
        canvas.save(target, format="PNG", optimize=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_tree", type=Path, help="Root directory of apktool-decoded source")
    parser.add_argument("logo_png", type=Path, help="Saifer logo PNG with transparent background")
    args = parser.parse_args()

    root = args.source_tree.resolve()
    strings_file = root / "res/values/strings.xml"
    if not strings_file.is_file() or not (root / "AndroidManifest.xml").is_file():
        parser.error("source_tree must be the root of an apktool-decoded Android project")

    try:
        patch_label(strings_file)
        for relative, size in ICON_TARGETS:
            patch_icon(args.logo_png.resolve(), root / relative, size)
    except (OSError, ValueError, ET.ParseError) as exc:
        print(f"Branding patch failed: {exc}", file=sys.stderr)
        return 1

    print("Branding patch applied.")
    print("Updated label: Saifer Browser")
    for relative, size in ICON_TARGETS:
        print(f"Updated {relative} ({size}x{size}, transparent PNG)")
    print("Package ID, manifest, adaptive icon XML, monochrome icon, and other resources were not changed intentionally.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
