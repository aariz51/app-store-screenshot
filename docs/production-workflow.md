# 05 — Production Workflow (Deliverable 6)

[INF] Nothing in the files shows which tools the original designers used. The pipeline below **reproduces** the observed results. It does not claim to be how they were made.

## Recommended stack
| Need | Primary | Alternative |
|---|---|---|
| Real UI capture | `goldie` (drives the app on a simulator) or `xcrun simctl io booted screenshot` | Flutter `integration_test` screenshots |
| Composition (code, repeatable) | **HTML/CSS canvas at 1320×2868 rendered with Playwright** (headline, gradient, device PNG, callouts as cropped real-UI PNGs) | Figma (auto-layout frames per tile) |
| Device frames | Apple Design Resources product bezels (licensed for marketing) | Figma community mockups (check licence) |
| 3D objects | Blender / Spline renders with transparent background | Licensed 3D icon packs; AI image gen (no faces) |
| Photo + hand compositing | Photoshop (screen replace with perspective warp) | Figma + a flat hand PNG |
| Batch export + validation | Script: check sizes, sRGB, no alpha, file size | — |

A code-based compositor fits this system best: tokens map straight to CSS, every tile is reproducible, and copy changes and localisation are a re-render, not a redesign.

## Pipeline

1. **Feature selection.** List every real feature, then rank by (a) the reason people download, (b) differentiation, (c) visual demonstrability. Keep 5–8. Nothing that does not exist in the build.
2. **Headline development.** For each feature, write a benefit headline of 2–6 words (formulas in `06-generation-blueprint.md`) plus an optional sub-line of 8 words or fewer. Run `humanizer`. Check every word against the product.
3. **Storyboard.** Fill the storyboard table (06). Assign a layout ID (L1–L12) to each tile and check the rhythm rule.
4. **Canvas prep.** Build 1320×2868 frames. Set guides: safe 6% inset, text margin 8% or 12%, headline top 6.5%.
5. **Typography.** Pick the display + text pair (brand font first, otherwise the archetype hint). Test the longest headline at thumbnail scale (220 px wide). Lock size per tile, so all tiles share one headline size unless a tile is deliberately the hero.
6. **Background.** Apply the field gradient tokens. On coloured fields, check that headline contrast is at least 4.5:1 (computed: white on `#FDA273` is about 2.0:1, which is why A's white headline relies on its sheer size. [REC] Darken the field or the text if the headline is under 15cw).
7. **Device mockup.** Place the real screenshot in the bezel, at its exact pixels with no rescale blur (render the screen at device-native resolution, then scale the composite once). Crop by moving the device past the canvas edge, never by masking the screen.
8. **UI extraction for callouts.** Crop the real component from a **higher-resolution capture** (simulator at 3×) so a 1.1–1.25× enlargement stays sharp. Keep it pixel-identical. Rounded mask = the component's own radius.
9. **Floating UI.** Place callouts so they are wider than the device (up to 94cw), overlap the device by 20–40% of their own height, and rotate 0–3° only if the archetype allows.
10. **Decorative assets.** At most 3 per tile; render or source them with transparent backgrounds; check they cannot be mistaken for features (a 3D car icon on an insights tile is a category symbol, not a feature).
11. **Light & shadow.** Use the tinted shadow tokens. One light direction (top) for the whole set. On dark fields, swap shadows for strokes and glow.
12. **Composition pass.** Check the reading order: key word → rest of headline → focal callout → device → decoration. Squint test: the headline should still be the first read.
13. **Colour grade.** Unify the warmth of photos and 3D renders to the field (a slight brand-hue overlay at 5–8%, soft-light).
14. **Export.** PNG, sRGB, flattened, no alpha, exact pixel size, 1 file per tile, numbered `01_…png`.
15. **QA.** Run `07-qa-checklist.md` plus the validation script, and make a contact sheet of all tiles at thumbnail size.

## Recipes for signature techniques

**Panorama pair (A tiles 1–2).** Build one 2640×2868 artboard. Place the device at about 150% of tile width, rotated −8°, centred on x = 1320, then slice it into two 1320 frames. Check that each half still reads alone: tile 1 must not depend on tile 2's headline.

**Magnified callout (A, C).** Duplicate the real component crop at 1.15× and place it over the same spot on the device. Add `card_on_light` shadow and 4.5cw radius. Optional: a 2–3° tilt and a 1 px white inner stroke for separation on white UI.

**Neon card (D).** Set the card fill 4% lighter than the background, add a 2 px accent stroke, and an outer glow (accent @55%, blur 4cw) at 60% opacity. Put a blurred radial blob in a second accent behind it.

**Two-tone headline.** Split the headline into spans. The key word (the one carrying the benefit or the keyword) gets `brand.primary`; everything else gets `ink`. Exactly one coloured span per headline.

**Hand-held (A6).** Use a hand-only stock photo or 3D hand (no face). Perspective-warp the screen into the device, add a screen glare gradient (white 0→8%), and match the shadow direction.

**Before/After (F).** Two identical card templates side by side or stacked; tags in semantic red/green; numbers taken from real product output for the same real item; on-tile footnote if the numbers are examples.

## Automating the compositor (sketch)
```
tiles.yaml (storyboard) + tokens.json + ui/*.png
      → render_tile.html (template per layout ID)
      → playwright screenshot @1320x2868, deviceScaleFactor 1
      → validate.py (size, mode RGB, no alpha, ≤ 8 MB)
      → contact_sheet.png (all tiles at 220 px wide)
```
