# Design styles

Each style is its own module in `appshots/styles/`, with its own layouts per message kind. The measurements behind them are in [references/01-reference-reports.md](../references/01-reference-reports.md). The reference images are not redistributed.

| Style | Reference | Field | Type | Layout logic by kind | Depth |
|---|---|---|---|---|---|
| `warm-premium` | A | Coral gradient `#FDA273→#FE8D6C` alternating with cream `#F9F8F4` | Archivo 800 (narrow), ~230 px at 2868 h, sentence case, left-aligned, up to 3 short lines, one orange `#EB8442` key word | hero+detail: one panorama across tiles 1-2 with a giant phone tilted −9°. catalogue/list: copy at top, phone bottom-cropped, enlarged cards wider than the phone. feature: phone enters from the top, copy at the bottom. output: phone tilted +10° with real format tiles. | Warm-tinted soft shadows |
| `bold-blue` | B | `#3A95FF→#1F74F0`, with white tiles at positions 3 and 5 | Baloo 2 800, centred, word-level size jumps, key word as outlined sticker or pill | Copy at top, phone below, oversized real UI breaking the phone edge. Gold sparkles. Cloud band on hero and feature tiles. | Navy shadows |
| `feature-led` | C | Single blue `#2A82FA→#145FD6`, light ellipse behind the phone | Archivo 900 wide caps, up to 3 lines, plus a lighter-blue qualifier, centred | hero: translucent highlight band and live-content strip. detail: copy at the bottom. catalogue: three real tiles fanned. feature: magnifier lens on the proof detail. output: fanned format tiles. | Deep-blue shadows |
| `dark-neon` | D | `#16131C→#09080C`, purple and accent glow blobs | Anton caps manifesto lines ending in full stops, lime `#C8FC49` / pink `#EE3497` alternating | Zig-zag: even tiles have the phone on top and copy below, odd tiles the reverse. Real UI card with a neon outline. | Emitted glow, no drop shadows |
| `minimal-editorial` | E | `#F4F5F7`, lavender hero | Barlow Condensed caps, centred, step tiles numbered inline ("1. …"), blue/magenta key word | hero: bento card of fanned real frames. detail: bento cells with the editor and rows. catalogue: grid of real tiles. Others: clean, centred, bottom-cropped phone. | Faint neutral shadows |

**What carries over from each reference** is its design method: layout, type, colour, depth and story rhythm. Its subject matter (characters, people, dating imagery, third-party logos) is never reused.

**Choosing a style:** see the decision engine in [references/03-archetypes-decision-engine-layouts.md](../references/03-archetypes-decision-engine-layouts.md). Match the app's own UI theme and category, not the prettiest option. Rendering several styles and comparing `master-comparison.png` is cheap.
