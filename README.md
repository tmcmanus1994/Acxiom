# Acxiom Design System

Brand assets and design tokens for the **Acxiom Master Template 2026 (v1.0)**.

Everything here is derived from the two source decks in [`reference/`](reference/) — the colors,
type scale, spacing, and rules were extracted from those PDFs rather than approximated.

---

## Start here

| If you want to… | Go to |
| --- | --- |
| Understand the brand and its rules | [`design-system/brand-guidelines.md`](design-system/brand-guidelines.md) |
| Pull tokens into code | [`design-system/tokens/`](design-system/tokens/) |
| Find an icon | [`design-system/icons.md`](design-system/icons.md) |
| Query every asset programmatically | [`design-system/assets.json`](design-system/assets.json) |
| See the system rendered | [`design-system/preview.html`](design-system/preview.html) |
| Read the original decks | [`reference/`](reference/) |

Building something with Claude? [`CLAUDE.md`](CLAUDE.md) is the working brief.

---

## The system in one screen

**Two typefaces.** Tw Cen MT for headlines and body. Consolas for kickers and labels, always
uppercase, always widely tracked.

**Four core colors.**

| | Hex | Role |
| --- | --- | --- |
| Black | `#000000` | Dark surface — covers, hero moments |
| Bone | `#EDECE8` | Light surface — the default content background |
| White | `#FFFFFF` | Text on dark; chart fills |
| Plum | `#2A182E` | Secondary dark surface, third chart series |

**Three accents,** for data and highlights only, never for type: magenta `#FF00A9`,
blue `#1A12F7`, orange `#FF672D`.

**One hero effect.** The glow — an angled beam of magenta-through-violet light across black.

```css
background: linear-gradient(75deg, #000000 0%, #2A182E 35%, #940BE0 70%, #FF00A9 100%);
```

---

## Repository layout

```
.
├── CLAUDE.md                       Working brief for Claude
├── README.md
├── assets/
│   ├── logo/
│   │   ├── svg/                    acxiom-logo-{black,white}.svg   ← preferred
│   │   ├── png/                    3344 × 521, transparent
│   │   └── eps/                    print and vendor handoff
│   ├── icons/
│   │   ├── dotted/black/           60 icons, 285 × 285 PNG
│   │   ├── dotted/white/           60 icons, mirrored set
│   │   ├── bullets/black/          19 numbered bullets
│   │   └── bullets/white/          19 numbered bullets
│   └── backgrounds/
│       ├── teams/                  5 Teams video backgrounds
│       └── desktop/                4 wallpapers at 3840 × 2160
├── design-system/
│   ├── brand-guidelines.md         Rules, anatomy, dos and don'ts
│   ├── icons.md                    Searchable icon index with previews
│   ├── assets.json                 Machine-readable manifest of everything
│   ├── preview.html                Visual reference — open in a browser
│   ├── tokens/
│   │   ├── tokens.json             Source of truth (DTCG format)
│   │   ├── tokens.css              CSS custom properties + utility classes
│   │   ├── tokens.scss             SCSS variables and mixins
│   │   └── tailwind.preset.js      Tailwind preset
│   └── scripts/
│       └── build-manifest.py       Regenerates assets.json and icons.md
└── reference/
    ├── AcxiomMasterTemplate_2026.pdf   21pp — the authoritative source
    └── AcxiomValueDeck_2026.pdf        95pp — the template applied at length
```

---

## Using the tokens

**CSS**

```html
<link rel="stylesheet" href="design-system/tokens/tokens.css">
```

```css
.hero {
  background: var(--acx-gradient-glow);
  color: var(--acx-text-on-dark-display);
}
```

**SCSS**

```scss
@use 'design-system/tokens/tokens' as acx;

.kicker { @include acx.acx-eyebrow; }
```

**Tailwind**

```js
// tailwind.config.js
module.exports = {
  presets: [require('./design-system/tokens/tailwind.preset.js')],
  content: ['./src/**/*.{html,js,jsx,ts,tsx}'],
}
```

```html
<p class="font-mono text-eyebrow uppercase">One look. One experience.</p>
```

**Anything else** — read [`tokens.json`](design-system/tokens/tokens.json). It is the source of
truth; the other three files are generated views of it.

---

## Regenerating the manifest

After adding or renaming assets:

```bash
python3 design-system/scripts/build-manifest.py
```

This rewrites `design-system/assets.json` and `design-system/icons.md`. New icons need a row in
the `ICONS` table at the top of the script so they get a label, category, and search aliases.

---

## Fonts

**Tw Cen MT** is licensed through Monotype and is not bundled here. It ships with Microsoft
Office, which is why the PowerPoint template can rely on it. For web work, the token files carry
a fallback stack — Twentieth Century, Futura, Century Gothic, Questrial — ordered closest first.

**Consolas** ships with Windows and Office. The fallback stack is Cascadia Mono, SF Mono, Menlo.

---

## Provenance

| | |
| --- | --- |
| Template | Acxiom Master Template, version 1.0 |
| Dated | January 2026 |
| Brand contact | acxiombrand@acxiom.com |

Slides marked `© 2026` are on this template. Slides marked `© 2025` are the previous one — still
on brand, but **do not mix slides between the two**.
