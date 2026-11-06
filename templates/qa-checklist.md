# 07 — Quality Assurance Checklist (Deliverable 10)

Tick every line for every tile. One fail blocks handoff.

## Technical (automate)
- [ ] Exact pixel size for the target slot (6.9″: 1320×2868 or 1290×2796; 6.5″: 1284×2778 or 1242×2688; iPad 13″: 2064×2752 or 2048×2732). Re-check Apple's current list before delivery.
- [ ] PNG or JPEG, sRGB, **no alpha channel**, flattened.
- [ ] Consistent orientation across the set; at most 10 per locale.
- [ ] File names ordered `01_…` to `10_…`.

## Accuracy
- [ ] Every headline claim maps to a real, shipped feature.
- [ ] Every UI pixel inside a device or callout comes from a real build capture.
- [ ] Numbers, ratings, awards and "#1" have a written source, or are removed.
- [ ] No placeholder or lorem text; demo data is realistic and non-personal.
- [ ] No third-party logos without a shipped integration.
- [ ] No human faces anywhere.
- [ ] No paywall, onboarding or splash screens (unless asked).

## Readability
- [ ] Contact sheet at 220 px wide: every headline readable, key word visible.
- [ ] Headline contrast ≥ 4.5:1, or headline ≥ 15cw heavy (large-text exception ≥ 3:1).
- [ ] Sub-line ≤ 2 lines, ≥ 52 px at 1320 w.
- [ ] Headline has 2–6 words; exactly one coloured key word.

## Composition
- [ ] Text stays inside the 6% safe inset.
- [ ] Headline top and side margins identical across tiles (± 4 px).
- [ ] Headline size identical across tiles unless the hero is deliberately different.
- [ ] Device scale consistent per layout family; crop never cuts a key UI element mid-line.
- [ ] Callouts show complete components edge to edge; no half-cut text.
- [ ] At least 2 layout families alternate; no two identical tiles (D's duplicate is the anti-pattern).
- [ ] Panorama: each half reads alone; the seam does not cut text.
- [ ] No more than 3 decorative objects per tile.

## Rendering
- [ ] One light direction for the whole set; shadows are tinted, not grey, on coloured fields.
- [ ] Screens are sharp at 100% zoom (no upscaled UI); device bezel edges are clean.
- [ ] Gradients have no banding (add 1–2% noise if needed).
- [ ] 3D renders and photos colour-graded to the field.

## Story
- [ ] Tiles 1–3 answer: what it is · why it's different · what you do.
- [ ] Tile 1 contains the category keyword and the brand name.
- [ ] The sequence ends on mastery or progress, not on a minor feature.
- [ ] All copy passed `humanizer`.

## Comparison
- [ ] Placed next to the top 3 competitors' first three screenshots: visibly different in colour, layout, or both.
