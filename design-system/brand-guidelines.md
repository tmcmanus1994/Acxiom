# Acxiom Brand Guidelines

Distilled from **AcxiomMasterTemplate_2026.pdf** (Master Template v1.0, January 2026) and
**AcxiomValueDeck_2026.pdf**. Both source PDFs live in [`../reference/`](../reference/).

Brand questions that this document does not answer go to **acxiombrand@acxiom.com**.

---

## 1. The idea

> "One look. One experience."

The 2026 template is a new *expression* of the brand, not a new brand. It exists to make every
Acxiom touchpoint — deck, web, social, Teams call — read as one continuous experience, aligned
to the Omnicom Media story. The full site launch follows in 2026.

Visually the system is built from four moves:

1. **A black canvas cut by an angled beam of light** (the glow) for covers and hero moments.
2. **A warm bone field** (`#EDECE8`) for everything that has to be read.
3. **Geometric sans headlines** in Tw Cen MT, set large and light, never shouty.
4. **A monospaced, wide-tracked uppercase kicker** in Consolas above the headline.

If a layout has those four things in the right proportion, it looks like Acxiom.

---

## 2. Color

Text is **black or white only**. Accent colors are for data, diagrams, and highlights — never
for type.

### Core

| Token | Hex | Role |
| --- | --- | --- |
| `black` | `#000000` | Primary dark surface. Covers, section dividers, hero moments. |
| `bone` | `#EDECE8` | Primary light surface. Warm off-white — the default content background. |
| `white` | `#FFFFFF` | Body text on dark surfaces; fills inside charts and diagrams. |
| `plum` | `#2A182E` | Deep aubergine. Secondary dark surface, card fills, third chart series. |

**Bone is not white.** Do not substitute `#FFFFFF` for `#EDECE8` as a page or slide background —
the warmth of the bone is what keeps the palette from reading cold and generic.

### Accent

| Token | Hex | Notes |
| --- | --- | --- |
| `magenta` | `#FF00A9` | Signature accent. First choice for emphasis; lead pie/donut series. |
| `blue` | `#1A12F7` | Second accent. Leads the column chart series order. |
| `orange` | `#FF672D` | Third accent, used least. Diagram keys and gradient stops. |

### Neutral

| Token | Hex | Role |
| --- | --- | --- |
| `grey` | `#C6C6C3` | Chart neutral, table rules, inactive states on light. |
| `grey-dark` | `#A0A0A0` | Secondary label text on light surfaces. |
| `bone-shade` | `#D8D6D0` | Dividers and hairlines on bone. |

### Gradient stops

`cyan #00E1FD` and `violet #940BE0` are **endpoints only**. They appear inside the glow and the
gradient strokes on flow-chart shapes. Do not use either as a flat fill.

### Chart series order

Charts step through the palette in this fixed order:

1. `blue #1A12F7`
2. `magenta #FF00A9`
3. `plum #2A182E`
4. `grey #C6C6C3`

### Contrast

`bone` on `black` and `black` on `bone` both clear WCAG AA comfortably. The accents do **not** —
`magenta`, `blue`, and `orange` are decorative and are never asked to carry text. When an accent
sits behind a label, that label is white or black, whichever the accent supports.

---

## 3. Typography

**Two typefaces. No exceptions.**

### Tw Cen MT — headlines and body

A geometric sans (Monotype). Carries every headline, every paragraph, every caption. Almost
always Regular weight; Bold appears rarely, Italic rarer still.

Web fallback stack, closest first:

```
"Tw Cen MT", "Twentieth Century", Futura, "Century Gothic", Questrial, sans-serif
```

### Consolas — kickers and labels

The monospaced counter-voice. **Consolas is always set in ALL CAPS** with wide tracking. It is
never used for body copy and never set in sentence case.

```
Consolas, "Cascadia Mono", "SF Mono", Menlo, monospace
```

### Scale

Sizes are points on the native 960×540pt slide, which map 1:1 to px in a 960×540 web frame.

| Style | Face | Size | Tracking | Case | Use |
| --- | --- | --- | --- | --- | --- |
| `display` | Tw Cen MT | 72 | 0 | Sentence | Cover and section-divider headline |
| `title` | Tw Cen MT | 32 | 0 | Sentence | Oversized standalone statement |
| `heading` | Tw Cen MT | 28 | 0 | Sentence | Standard slide headline |
| `lead` | Tw Cen MT | 16 | 0 | Sentence | Opening paragraph, pull copy |
| `body` | Tw Cen MT | 14 | 0 | Sentence | Body copy |
| `body-sm` | Tw Cen MT | 12 | 0 | Sentence | Diagram and table labels |
| `caption` | Tw Cen MT | 10 | 0.05em | Sentence | Icon captions, chart axis labels |
| `eyebrow` | Consolas | 11 | 0.25em | UPPER | The kicker above a headline |
| `label` | Consolas | 8 | 0.35em | UPPER | Bullet keys, micro-labels |
| `footer` | Consolas | 10 | 0.15em | UPPER | Copyright line and page number |

Tracking widens as Consolas gets smaller — 0.15em at 10pt, 0.25em at 11pt, 0.35em at 8pt.

**Do not increase headline or subheading sizes.** Body text is the only size you may adjust.

---

## 4. Layout

The native canvas is a 16:9 slide at **960 × 540 pt**.

| Measure | Value |
| --- | --- |
| Margin (left/right) | 28.8pt (0.4in) |
| Headline cap height from top | 19.2pt |
| Footer baseline from bottom | ~24pt |
| Space scale | 4pt base — 4, 8, 12, 16, 24, 28.8, 32, 48, 64 |

### Slide anatomy

```
┌────────────────────────────────────────────────────────────┐
│  ← 28.8pt                                                  │
│  Slide headline                          (28pt, Tw Cen MT) │
│                                                            │
│  E Y E B R O W   K I C K E R           (11pt Consolas UC)  │
│  Body copy sits under the eyebrow.        (14pt Tw Cen MT) │
│                                                            │
│                                          ░ dotted-grid     │
│                                            watermark       │
│  12 | © 2026 ACXIOM LLC CONFIDENTIAL           ACXIOM ◀ logo│
└────────────────────────────────────────────────────────────┘
```

The eyebrow sits **above** the copy it introduces, not above the headline, on content slides.
On covers it sits directly beneath the display headline.

### Footer

Every content slide carries: page number, `© 2026 ACXIOM LLC CONFIDENTIAL` in tracked uppercase
Consolas at the left, and the Acxiom wordmark at the right. On the closing slide the footer
also carries `acxiom.com` and the positioning line:

> We put data to work — so brands can realize the greatest value from data and technology.

### Dotted-grid watermark

A sparse field of dots, derived from the same dot language as the icon set, sits low-contrast in
the lower-right of content slides and top-right of covers. It is decoration — keep it faint and
never let it collide with content.

---

## 5. Logo

Two variants ship, in three formats each:

| Variant | Use on |
| --- | --- |
| `acxiom-logo-black` | bone, white, and other light surfaces |
| `acxiom-logo-white` | black, plum, imagery, and the glow |

- **SVG** for web and anything that scales. Source aspect ratio `802.22 × 124.81` (≈6.43:1).
- **PNG** at 3344 × 521 with transparency, for raster contexts.
- **EPS** for print and vendor handoff.

Rules:

- The logo appears **in the slide footer only**. Do not place client logos in the footer — client
  logos belong on cover slides where available.
- Never recolor the wordmark. Black or white, nothing else.
- Never stretch, rotate, add effects, or box the wordmark.
- If the glow passes over the logo, paste the logo again on top so it stays legible.

---

## 6. Iconography

The icon set is **dotted-line style** — forms drawn from dot fields rather than solid strokes.
It comes in two variants that mirror each other exactly.

| Set | Count | Path |
| --- | --- | --- |
| Dotted icons, black | 60 | `assets/icons/dotted/black/` |
| Dotted icons, white | 60 | `assets/icons/dotted/white/` |
| Dotted bullets, black | 19 | `assets/icons/bullets/black/` |
| Dotted bullets, white | 19 | `assets/icons/bullets/white/` |

All icons are 285 × 285 px PNG with transparency. Use **black on light surfaces, white on dark**.
Typical placed size is ~48pt on a slide; bullets sit around 20pt.

Full searchable index: [`icons.md`](./icons.md). Machine-readable: [`assets.json`](./assets.json).

---

## 7. Imagery

### Photo glow

The glow is the brand's one hero effect: an angled beam of magenta-through-violet light across a
dark image or a black field. In the PowerPoint template it ships as a pasteable PNG overlay —
copy it directly on top of the image. In web and print work, reproduce it with the gradient ramp:

```css
background: linear-gradient(75deg, #000000 0%, #2A182E 35%, #940BE0 70%, #FF00A9 100%);
```

If the glow lands over the logo, paste the logo on top of the glow as well.

### Backgrounds

| Set | Size | Path |
| --- | --- | --- |
| Teams backgrounds | 8001 × 4501 | `assets/backgrounds/teams/` |
| Desktop wallpapers | 3840 × 2160 (4K) | `assets/backgrounds/desktop/` |

### Compression

Use the template's **standard image compression**. Do not leave images uncompressed.

---

## 8. Charts, tables, and diagrams

- **Column and bar charts** — series in palette order (blue, magenta, plum, grey). Hairline
  horizontal gridlines in `grey`, no vertical gridlines, no chart border, no 3D.
- **Pie charts** are drawn as **donuts**, with external leader lines to labels.
- **Flow charts** ship in light and dark variants. Boxes are square-cornered; fills are blue,
  black, plum, magenta, or bone with a 1pt accent or gradient stroke. Circles use gradient
  strokes (cyan→magenta, magenta→violet, orange→violet).
- **Lines** are black, solid or dashed, with simple arrowheads.
- **Keys** use a solid swatch plus a body-sm label.
- **Journey/timeline** blocks are numbered `.01 .02 .03 .04` in tracked Consolas, each with an
  uppercase highlight and body copy beneath.

---

## 9. Motion

Use the standard, pre-selected slide transitions and animations only. **No custom transitions,
no complex animation.**

---

## 10. Dos and don'ts

Transcribed from the master template.

| Do this | Not this |
| --- | --- |
| Use this template for any new materials from 2026 onward. No need to retrofit non-mission-critical decks. | Don't assume 2025 is off-brand — it isn't, it's just a different expression. |
| Use the full 2026 template **or** the full 2025 template. | Don't mix slides from the new and old templates. Check the year on the footer copyright line to see which you're in. |
| Use the fonts and font sizes embedded in the template. Consolas always stays in all caps. | Don't use fonts outside the template. Only Tw Cen MT and Consolas. Don't increase headline or subheading sizes — body text only. |
| Use the colors pre-built into the color selection tools. For text, only black and white. | Don't use colors outside the color selection tool or presentation toolkit. Don't use color for text. |
| Display only the Acxiom logo in the footer. | Don't add client logos to slide footers — cover slides only. |
| Use the standard, pre-selected slide transitions and animations. | Don't add slide transitions or complex animation. |
| Use the standard image compression. | Don't leave images uncompressed. |

---

## 11. Voice

Short declaratives. Lowercase confidence rather than exclamation. The house line:

> **We put data to work — so brands can realize the greatest value from data and technology.**

Headlines in the template read like: *"Our template just leveled up."* · *"Where we're headed"* ·
*"Trust & intelligence at scale."* — plain-spoken, present tense, no jargon stacking.
