#!/usr/bin/env python3
"""Validate publication-critical invariants for The Cosmic Alchemy static site."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_ORIGIN = "https://thecosmicalchemy.com/"
HIDDEN_SERVICES = ("Akashic Records", "Astrology Consultation", "Numerology Reading")
EXPECTED_READMES = (
    "architecture/README.md",
    "architecture/decisions/README.md",
    "architecture/source/README.md",
    "docs/README.md",
    "docs/phases/README.md",
    "docs/stages/README.md",
    "docs/binary-source-docs/README.md",
    "src/README.md",
    "tests/README.md",
    "scripts/README.md",
    "data/README.md",
    "data-drivers/README.md",
    "archive/README.md",
    ".goldie/README.md",
    "configs/README.md",
    "workspace/README.md",
)
EXPECTED_PNGS = {
    "branding/favicon-om-lotus.png": (480, 480),
    "branding/favicon-32.png": (32, 32),
    "branding/favicon-48.png": (48, 48),
    "branding/apple-touch-icon.png": (180, 180),
}
LUCIDE_SHA256 = "8550d4d51d4046fab58c9e9c786bdd62e2a1e917102389f9a94138d2b397c6a0"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.refs: list[str] = []
        self.json_ld: list[str] = []
        self.missing_image_alt: list[str] = []
        self.unsafe_blank_links: list[str] = []
        self.label_targets: set[str] = set()
        self.form_control_ids: set[str] = set()
        self._in_json_ld = False
        self._json_chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        if attr.get("id"):
            self.ids.append(attr["id"] or "")
        for key in ("href", "src"):
            if attr.get(key):
                self.refs.append(attr[key] or "")
        if tag == "img" and "alt" not in attr:
            self.missing_image_alt.append(attr.get("src") or "unknown image")
        if tag == "a" and attr.get("target") == "_blank":
            rel = set((attr.get("rel") or "").split())
            if "noopener" not in rel:
                self.unsafe_blank_links.append(attr.get("href") or "unknown link")
        if tag == "label" and attr.get("for"):
            self.label_targets.add(attr["for"] or "")
        if tag in {"input", "textarea", "select"} and attr.get("id"):
            self.form_control_ids.add(attr["id"] or "")
        if tag == "script" and attr.get("type") == "application/ld+json":
            self._in_json_ld = True
            self._json_chunks = []

    def handle_data(self, data: str) -> None:
        if self._in_json_ld:
            self._json_chunks.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._in_json_ld:
            self.json_ld.append("".join(self._json_chunks))
            self._in_json_ld = False


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_local_refs(parser: PageParser, errors: list[str]) -> None:
    for ref in parser.refs:
        if ref.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
            continue
        parsed = urlsplit(ref)
        if parsed.scheme or parsed.netloc:
            continue
        path = parsed.path
        if not path or path == "/":
            continue
        candidate = ROOT / path.lstrip("/")
        if not candidate.exists():
            fail(errors, f"Missing local reference: {ref}")


def validate_homepage(page_name: str, production: bool, errors: list[str]) -> None:
    page = ROOT / page_name
    html = page.read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(html)

    duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicates:
        fail(errors, f"Duplicate HTML ids in {page_name}: {', '.join(duplicates)}")
    validate_local_refs(parser, errors)
    for ref in parser.refs:
        if ref.startswith("#") and len(ref) > 1 and ref[1:] not in parser.ids:
            fail(errors, f"Broken fragment reference in {page_name}: {ref}")
    if parser.missing_image_alt:
        fail(errors, f"Images without alt text in {page_name}: {parser.missing_image_alt}")
    if parser.unsafe_blank_links:
        fail(errors, f"New-tab links without noopener in {page_name}: {parser.unsafe_blank_links}")
    unlabelled = sorted(parser.form_control_ids - parser.label_targets)
    if unlabelled:
        fail(errors, f"Form controls without associated labels in {page_name}: {unlabelled}")

    for index, block in enumerate(parser.json_ld, start=1):
        try:
            json.loads(block)
        except json.JSONDecodeError as exc:
            fail(errors, f"Invalid JSON-LD block {index} in {page_name}: {exc}")

    for service in HIDDEN_SERVICES:
        if service.lower() in html.lower():
            fail(errors, f"Hidden service remains in {page_name}: {service}")

    for stale in ("muggle14.github.io/gold-healer", "DRAFT testimonial", ">Priya<", ">Himanshu<"):
        if stale in html:
            fail(errors, f"Stale or unverified content remains in {page_name}: {stale}")

    if html.count('class="svc-card') != 10:
        fail(errors, f"Expected 10 public service cards in {page_name}")
    if html.count('class="t-card') != 4:
        fail(errors, f"Expected 4 verified testimonial cards in {page_name}")
    for timing_marker in ('class="svc-dur"', "Timing as per the guidance", ">Duration<"):
        if timing_marker in html:
            fail(errors, f"Visible timing content remains in {page_name}: {timing_marker}")
    for required in (
        PUBLIC_ORIGIN,
        "branding/logo-emblem-gold.png",
        "branding/logo-mark.png",
        "branding/favicon-32.png",
        "branding/favicon-48.png",
        "branding/apple-touch-icon.png",
        "branding/social-preview.png",
        "vendor/lucide/lucide.min.js",
        "wa.me/918095175533",
        "tel:+918095175533",
    ):
        if required not in html:
            fail(errors, f"Required publication value missing from {page_name}: {required}")

    robots_match = re.search(r'<meta name="robots" content="([^"]+)">', html)
    robots = robots_match.group(1) if robots_match else ""
    if production:
        if "index" not in robots or "noindex" in robots:
            fail(errors, "Production homepage must be indexable")
        if 'data-environment="staging"' in html or "Staging —" in html:
            fail(errors, "Production homepage contains a staging marker")
    else:
        if robots != "noindex,nofollow":
            fail(errors, "Staging homepage must use noindex,nofollow")
        if 'data-environment="staging"' not in html:
            fail(errors, "Staging homepage is missing its environment marker")


def validate_supporting_files(errors: list[str]) -> None:
    for name in ("privacy.html", "terms.html", "404.html"):
        html = (ROOT / name).read_text(encoding="utf-8")
        parser = PageParser()
        parser.feed(html)
        validate_local_refs(parser, errors)
        if "muggle14.github.io/gold-healer" in html:
            fail(errors, f"Old canonical domain remains in {name}")

    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    if f"Sitemap: {PUBLIC_ORIGIN}sitemap.xml" not in robots:
        fail(errors, "robots.txt does not point to the canonical sitemap")

    sitemap = ET.parse(ROOT / "sitemap.xml")
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locations = [node.text for node in sitemap.findall("sm:url/sm:loc", namespace)]
    if locations != [PUBLIC_ORIGIN]:
        fail(errors, f"Unexpected sitemap locations: {locations}")

    cname = (ROOT / "CNAME").read_text(encoding="utf-8").strip()
    if cname != "thecosmicalchemy.com":
        fail(errors, "CNAME does not contain the canonical custom domain")


def validate_repository_standard(errors: list[str]) -> None:
    if not (ROOT / "STANDARD.md").exists():
        fail(errors, "STANDARD.md is missing")
    for relative_path in EXPECTED_READMES:
        if not (ROOT / relative_path).exists():
            fail(errors, f"Required folder README is missing: {relative_path}")

    stage_state_path = ROOT / ".goldie/stage_state.json"
    try:
        json.loads(stage_state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"Invalid project stage state: {exc}")


def validate_png_assets(errors: list[str]) -> None:
    for relative_path, expected_size in EXPECTED_PNGS.items():
        data = (ROOT / relative_path).read_bytes()
        if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
            fail(errors, f"Invalid PNG signature: {relative_path}")
            continue
        width, height = struct.unpack(">II", data[16:24])
        colour_type = data[25]
        if (width, height) != expected_size:
            fail(errors, f"Unexpected PNG dimensions for {relative_path}: {(width, height)}")
        if colour_type not in {4, 6}:
            fail(errors, f"PNG does not contain an alpha channel: {relative_path}")


def validate_vendored_dependency(errors: list[str]) -> None:
    runtime = ROOT / "vendor/lucide/lucide.min.js"
    digest = hashlib.sha256(runtime.read_bytes()).hexdigest()
    if digest != LUCIDE_SHA256:
        fail(errors, f"Lucide runtime integrity mismatch: {digest}")
    if not (ROOT / "vendor/lucide/LICENSE").exists():
        fail(errors, "Vendored Lucide licence is missing")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--production", action="store_true", help="Validate index.html")
    args = parser.parse_args()
    page_name = "index.html" if args.production else "staging.html"

    errors: list[str] = []
    validate_homepage(page_name, args.production, errors)
    validate_supporting_files(errors)
    validate_repository_standard(errors)
    validate_png_assets(errors)
    validate_vendored_dependency(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Validated {page_name} and publication support files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
