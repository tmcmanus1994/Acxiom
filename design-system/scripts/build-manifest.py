#!/usr/bin/env python3
"""Regenerate design-system/assets.json and design-system/icons.md from the
contents of assets/.

Run from the repository root:

    python3 design-system/scripts/build-manifest.py

Pillow is optional. Without it, image dimensions are omitted rather than guessed.
"""

import json
import os
import sys
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
except ImportError:
    Image = None

# Icon metadata: slug -> (label from the master template, category, extra search aliases)
ICONS = OrderedDict([
    ("ai",              ("AI",              "technology",    ["artificial intelligence", "machine learning"])),
    ("analytics",       ("Analytics",       "data",          ["chart", "insights", "measurement"])),
    ("automotive",      ("Automotive",      "industry",      ["car", "vehicle", "auto"])),
    ("banking",         ("Banking",         "industry",      ["bank", "finance", "financial services"])),
    ("bot-ai",          ("Bot/AI",          "technology",    ["chatbot", "robot", "assistant"])),
    ("calendar",        ("Calendar",        "ui",            ["date", "schedule", "event"])),
    ("chat-message",    ("Chat/Message",    "communication", ["sms", "text", "conversation"])),
    ("checkmark",       ("Check",           "symbol",        ["tick", "done", "complete", "confirm"])),
    ("churn",           ("Churn",           "data",          ["attrition", "retention", "loss"])),
    ("clean-room",      ("Clean room",      "data",          ["data clean room", "secure", "collaboration"])),
    ("clock",           ("Clock",           "ui",            ["time", "duration", "speed"])),
    ("cloud",           ("Cloud",           "technology",    ["saas", "hosting", "infrastructure"])),
    ("connected-tv",    ("Connected TV",    "media",         ["ctv", "ott", "streaming", "television"])),
    ("cpg",             ("CPG",             "industry",      ["consumer packaged goods", "fmcg"])),
    ("credit-cards",    ("Credit cards",    "commerce",      ["payment", "card", "checkout"])),
    ("customer",        ("Customer",        "people",        ["person", "user", "consumer", "profile"])),
    ("data",            ("Data",            "data",          ["database", "records", "storage"])),
    ("data-file",       ("Data file",       "data",          ["dataset", "file", "export"])),
    ("direct-mail",     ("Direct mail",     "communication", ["postal", "print", "letter"])),
    ("directional",     ("Directional",     "symbol",        ["arrow", "direction", "pointer"])),
    ("document",        ("Document",        "ui",            ["page", "report", "paper"])),
    ("equal",           ("Equal",           "symbol",        ["equals", "parity", "same"])),
    ("growth",          ("Growth",          "data",          ["increase", "trend up", "scale"])),
    ("headphones",      ("Headphones",      "media",         ["audio", "listen", "support"])),
    ("health",          ("Health",          "industry",      ["healthcare", "medical", "pharma"])),
    ("heart",           ("Heart",           "symbol",        ["love", "favorite", "loyalty"])),
    ("household",       ("Household",       "people",        ["home", "family", "residence"])),
    ("key",             ("Key",             "security",      ["access", "unlock", "credential"])),
    ("landline",        ("Landline",        "communication", ["phone", "telephone", "call"])),
    ("laptop",          ("Laptop",          "device",        ["computer", "desktop", "web"])),
    ("legal",           ("Legal",           "industry",      ["law", "compliance", "regulation"])),
    ("location",        ("Location",        "ui",            ["pin", "map", "geo", "place"])),
    ("lock",            ("Lock",            "security",      ["privacy", "secure", "protected"])),
    ("mail",            ("Mail",            "communication", ["email", "envelope", "message"])),
    ("manufacturing",   ("Manufacturing",   "industry",      ["factory", "production", "industrial"])),
    ("manufacturing-2", ("Manufacturing 2", "industry",      ["factory", "production", "alternate"])),
    ("megaphone",       ("Megaphone",       "marketing",     ["announce", "advertising", "promotion"])),
    ("money",           ("Money",           "commerce",      ["cash", "revenue", "budget", "cost"])),
    ("music",           ("Music",           "media",         ["audio", "streaming", "entertainment"])),
    ("no-symbol",       ("No symbol",       "symbol",        ["prohibited", "blocked", "not allowed"])),
    ("privacy",         ("Privacy",         "security",      ["consent", "shield", "protection"])),
    ("question-mark",   ("Question mark",   "symbol",        ["help", "unknown", "faq"])),
    ("quote-mark",      ("Quote mark",      "symbol",        ["testimonial", "citation", "quotation"])),
    ("restaurant",      ("Restaurant",      "industry",      ["dining", "food service", "qsr"])),
    ("revenue",         ("Revenue",         "data",          ["sales", "income", "earnings"])),
    ("reverse-arrows",  ("Reverse arrows",  "symbol",        ["exchange", "sync", "two-way", "swap"])),
    ("search",          ("Search",          "ui",            ["find", "magnifier", "discovery"])),
    ("service",         ("Service",         "people",        ["support", "customer service", "help desk"])),
    ("shopping-bag",    ("Retail",          "commerce",      ["shopping bag", "purse", "store", "purchase"])),
    ("shopping-cart",   ("Shopping cart",   "commerce",      ["ecommerce", "basket", "checkout"])),
    ("smartphone",      ("Smartphone",      "device",        ["mobile", "phone", "app"])),
    ("speech-bubble",   ("Speech bubble",   "communication", ["comment", "feedback", "dialogue"])),
    ("storefront",      ("Storefront",      "commerce",      ["shop", "retail location", "brick and mortar"])),
    ("telco",           ("Telco",           "industry",      ["telecom", "telecommunications", "carrier"])),
    ("thumbs-up",       ("Thumbs up",       "symbol",        ["approve", "like", "positive"])),
    ("travel",          ("Travel",          "industry",      ["airline", "trip", "tourism", "hospitality"])),
    ("trophy",          ("Trophy",          "symbol",        ["award", "win", "achievement", "best"])),
    ("versus",          ("Versus",          "symbol",        ["vs", "compare", "comparison"])),
    ("x-symbol",        ("X symbol",        "symbol",        ["close", "cancel", "cross", "remove"])),
    ("yes-symbol",      ("Yes symbol",      "symbol",        ["affirmative", "agree", "positive"])),
])


def dims(path):
    if Image is None:
        return None
    try:
        with Image.open(path) as im:
            return {"width": im.size[0], "height": im.size[1]}
    except Exception:
        return None


def entry(relpath, **extra):
    item = {"path": relpath}
    d = dims(os.path.join(ROOT, relpath))
    if d:
        item.update(d)
    item.update(extra)
    return item


def build():
    manifest = OrderedDict()
    manifest["$description"] = (
        "Machine-readable index of every Acxiom brand asset in this repository. "
        "Regenerate with: python3 design-system/scripts/build-manifest.py"
    )
    manifest["$version"] = "1.0.0"
    manifest["source"] = {
        "masterTemplate": "reference/AcxiomMasterTemplate_2026.pdf",
        "valueDeck": "reference/AcxiomValueDeck_2026.pdf",
        "templateVersion": "1.0",
        "templateDate": "2026-01",
    }
    manifest["tokens"] = {
        "json": "design-system/tokens/tokens.json",
        "css": "design-system/tokens/tokens.css",
        "scss": "design-system/tokens/tokens.scss",
        "tailwind": "design-system/tokens/tailwind.preset.js",
    }

    # --- Logo -------------------------------------------------------------
    logo = []
    for variant, use in (("black", "Light surfaces: bone, white."),
                         ("white", "Dark surfaces: black, plum, imagery, the glow.")):
        for ext, note in (("svg", "Preferred for web and any scaled use."),
                          ("png", "Raster, transparent background."),
                          ("eps", "Print and vendor handoff.")):
            p = "assets/logo/%s/acxiom-logo-%s.%s" % (ext, variant, ext)
            if os.path.exists(os.path.join(ROOT, p)):
                logo.append(entry(p, variant=variant, format=ext, useOn=use, note=note))
    manifest["logo"] = {
        "aspectRatio": "802.22 / 124.81",
        "rules": [
            "Appears in the slide footer only.",
            "Never recolor: black or white only.",
            "Never stretch, rotate, box, or add effects.",
            "If the glow passes over the logo, paste the logo on top so it stays legible.",
            "Client logos never go in the footer, only on cover slides.",
        ],
        "files": logo,
    }

    # --- Icons ------------------------------------------------------------
    icons = []
    for slug, (label, category, aliases) in ICONS.items():
        variants = {}
        for v in ("black", "white"):
            p = "assets/icons/dotted/%s/%s.png" % (v, slug)
            if os.path.exists(os.path.join(ROOT, p)):
                variants[v] = p
        if not variants:
            print("warning: no files for icon %r" % slug, file=sys.stderr)
            continue
        icons.append({
            "name": slug,
            "label": label,
            "category": category,
            "aliases": aliases,
            "variants": variants,
        })

    bullets = []
    for n in range(1, 20):
        variants = {}
        for v in ("black", "white"):
            p = "assets/icons/bullets/%s/bullet-%02d.png" % (v, n)
            if os.path.exists(os.path.join(ROOT, p)):
                variants[v] = p
        if variants:
            bullets.append({"name": "bullet-%02d" % n, "variants": variants})

    manifest["icons"] = {
        "style": "Dotted line — forms drawn from dot fields rather than solid strokes.",
        "size": {"width": 285, "height": 285, "format": "PNG", "alpha": True},
        "usage": "Black on light surfaces, white on dark. ~48pt placed on a slide; bullets ~20pt.",
        "categories": sorted({i["category"] for i in icons}),
        "dotted": icons,
        "bullets": bullets,
    }

    # --- Backgrounds ------------------------------------------------------
    backgrounds = {}
    for group, folder, note in (
        ("teams", "assets/backgrounds/teams", "Microsoft Teams video backgrounds."),
        ("desktop", "assets/backgrounds/desktop", "4K desktop wallpapers."),
    ):
        files = []
        d = os.path.join(ROOT, folder)
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if f.startswith("."):
                    continue
                files.append(entry("%s/%s" % (folder, f)))
        backgrounds[group] = {"note": note, "files": files}
    manifest["backgrounds"] = backgrounds

    # --- Reference --------------------------------------------------------
    manifest["reference"] = [
        {
            "path": "reference/AcxiomMasterTemplate_2026.pdf",
            "title": "Acxiom Master Template 2026, v1.0",
            "pages": 21,
            "note": "The authoritative source for this design system: dos and don'ts, "
                    "icon inventory, flow-chart and chart styling, photo glow, footer anatomy.",
        },
        {
            "path": "reference/AcxiomValueDeck_2026.pdf",
            "title": "Acxiom Value Deck 2026",
            "pages": 95,
            "note": "The template applied at length. Use it to see the system in practice.",
        },
    ]

    manifest["contact"] = {"brand": "acxiombrand@acxiom.com"}
    return manifest


def write_icons_md(manifest):
    lines = [
        "# Icon Index",
        "",
        "Auto-generated by `design-system/scripts/build-manifest.py`. Do not edit by hand.",
        "",
        "All icons are **285 × 285 px PNG** with transparency, in the Acxiom dotted-line style.",
        "Use **black on light surfaces, white on dark**. Machine-readable equivalent:",
        "[`assets.json`](./assets.json).",
        "",
        "## Dotted icons (%d)" % len(manifest["icons"]["dotted"]),
        "",
    ]

    by_cat = OrderedDict()
    for icon in manifest["icons"]["dotted"]:
        by_cat.setdefault(icon["category"], []).append(icon)

    for cat in sorted(by_cat):
        lines += ["### %s" % cat.title(), "",
                  "| Preview | Name | Template label | Also search for |",
                  "| --- | --- | --- | --- |"]
        for icon in sorted(by_cat[cat], key=lambda i: i["name"]):
            black = icon["variants"].get("black", "")
            preview = "![%s](../%s)" % (icon["name"], black) if black else ""
            lines.append("| %s | `%s` | %s | %s |" % (
                preview, icon["name"], icon["label"], ", ".join(icon["aliases"])))
        lines.append("")

    lines += [
        "## Dotted bullets (%d)" % len(manifest["icons"]["bullets"]),
        "",
        "Numbered decorative bullets for list slides. They carry no fixed meaning — pick by shape.",
        "",
        "| Preview | Name |",
        "| --- | --- |",
    ]
    for b in manifest["icons"]["bullets"]:
        black = b["variants"].get("black", "")
        preview = "![%s](../%s)" % (b["name"], black) if black else ""
        lines.append("| %s | `%s` |" % (preview, b["name"]))
    lines.append("")
    return "\n".join(lines)


def main():
    manifest = build()
    out_json = os.path.join(ROOT, "design-system", "assets.json")
    with open(out_json, "w") as fh:
        json.dump(manifest, fh, indent=2)
        fh.write("\n")
    print("wrote %s" % out_json)

    out_md = os.path.join(ROOT, "design-system", "icons.md")
    with open(out_md, "w") as fh:
        fh.write(write_icons_md(manifest))
    print("wrote %s" % out_md)


if __name__ == "__main__":
    main()
