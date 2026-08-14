# Acxiom Brand Design System — Claude Design Handoff
**Source: Acxiom Master Template v1.0, January 2026**
**Purpose: This file is the source of truth for all Acxiom-branded design work. Follow these rules exactly. When a rule here conflicts with your default design instincts, this file wins.**

---

## 1. Brand Voice and Positioning

- Tagline: "We put data to work — so brands can realize the greatest value from data and technology."
- Design language: dark, cinematic, precise. Black canvases with aurora-style gradient light (magenta into blue). Technical monospace labels paired with clean geometric headlines.
- The 2026 template is an iteration, not a rethink. Brand core remains the same, aligned with the Omnicom Media story for one consistent client journey.

---

## 2. Typography

The brand typeface is **Sofia Pro**. TW Cen MT exists only as the PowerPoint-embedded substitute where Sofia Pro can't be installed. **In all design, web, and digital contexts, use Sofia Pro — never TW Cen MT.** Consolas is the monospace label face across all contexts.

| Role | Typeface | Context | Rules |
|---|---|---|---|
| Headlines, subheadings, body | Sofia Pro | Design, web, digital, video, all Claude Design output | Sentence case for headlines ("Our template just leveled up."). Never increase headline or subheading sizes relative to the type scale. Body text size may be adjusted. |
| Headlines, subheadings, body | TW Cen MT | PowerPoint decks ONLY (embedded substitute) | Same rules as Sofia Pro. Never use in web/design work. |
| Labels, eyebrows, metadata, section tags | Consolas | All contexts | ALWAYS ALL CAPS. Always letterspaced (wide tracking, approx 0.2em–0.3em). Used for eyebrow labels like "THE CHALLENGE", "IN THIS SECTION", "MASTER TEMPLATE 2026", footer copyright lines, timeline highlights, chart titles. |

**TODO: confirm Sofia Pro weights in use against the brand asset repo.** Suggested mapping until confirmed:
- Display/headlines: Sofia Pro Light or Regular (the template's headline voice is light and geometric)
- Subheadings: Sofia Pro Regular or Medium
- Body: Sofia Pro Regular
- Emphasis: Sofia Pro Semi Bold (use sparingly; no faux bold)

Font stacks:
- Sofia Pro → `"Sofia Pro", "sofia-pro", "Century Gothic", Futura, sans-serif` (self-host licensed files from the repo, or load via Adobe Fonts `sofia-pro`)
- Consolas → `Consolas, "SF Mono", "JetBrains Mono", monospace`

Typography patterns observed in the template:
- Eyebrow label (Consolas, all caps, letterspaced) sits ABOVE the content it describes
- Large display headlines are Sofia Pro (TW Cen MT in decks) in off-white on dark backgrounds
- Section numbers rendered huge in Consolas (e.g. "01") in the top-right of section dividers

---

## 3. Color System

**TODO before first use: replace approximate hex values below with exact values from the brand asset repo / PowerPoint color selection tool. Approximations are sampled visually from the template PDF.**

### Core palette

| Token | Approx Hex | Usage |
|---|---|---|
| `--acxiom-black` | `#000000` | Primary dark background |
| `--acxiom-ink` | `#2B2233` (approx, dark plum) | Dark boxes, bullet chips, secondary dark fill |
| `--acxiom-paper` | `#EDEBE6` (approx, warm off-white) | Light background, text on dark |
| `--acxiom-white` | `#FFFFFF` | Text on dark, light box fill |
| `--acxiom-magenta` | `#FF0099` (approx, hot pink) | Primary accent, gradients, chart series, project bars |
| `--acxiom-blue` | `#1F1FFF` (approx, pure blue) | Secondary accent, gradients, chart series |
| `--acxiom-orange` | `#FF6B35` (approx) | Tertiary accent (flow chart key, circle gradients) |
| `--acxiom-gray` | `#C8C8C8` (approx) | Table headers, muted chart segments |

### Hard rules
- Text is ONLY black or white (off-white/paper counts as white). Never colored text. No magenta headlines, no gradient text.
- Colors come only from the pre-built palette above. Do not invent tints, shades, or new hues.
- Accent colors are for: gradients, borders, chart fills, bars, keys, and shape strokes — never type.

### Signature gradients
- **Aurora glow**: magenta → violet → blue, radiating from a corner or edge of a black canvas. Used on covers, section dividers, closing slides, and as the "photo glow" overlay.
- **Gradient strokes**: 1–2px box/circle outlines that transition between two accent colors (e.g. orange→magenta, blue→cyan, magenta→violet). Fills stay transparent or solid; gradients live on the stroke.
- **Timeline gradient**: horizontal rule running magenta → violet → blue, left to right.

---

## 4. Logo

- Wordmark: "ACXIOM" in the custom geometric letterform (A rendered as caret shape /\, X as crossing strokes).
- On dark: white logo. On light: black logo.
- Footer: display ONLY the Acxiom logo, bottom-right. Never client logos in footers.
- Client logos: allowed only on cover/case-study lead slides, top-right (see Heathrow case study layout).
- Dotted-dot motif (small dot matrix arrow/glyph) appears top-left on branded dark slides next to the eyebrow tag.

---

## 5. Iconography — Dotted Icons

All icons are built from dot matrices (small circular dots forming a pictogram). No stroke icons, no filled icons, no third-party icon sets (no Lucide, no Font Awesome) in Acxiom-branded work.

- Icon library (from template): Credit cards, Customer, Data, Direct mail, AI, Document, Telco, Data file, Growth, CPG, Thumbs up, Banking, Headphones, Storefront, Heart, Household, Key, Landline, Laptop, Legal, Location, Connected TV, Chat/Message, Automotive, Lock, Mail, Manufacturing, Manufacturing 2, Megaphone, Money, Music, Travel, Privacy, Cloud, Calendar, Analytics, Smartphone, Shopping cart, Retail, Service, Search, Speech bubble, Revenue, Restaurant, Trophy, Clock, Clean room, Bot/AI, Reverse arrows, Health, Equal, X symbol, Quote mark, Check, Versus, Directional, No symbol, Yes symbol, Churn, Question mark
- Icons render white-on-dark or black-on-light.
- **Asset rule: pull dotted icon SVGs/PNGs from the GitHub assets repo. Do not redraw or approximate them with other icon styles. If an icon is missing, flag it rather than substituting.**

### Dotted icon bullets
- Bullet pattern: small square chip (ink/dark plum fill) containing a dotted icon, followed by a Consolas all-caps letterspaced label on a subtle horizontal band.
- Dark slides: dark chip + dark translucent band. Light slides: dark chip + white band.

---

## 6. Layout System

### Slide/canvas anatomy (16:9)
- **Top-left**: page title in TW Cen MT (dark slides: off-white; light slides: black), or dot-glyph + eyebrow tag on section/cover slides
- **Bottom-left**: page number + `| © 2026 Acxiom LLC Confidential` in small muted type
- **Bottom-right**: Acxiom logo
- Generous margins; content breathes. Never crowd the footer zone.

### Key layouts in the system
1. **Cover**: black + aurora glow, logo top-left, dot glyph top-right, massive display title lower-left, Consolas metadata (version, date)
2. **Statement slide**: centered oversized TW Cen MT statement on black + corner glow
3. **Section divider**: giant Consolas section number top-right in glow, display title lower-left, "IN THIS SECTION" Consolas eyebrow + short description lower-right
4. **Content light**: paper background, black title top-left, subtle gray dot-motif watermark lower-right
5. **Content dark**: black background, white title, glow lower-right
6. **Split case study**: left half paper with eyebrow-labeled sections (CASE STUDY / INDUSTRY, THE CHALLENGE, OUR APPROACH, THE RESULTS), right half full-bleed photo with glow overlay; client logo top-right; oversized stat numbers in accent-adjacent display treatment with small body captions
7. **Photo glow**: full-bleed photo with the magenta aurora gradient overlaid on the lower portion (copy/paste glow asset over image; re-place logo on top if covered)

### Flow charts
- Boxes: thin-stroke rectangles (solid black/white stroke, or gradient stroke), solid fills in blue, black, ink, magenta, or white. Text inside follows the black/white text rule (white text on dark fills, black on light).
- Circles: thin gradient-stroke circles, transparent fill.
- Lines: solid arrows (primary flow), dashed arrows (secondary/optional flow), curly braces for grouping, curved fork arrows for branching.
- Endpoints can be dotted icons with small labels.
- Key/legend: small color swatch squares + label.

### Timelines
- Horizontal gradient rule (magenta→blue), node dots on the line, vertical tick lines dropping to labels.
- Milestone labels above the line: Consolas all caps, numbered ".01 / .02 / .03 / .04" + "HIGHLIGHT HERE" style.
- Node labels below in TW Cen MT.

### Tables / project plans (Gantt)
- Header row: ink/dark plum fill, white text (quarters), second row gray fill (months).
- Row labels: gray fill cells.
- Bars: arrow-ended (pentagon) bars in magenta, blue, ink; white label text inside bars.
- A vertical "today" line may cross the chart.

### Charts
- Column charts: series colors in order — blue, magenta, ink. Light gray gridlines, no chart junk.
- Pie/donut: magenta (dominant), blue, gray, ink. Donut style with callout labels.
- Chart titles: Consolas all caps letterspaced.
- Legends: small squares + TW Cen MT labels.

---

## 7. Motion and Media

- Use only standard, pre-selected transitions and animations. No complex or custom animation in deck contexts. (Web contexts: keep motion minimal and purposeful; subtle fades, no gimmicks.)
- Use standard image compression. Do not run additional compression passes on images.

---

## 8. Dos and Don'ts (verbatim rules from brand team)

**DO**
- Use this 2026 system for all new materials
- Use the full 2026 template OR the full 2025 template — never mixed
- Use embedded fonts and sizes; Consolas always all caps
- Use only pre-built palette colors; text only black and white
- Only the Acxiom logo in footers
- Standard transitions, standard image compression

**DON'T**
- Don't mix 2025 and 2026 template slides (check the copyright year in the footer to identify version)
- Don't use any fonts other than TW Cen MT and Consolas
- Don't increase headline/subheading sizes (body only)
- Don't use colors outside the palette; don't color text
- Don't put client logos in footers (cover slides only)
- Don't add slide transitions or complex animation
- Don't compress images beyond standard

---

## 9. Asset Manifest (GitHub repo)

**TODO: update paths to match actual repo structure.**

```
/assets
  /logos          → acxiom-wordmark-white.svg, acxiom-wordmark-black.svg
  /icons          → dotted icon set (59 icons, see §5 list)
  /gradients      → aurora glow PNGs (cover, corner, photo-glow overlay)
  /motifs         → dot-matrix glyph / watermark
  /fonts          → Sofia Pro (licensed web files), Consolas; TW Cen MT for deck contexts only
ACXIOM-BRAND.md   → this file (keep at repo root so it is read first)
```

---

## 10. Execution Checklist for Claude Design

Before delivering any Acxiom-branded artifact, verify:

- [ ] Sofia Pro + Consolas only (TW Cen MT permitted in PowerPoint decks exclusively); Consolas is all caps and letterspaced
- [ ] All text is black or white — zero colored text
- [ ] All colors are from §3; gradients are magenta/blue/violet aurora family
- [ ] Icons are the dotted set from the repo, not substitutes
- [ ] Footer: page number + copyright left, Acxiom logo right, nothing else
- [ ] Eyebrow labels follow the Consolas-above-content pattern
- [ ] Dark canvases use the aurora glow sparingly (one corner/edge, not everywhere)
- [ ] Headline sizes untouched from template scale
- [ ] No transitions/animations beyond the standard set
- [ ] Copyright line reads © 2026 (confirms 2026 system, not 2025)
