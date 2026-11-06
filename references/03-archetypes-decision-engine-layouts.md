# 03 — Archetype Library, Decision Engine, Layout Library (Deliverables 7, 9-B, 9-C)

## A. Design archetype library

Each archetype is derived from one or more references but is written to stay independent of them.

### ARC-1 "Warm Companion" (from A)
- **Personality:** reassuring, relational, premium-friendly.
- **Fits:** personal finance, couples/family, wellness habits, journaling, home and lifestyle.
- **Colour:** one warm mid-saturation brand colour as a soft vertical gradient (Δ luminance about 6%), alternating with a warm cream. Headline: brand colour plus a warm near-black.
- **Type:** heavy grotesk, title case, left-aligned, two-tone (one key word in brand colour), tight tracking.
- **Device:** front-on, cropped; one giant tilted hero device may straddle tiles 1→2.
- **Decoration:** magnified real UI cards; at most 3 soft 3D category objects.
- **Layout:** L1, L3, L4, L7.
- **Story:** identity → differentiator → features → mastery.
- **Strengths:** reads premium, adapts to almost any consumer app. **Weaknesses:** can look generic if the brand colour is a default orange or blue; depends on high-quality UI.

### ARC-2 "Playful Loop" (from B)
- **Personality:** energetic, rewarding, cute.
- **Fits:** gamified habits, kids or education, fitness challenges, screen-time, language learning — only if the app really has a character or reward economy.
- **Colour:** saturated primary (blue, purple, green) + gold reward colour + white rest tiles.
- **Type:** heavy rounded display, word-level size jumps, emoji or glyph substitution.
- **Device:** front, cropped; objects break the tile edges.
- **Decoration:** mascot (must already exist in the brand), 3D rewards, clouds.
- **Layout:** L2, L5, L8.
- **Story:** promise → each step of the loop → progress proof.
- **Weaknesses:** looks childish for serious categories; conflicts with the no-stickers contract, so **opt-in only**.

### ARC-3 "Bold Utility" (from C)
- **Personality:** confident, direct, one job done well.
- **Fits:** converters, exporters, scanners, PDF tools, VPNs, cleaners, keyboards.
- **Colour:** one saturated brand field on every tile, white type, a lighter vignette behind the device.
- **Type:** ALL-CAPS heavy condensed, centred; big benefit + small qualifier.
- **Device:** front + an enlarged key sheet or menu; 3D format icons for the inputs and outputs.
- **Story:** authority → what goes in → what comes out → quality.
- **Weaknesses:** shouty, and ages fast. Relies on claims ("#1") that need proof. Trademark risk with third-party logos.

### ARC-4 "Night Manifesto" (from D)
- **Personality:** intimate, edgy, exclusive, private.
- **Fits:** dating, social, nightlife, music, privacy and security, gaming, AI companions (with care).
- **Colour:** near-black with a purple or blue tint + 1–2 neon accents; glow instead of shadow.
- **Type:** ALL-CAPS condensed, short declaratives with full stops, one neon word.
- **Device:** zig-zag top and bottom crops; outlined neon cards.
- **Decoration:** masks or abstract avatars (fits the no-faces rule), glow blobs, a single symbolic object (moon, lock).
- **Story:** value → mechanism → safety.
- **Weaknesses:** poor for daytime or family categories; contrast must be checked on grey text.

### ARC-5 "Editorial Bento" (from E)
- **Personality:** curated, design-literate, calm.
- **Fits:** creative tools, photo or video editors, templates, design apps, note-taking, AI generators.
- **Colour:** light neutral tiles; colour comes from user-generated output; 1–2 step colours.
- **Type:** condensed caps or editorial grotesk, centred, numbered steps.
- **Device:** used sparingly; bento cells show inputs and outputs directly.
- **Story:** tutorial — promise → inputs → step 1 → step 2 → result.
- **Weaknesses:** needs strong sample content (which must come from the real product); low colour contrast can be weak at thumbnail size.

### ARC-6 "Proof First" (from F)
- **Personality:** friendly, smart, outcome-driven.
- **Fits:** health, nutrition, fitness, savings, productivity — any app with a **measurable outcome**.
- **Colour:** hero colour on tile 1 only, white after; green/red reserved for semantic before/after.
- **Type:** rounded-geometric bold, sentence case, lead-in + main line, hand-drawn underline accent.
- **Device:** front, cropped; chips break the device edge.
- **Story:** quantified outcome → how → breadth → depth.
- **Weaknesses:** every number must be real and reproducible. Laurels need a source.

## B. Design decision engine

Score each archetype 0–3 on each input, multiply by the weight, and pick the highest. **Break a tie toward the archetype that shows more real UI.** Never pick on attractiveness.

| Input (weight) | ARC-1 Warm | ARC-2 Playful | ARC-3 Utility | ARC-4 Night | ARC-5 Editorial | ARC-6 Proof |
|---|---|---|---|---|---|---|
| Category match (×3) | finance, family, wellness | habits, kids, games | tools | dating, social, privacy | creative | health, outcome |
| Audience age (×1) | 25–45 | 8–30 | any | 18–35 | 20–40 creatives | 25–50 |
| Emotional target (×2) | safe, close | fun | efficient | thrilling, discreet | inspired | confident |
| Existing brand (×3) | warm palette | has mascot | 1 strong colour | dark UI | neutral UI + rich content | bright brand |
| UI is dark mode (×2) | 0 | 0 | 1 | 3 | 1 | 0 |
| Has measurable outcome (×2) | 1 | 1 | 1 | 0 | 0 | 3 |
| Workflow needs teaching (×1) | 1 | 2 | 2 | 1 | 3 | 1 |
| House-contract compatibility (×2) | 3 | 1 | 1 | 2 | 3 | 2 |

**Hard gates (before scoring):**
1. If the app's own UI is dark-themed and the archetype puts it on a light field (or the reverse), that is allowed only if contrast passes. Otherwise move to the archetype that matches the UI.
2. ARC-2 requires an existing mascot or character in the brand. Never invent one for the store.
3. Any archetype's proof elements (laurels, ratings, "#1") are **removed** unless the owner supplies a source.
4. Brand colours **override** archetype palettes. The archetype supplies the structure only.

**Blending:** allowed when the two archetypes share a field strategy. Common combinations: ARC-1 structure + ARC-6 proof tile; ARC-5 + ARC-1 callouts. Never blend ARC-4 with ARC-2.

## C. Layout library (normalised to a 1320×2868 tile)

Coordinates are X/Y/W/H in % of the tile. `safe` = 6% inset on every side for text.

| ID | Name | Text | Device | Floating | Use for |
|---|---|---|---|---|---|
| L1 | **Headline-led hero** | X10 Y7 W80 H28 (3 lines max) + sub Y36 | Optional half-device teaser bleeding off the right or bottom | Proof chip Y45; 1–2 cards bleeding off an edge | Tile 1 |
| L2 | **Device-bottom** (classic) | X8 Y6 W84 H20 | Front, X8 Y30 W84, bleeds off the bottom (visible screen ≈ 70% of device) | 0–2 callouts | Default feature tile |
| L3 | **Device-top inverted** | X8 Y74 W84 H18 | Front, enters from the top, X8 Y-8 W84 H72 | Card crossing the device edge around Y55 | Every 2nd–3rd tile for rhythm |
| L4 | **Magnified callout** | as L2 | Front, bottom bleed, 80–86% wide | 1–2 **real UI components at 1.10–1.25×**, wider than the device (X3–97), 0–3° rotation, soft shadow | Feature detail |
| L5 | **Hero object** | Top or bottom | Small device or none | One 3D object / illustration at 50–70% of the tile | Brand moment, reward |
| L6 | **Panorama pair** | Tile 1 text-led, tile 2 caption on top | Device 140–170% of tile width, rotated −6° to −12°, centred on the seam | Cards bleed across the seam | Tiles 1→2 only |
| L7 | **Hand-held lifestyle** | Top | Hand (no face) + device rotated −8° to −14° | 2–3 floating 3D objects | Closing tile |
| L8 | **Bento** | Top, centred | none, or a small device in one cell | 2–4 rounded cells, gap 2% | Inputs, options, templates |
| L9 | **Before / After** | Top | none, or small | Two cards with semantic tags + connector (only with opt-in; otherwise vertical stacking) | Outcome proof |
| L10 | **Multi-device** | Top | 2 devices, front + back, offset 18%, back device at 85% scale | — | Cross-device, comparison, phone + watch |
| L11 | **Dark glow** | Top or bottom (zig-zag) | Front, alternating crop | Outlined neon cards, glow blobs | ARC-4 |
| L12 | **Numbered step** | "1. VERB" centred, step word in colour | Front, bottom bleed | — | Tutorial sequences |

**Rhythm rule** (from D and A): across a set, alternate at least two layout families so swipes do not feel repetitive. For example: L1 → L2 → L4 → L3 → L4 → L7.
