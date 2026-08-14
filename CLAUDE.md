# Working with the Acxiom design system

This repository is a brand asset library, not an application. There is no build, no test suite,
and no runtime. Treat it as the source of truth when producing anything that has to look like
Acxiom — decks, web pages, artifacts, diagrams, social assets.

## Where things are

| Need | File |
| --- | --- |
| Colors, type, spacing as data | `design-system/tokens/tokens.json` |
| Same, ready to drop into code | `tokens.css` · `tokens.scss` · `tailwind.preset.js` |
| The rules, in prose | `design-system/brand-guidelines.md` |
| Every asset, queryable | `design-system/assets.json` |
| Icon lookup with search aliases | `design-system/icons.md` |
| Original decks | `reference/` |

`tokens.json` is the source of truth. `tokens.css`, `tokens.scss`, and `tailwind.preset.js` are
hand-maintained views of it — if you change a value, change it in all four.

## The rules that matter most

These come from the master template's own dos-and-don'ts page. They are not stylistic
preferences.

1. **Two typefaces only** — Tw Cen MT and Consolas. Nothing else.
2. **Consolas is always ALL CAPS**, widely tracked. Never sentence case, never body copy.
3. **Text is black or white only.** Accent colors never carry type.
4. **Bone is not white.** `#EDECE8` is the light background. Do not swap in `#FFFFFF`.
5. **Do not enlarge headlines or subheadings.** Body text is the only size you may adjust.
6. **The logo goes in the footer only,** and is never recolored, stretched, or boxed.
7. **No custom animation or slide transitions.**

## Composing a layout

The native canvas is 960 × 540pt with a 28.8pt margin. A slide or page section is usually:

```
E Y E B R O W   K I C K E R          ← Consolas, 11pt, uppercase, 0.25em tracking
Headline in sentence case            ← Tw Cen MT, 28pt (72pt for covers/dividers)
Body copy underneath.                ← Tw Cen MT, 14pt
```

Dark compositions use black or plum with white body and bone headlines. Light compositions use
bone with black text. Accent color enters through charts, diagram shapes, and the glow — not
through type.

The glow is the one hero effect. Reach for it on covers and hero moments, not on content:

```css
background: linear-gradient(75deg, #000000 0%, #2A182E 35%, #940BE0 70%, #FF00A9 100%);
```

## Charts

Series step through the palette in this fixed order: blue `#1A12F7`, magenta `#FF00A9`,
plum `#2A182E`, grey `#C6C6C3`. Hairline horizontal gridlines only, no chart border, no 3D. Pie
charts are drawn as donuts with external leader lines.

## Picking assets

Read `design-system/assets.json` rather than globbing the directories — it carries labels,
categories, and search aliases the filenames don't. Icons come in mirrored black and white sets:
**black on light surfaces, white on dark.**

Prefer the SVG logo (`assets/logo/svg/`) for anything that scales. EPS is for print handoff only.

## Changing assets

After adding, renaming, or removing anything under `assets/`:

```bash
python3 design-system/scripts/build-manifest.py
```

New icons also need a row in the `ICONS` table at the top of that script, or they will be
skipped with a warning.

## When something isn't specified here

Check `reference/AcxiomMasterTemplate_2026.pdf` first — it is the authority, and
`AcxiomValueDeck_2026.pdf` shows the system applied across 95 pages. If neither settles it, say
so rather than inventing a rule; brand questions go to acxiombrand@acxiom.com.
