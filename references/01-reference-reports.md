# 01 — Individual Reference Reports (Deliverables 2, 4, 5)

Evidence tags used throughout:

| Tag | Meaning |
|---|---|
| **[OBS]** | Directly visible in the reference |
| **[MEAS]** | Derived from pixel analysis (`scripts/measure-reference.py`; the reference images themselves are not redistributed) |
| **[INF]** | Reasonable interpretation of visual evidence |
| **[UNK]** | Cannot be established from these files |
| **[REC]** | Recommendation for recreating or improving |

Confidence: **H** clearly observable · **M** strong inference · **L** unreliable.

---

## 0. Corrections to the brief before starting

1. **There are six references, not five.** [OBS·H] The sixth image is a food-ordering app ("LeanBites", orange). It is analysed as **Reference F**.
2. **None of the files are App Store exports.** [MEAS·H] They are *showcase compositions*: several screenshots laid side by side on a neutral backdrop, with rounded tiles and gutters. The real App Store asset is each tile on its own, as a rectangle (Apple rounds corners in the store UI itself). Rounded corners, gutters and backdrop are presentation only, so do not bake them into exports.
3. **Resolution is low.** [MEAS·H] A is 2000×790. B is 495×679. C to F are 680×378 (a typical social-feed preview size [INF·M]). A single tile is only 137–309 px wide. Hairline details (stroke widths, small shadows, exact type metrics) are **±2–3 px at source**, which is ±10–25 px at real export size. Every size below is an estimate.
4. **All tiles share one aspect ratio.** [MEAS·H] Measured width/height is 0.459–0.469 on every complete tile, and Apple's 6.9″/6.7″ portrait sizes are 0.460–0.461 (1320×2868, 1290×2796). That ratio cannot separate 6.9″ from 6.5″ (1284×2778 = 0.462), so the target device class is **[UNK]**. Treat every reference as a **portrait iPhone 6.9″-class canvas**.
5. The brief's "Reference E = minimalist white" is only partly right. E mixes light grey bento tiles and dark product screens, and its type is a heavy condensed display face, not "clean" type. Details in §E.

### Measured panel grid (all references)

| Ref | File px | Layout | Tile px (w×h) | w/h | Gutter | Tile corner radius | Backdrop |
|---|---|---|---|---|---|---|---|
| A | 2000×790 | 1×6 strip | 307–309 × 664–666 | 0.462–0.465 | 8–10 px (≈2.9% of tile w) | 34–41 px ≈ **12% of tile w** | `#E0CFC5` warm taupe |
| B | 495×679 | 3×2 grid | 141–144 × 306–308 | 0.459–0.469 | 10–11 px (≈7%) | 9–12 px ≈ **7%** | `#EBEBEB` |
| C | 680×378 | 1×4.3 strip (cropped) | ≈144 × 321 | ≈0.45 | ≈8 px | ≈10–13% (L) | `#EBEBEB` |
| D | 680×378 | 1×4.3 strip | ≈143 × 319 | 0.451 | ≈7 px; 1 px white tile stroke | ≈5–8% (L) | `#EBEBEB` |
| E | 680×378 | 1×4.3 strip | 137–151 × 305 | 0.45–0.49 | 12–14 px | 6–9% (L) | `#EBEBEB` |
| F | 680×378 | 1×4.3 strip | ≈151 × 310 | 0.487 (L, merged edge) | ≈7 px | ≈7% (L) | `#EBEBEB` |

Use [MEAS] as H for A and B and M for C to F, because the low resolution and thin white tile strokes made automatic gutter detection unreliable there.

**Normalised coordinates.** Each box gives X/Y/W/H as a **% of its own tile** (origin top-left), which converts straight to 1320×2868. Headline boxes are [MEAS] from text-pixel bands. Every other box is an [INF·M] visual estimate, ±3%.

---

## A — Couples Expense Tracker (warm coral / cream)

### A.1 Canvas & composition
- [OBS·H] Six tiles. Colour fields alternate: **coral, coral (phone-dominant), cream, cream, coral, cream**.
- [OBS·H] **Tiles 1→2 form a panorama.** The tilted phone in tile 2 crosses the gutter into tile 1: "U… coming Bills" and "Hon…" are cut by the seam at tile 1's right edge (≈ y 55–68%). In the store, each screenshot ends at its own edge, so the half-phone in tile 1 reads as a tease that pulls the eye right.
- [OBS·H] Tile 1's streak card and House card also **bleed off the right edge** into tile 2, which reinforces the continuity.
- [INF·M] Every other tile is self-contained.
- [MEAS·H] Left text margin is **12–13% of tile width**, the same on tiles 1 and 3 (≈165 px at 1320 w).

### A.2 Per-tile structure & normalised boxes

| Tile | Headline box | Main visual | Secondary / floating | Layout family |
|---|---|---|---|---|
| 1 "Couples Expense Tracker." | X13 Y8 W57 H23 [MEAS]: three lines, pitch 8.4% of tile h | none (text-led hero) | Laurel "5.0 User Rating" X12 Y42 W44 H10; streak card X12 Y60 W70+ (bleeds); House card X27 Y71 W73+ (bleeds); app-icon-like piggy tile X9 Y87 W16 H7 | Headline-led hero + floating UI |
| 2 (no headline) | Caption at bottom: "Splitting by income of couples in multiple currencies", centred, X15 Y88 W70 H6 | Huge phone, **≈1.6× tile width**, rotated ≈ −8° to −10° [INF·M], top cropped, crosses into tile 1 | Six currency pills in a 3×2 grid, X5 Y79 W92 H8 | Device-dominant + panorama |
| 3 "Split It / Your Way" | X12 Y7 W58 H13 [MEAS]; subhead Y23–27 | Front-facing phone X8 Y32 W86, **bottom-cropped** | **Magnified UI callouts**: Netflix row and "Pay & Split" button redrawn ≈1.15× over the phone and wider than it (X3–97), with a soft shadow | Floating-UI callout |
| 4 "Shared Goals" | **Bottom**: X10 Y73 W50 H14; subhead Y88 | Phone **top-cropped** (enters from the top edge), X6 Y0 W88 H60 | Enlarged "House 44%" card wider than the phone (X3 Y13 W94 H17); "$11,180.4 Saved together" pill X8 Y62; 3D dart-and-target illustration X65 Y80 | Inverted (visual top, text bottom) |
| 5 "Expense History" | X11 Y7 W60 H17 (white on coral) | Front phone, bottom-cropped, X7 Y33 W83 | Two transaction cards magnified and offset right (X30–97), slightly rotated (≈ −2°) [INF·L] | Floating-UI callout |
| 6 "Spending Insights" | X11 Y7 W62 H17 | **Hand-held phone** (photo composite) rotated ≈ −12° | Three 3D object icons in white rounded squares (car, cart, house), each tilted ±10–15°, X0–100 Y12–55 | Lifestyle / hand-held |

### A.3 Typography
- [OBS·H] Headlines use a **heavy sans** in **sentence/title case** with very tight leading (pitch ≈ 1.0–1.05× cap+descender) and **negative tracking**. Tile 1 ends with a full stop.
- [OBS·H] **Two-tone headlines.** Tile 3: "Split It" orange, "Your Way" black. Tile 6: "Spending" orange, "Insights" black. Tile 4: "Shared" black, "Goals" orange. The rule is **one word or line in brand colour, the rest neutral**.
- [OBS·H] Subheads are a regular weight of the same family, about **0.28× headline cap height**, two lines, left-aligned to the headline edge.
- [INF·M] The face is a slightly narrow heavy grotesk with fairly geometric bowls. Candidates **(hypotheses, not identified)**: *Archivo SemiCondensed ExtraBold*, *Inter Tight ExtraBold*, *SF Pro Display Heavy at −3% tracking*. [UNK] actual family.
- [MEAS·M] Size: the tile 1 line pitch is 8.4% of tile height, which gives **≈240 px pitch / ≈210–230 px font size at 1320×2868** for 7–8-character lines.

### A.4 Colour [MEAS unless noted]

| Role | HEX | RGB | Confidence |
|---|---|---|---|
| Coral background, top | `#FDA273` | 253,162,115 | H |
| Coral background, bottom | `#FE8D6C` | 254,141,108 | H |
| Gradient | vertical, lighter at top, about 6% luminance drop | — | H |
| Brand headline orange | `#EB8442` | 235,132,66 | M (anti-aliasing) |
| Cream background | `#F8F7F3` / `#F9F8F3` | 248,247,243 | H |
| Card white | `#FEFEFB`–`#FFFFFF` | — | H |
| Headline neutral | near-black (dark brown-black, about `#1E1A18`) | — | L (too few pure pixels) |
| Deep coral (tile 2 shadow) | `#C76E62` / `#DB7760` | — | M |
| Showcase backdrop | `#E0CFC5` | 224,207,197 | H (presentation only) |

- [INF·M] The palette is warm throughout: coral and cream, with no cool colour except a little UI green ("Settled") and red. This fits a relationship and money app: warm and safe, nothing like a cold bank.

### A.5 Device
- [OBS·H] Device is a modern iPhone-style frame with a **Dynamic Island**, a thin black bezel and a titanium-grey outer rim on tile 2. [UNK] exact model.
- [OBS·H] Scale varies on purpose: the tile 2 phone is about **160% of tile width**, while tiles 3 and 5 are about 83–86%.
- [OBS·H] Cropping: tiles 3 and 5 bleed off the bottom, tile 4 off the top, tile 2 off the top and left.
- [INF·M] Production: tiles 3–5 use a flat front mockup with a screenshot inside. Tile 2 is either a perspective/3D render or a rotated flat mockup with a soft drop shadow (no visible perspective foreshortening, so **2D rotation is the likely method**, M). Tile 6 is a stock or photographed hand with the screen replaced.
- [OBS·M] Shadows are large, soft and warm-tinted, never grey-black.

### A.6 Floating elements

| Element | Functional or decorative | Depth | Shadow |
|---|---|---|---|
| Streak card, House card, goal cards, transaction cards, Pay & Split | **Functional**: real app components, enlarged | Above the device | Soft, about 8% opacity, 20–40 px blur at export, offset downward |
| Currency pills | Functional (supported currencies) | Flat on the background | Very light |
| Laurel "5.0 User Rating · App Store" | **A claim**: social proof | Flat | None |
| Piggy-bank tile (tile 1) | Brand mark or app icon [INF·M] | Flat | Soft |
| Car, cart, house 3D icons, dart target | **Decorative** category illustrations | Behind the hand, in front of the background | Soft |

### A.7 Hierarchy (reading order)
Tile 1: headline → laurel → cards → half-phone teaser. Tiles 3–6: coloured word → black word → subhead → magnified card → device.
[INF·M] The magnified card is the real focal point, because it has the largest UI type and the strongest shadow. The phone mostly says "this is real software".

### A.8 Story sequence
1. Category + positioning ("Couples Expense Tracker.") + proof (rating) + a hint of the UI.
2. Core differentiator: income-based splitting and multiple currencies.
3. Primary action: split a bill.
4. Shared savings goals (the emotional, aspirational feature).
5. History and accountability.
6. Insights and analytics.

[INF·M] The sequence runs from **identity → mechanism → action → aspiration → control → mastery**. It works because tile 2 answers "how is this different from Splitwise?" before any feature tour.
[REC] Tile 2 has no headline and relies on a small caption, so a search-result view (first 3 tiles) loses that differentiator. Move the caption to the top as a headline.

### A.9 Psychology
- Large type on tile 1: the category ("Couples Expense Tracker") **is** the keyword. Matching the search query immediately confirms relevance.
- Warm coral: lowers money anxiety and signals partnership, not accounting.
- Magnified real cards over the phone: proves the feature with real UI while keeping text legible at thumbnail size.
- Hand-held final tile: a human-scale "this fits your life" close.

### A.10 Tech spec summary
Canvas 1320×2868 portrait · two fields, coral gradient `#FDA273→#FE8D6C` and cream `#F8F7F3` · margins 12–13% L/R, headline top ≈7–8% · heavy grotesk, two-tone, left-aligned, about 7.5% of canvas height per line · phone 83–86% of width front-on, or 160% rotated hero · magnified callout cards at about 1.1–1.2× · warm soft shadows.

---

## B — Habit & Screen-Time (playful blue / mascot)

### B.1 Canvas
- [MEAS·H] A 3×2 grid of separate tiles. No panorama evidence.
- [OBS·H] Colour fields: **blue (1), blue (2), white (3), blue (4), white (5), blue top (6)**. Blue is dominant, and the white tiles give the eye a rest.

### B.2 Per-tile structure

| Tile | Headline | Main visual | Floating / decorative |
|---|---|---|---|
| 1 "Turn Your Life into a Game" | Centred, X8 Y6 W84 H40. Mixed sizes: "Turn" about 2× the size of "Your Life into a"; "Game" in a black sticker treatment with white outline | **Mascot** (white cat-like character with hourglass), X0 Y45 W75 H50 | Gold coin left edge (cropped), smiley emoji inline, white cloud band at the bottom |
| 2 "Block Distracting Apps" | Centred, X10 Y17 W80 H22; 👀 emoji inline | Phone, bottom-cropped, front | Floating padlock top-centre (breaks the tile top), big lock button bottom |
| 3 "Build Habits & Earn Coins" | Centred black on white; coins replace the letter "o" | Phone showing camera scanning a book, front, bottom-cropped | — |
| 4 "Coins Unlock Screen Time" | Centred, white, with "Coins" in a label pill | Treasure chest illustration inside the phone/card | Coin-price chips (10/15/20 min), black CTA pill "Buy Screentime" |
| 5 "Turn Reps into Screen Time" | **Bottom** headline, "Turn" in a blue pill | Phone showing a camera feed of a **real person doing push-ups** with a rep counter | 3D dumbbell and water drop floating at the phone edges |
| 6 "Track screen Time & Habits" | Top, white | Stats phone | Streak badges ("64 Best Streak", "STREAK!" mascot) overlapping the bottom; lightning bolt |

### B.3 Typography
- [OBS·H] Very heavy **rounded** display face. Some words have a white fill with a **dark outline and hard drop shadow** (sticker style). Title case.
- [OBS·H] **Word-level scale contrast**: the key verb or noun is set at about 1.6–2.2× the size of the connector words.
- [OBS·H] Glyph substitution: emoji or objects replace letters or sit inline (😊, 👀, coin-"o", lock).
- [INF·M] Candidates (hypotheses): *Lilita One*, *Baloo 2 ExtraBold*, *Fredoka Bold*, *Nunito Black*. [UNK] actual family.

### B.4 Colour

| Role | HEX | Confidence |
|---|---|---|
| Primary blue | `#2682FD` (range `#2383FD`–`#2882FC`) | H [MEAS] |
| Light blue (top glow / secondary) | `#429EF0`, `#6DAAF0` | M |
| Navy (outlines, mascot shading) | `#1C3A63` / `#2D4B7A` | M |
| Coin gold | `#F7CD1A`, with `#CBA772` shading | M |
| Tile white | `#FFFFFF` / `#FCFDFC` | H |
| Cloud tint | `#E5EAF5` | M |

[INF·M] Saturated mid-blue paired with gold coins is a classic reward palette: trustworthy blue plus "loot" gold.

### B.5 Device & depth
- [OBS·H] Front-facing phones, bottom-cropped, about 80–90% of tile width, no tilt.
- [OBS·H] Rendering is **3D cartoon** (mascot, coins, chest, padlock) with glossy highlights. [INF·M] The objects are either 3D renders (Blender/Spline) or high-quality 3D-style illustrations.
- [OBS·M] Objects **break the tile edge** (padlock top, coin left), which makes them feel like they come off the canvas.

### B.6 Story
1. Brand promise and character (gamification).
2. Mechanism 1: block apps.
3. Mechanism 2: earn coins through habits.
4. Mechanism 3: spend coins to unlock time (the economy loop).
5. Mechanism 4: physical reps (the most surprising feature).
6. Proof of progress: stats and streaks.

[INF·M] The story explains the **economy loop** step by step: earn → spend → measure. That suits a product whose value is its mechanic.

### B.7 Psychology
The mascot gives the app a face for brand recall (Duolingo-style recall [INF]), and a cute character lowers the "nagging app" feeling of screen-time control. Short verbs ("Turn", "Block", "Build", "Earn", "Unlock") frame the app as an action game, not a restriction.

### B.8 Notes against the content rules
- ⚠︎ Tile 5 shows a **real human face and body** in a camera feed. Under the content rules (no human faces in generated assets), use a silhouette, a mascot, or a camera feed showing only hands or feet.
- ⚠︎ Stickers and emoji conflict with the "no sticker packs" layout contract unless the app's brand really is playful (see the decision engine).

---

## C — Chat Export (bold blue / condensed caps)

### C.1 Canvas
- [OBS·H] Strip of about 4.3 tiles (the fifth is cropped by the preview). Every tile is blue, with no alternation.
- [OBS·M] Each tile has a **white ellipse vignette or lighter centre** behind the device.

### C.2 Per-tile

| Tile | Headline | Main visual | Floating |
|---|---|---|---|
| 1 "#1 Message Exporter on [Apple logo] iPhone" | Centred, top, about X10 Y6 W80 H22, with laurels around "#1" | Phone front, with a pink-red **highlight band** sweeping across the chat (selection/export metaphor) | Real hand holding printed pages (bottom right); lightning "FAST & PRINT-READY" label bottom left |
| 2 "Export to PDF / Excel or Text" | **Bottom** | Enlarged "Export chat" sheet card (PDF/Print/Spreadsheet/Text) over a phone | 3D file icons CSV / PDF / TXT, fanned |
| 3 "From any chat app / in minutes" | Top | 3D app icons in an arc → arrows → document stack | ★★★★★ "SAVED ME HOURS" testimonial chip at the bottom |
| 4 "Get clean documents with every detail" | Top | Document card; magnifier circle on "Aug 24, 2026" | Red starburst sticker "TIME-STAMPED FILES"; "Print Files" CTA |

### C.3 Typography
- [OBS·H] **ALL CAPS, heavy condensed grotesk**, white, centred. Secondary lines ("EXCEL OR TEXT", "IN MINUTES", "WITH EVERY DETAIL") about 40–50% of headline size and lighter in colour.
- [OBS·H] Headline pattern: **[big benefit verb + object] / [small qualifier]**.
- [INF·M] Candidates: *Anton*, *Oswald Bold*, *Barlow Condensed ExtraBold*, *Archivo ExtraCondensed Black*.

### C.4 Colour
| Role | HEX | Confidence |
|---|---|---|
| Brand blue | `#1B76F5` (range `#1F76F5`–`#257BFC`) | H [MEAS] |
| Light glow | `#7BA8E4` | M |
| Text | `#FFFFFF` | H |
| File colours | PDF red, CSV green `#4ECCA0`-ish, TXT blue | M |

### C.5 Psychology & risks
- "#1" and ★★★★★ "SAVED ME HOURS" are **claims**. [REC] Use them only with evidence (a category ranking you can cite, a real review quoted with permission). Apple Guideline 2.3.7 bars misleading metadata [INF·M, check the current guideline text].
- ⚠︎ Third-party logos (WhatsApp, Instagram, Messages, Telegram) are **trademarks**. Showing them implies compatibility and can be rejected or challenged. [REC] Show them only if the integration really exists, and follow each brand's usage guidelines.
- [INF·M] Story: **authority → formats → sources → output quality**. It is a utility pitch that answers "what goes in, what comes out, how good is it".

---

## D — Dating, anonymous (dark / neon)

### D.1 Canvas
- [OBS·H] Strip; near-black tiles with a purple tint.
- [OBS·H] **Tiles 1 and 3 are identical** ("VIBES OVER LOOKS."). This is either a presentation error or a deliberate repeat. [REC] Never repeat a tile in a real set; it wastes one of the first three slots.
- [OBS·H] **Zig-zag rhythm**: tile 1 has the device top and text bottom, tile 2 has text top and device bottom, and so on. Across a swipe, the eye moves top → bottom → top.

### D.2 Per-tile

| Tile | Headline (box) | Visual |
|---|---|---|
| 1/3 "VIBES OVER LOOKS." | Bottom, X6 Y78 W88 H13; "VIBES" pink, "OVER LOOKS." white | Phone top-cropped "Vibe check" grid of masked blobs; floating "IT'S A MATCH 94% vibe match" card with neon outline |
| 2 "TALK FIRST. REVEAL LATER." | Top, X6 Y6 W90 H26 [MEAS]: 3 lines, pitch about 8.7% of tile h | Chat bubble "you up? can't sleep" + "Reveal request" card with Not yet / Reveal buttons |
| 4 "GONE BY SUNRISE." | Top, "SUNRISE." lime | Neon crescent moon, "NEXT WIPE IN 05:59:12" chip, Disappearing-chats toggle card, "Screenshot blocked" pill |

### D.3 Type
- [OBS·H] **ALL CAPS heavy condensed** with very tight leading and a **full stop after each statement**: manifesto voice.
- [OBS·H] Two-tone: one key word in neon lime or pink.
- [INF·M] Candidates: *Anton*, *Big Shoulders Display Black*, *Archivo Black* (condensed width), *Druk*-like.
- Support line: small regular sans in grey (≈`#9A9A9A`, L).

### D.4 Colour [MEAS]
| Role | HEX | Conf. |
|---|---|---|
| Background | `#110F15` (range `#08080C`–`#1A1B1B`) | H |
| Purple-tinted dark | `#200E25` | M |
| Neon lime | `#C8FC49` (range `#C3ED55`–`#C9FB48`) | H |
| Hot pink | `#EE3497` | H |
| Purple glow | `#4B2844` / `#59374B` | M |

### D.5 Depth
- [OBS·H] **Glow, not shadow**: neon outer glows (lime/pink), coloured blurred blobs behind masked avatars, and outlined cards (1–2 px neon stroke).
- [INF·M] On dark backgrounds, depth comes from emitted light, not cast shadows. Drop shadows are invisible on black.

### D.6 Story & psychology
Value → mechanism → privacy promise: *what you get (chemistry), how it works (talk then reveal), why it's safe (disappearing)*. Anonymity is carried visually by **masks instead of faces**, which also satisfies a no-faces rule and is a technique worth reusing. Dark + neon reads as **night, intimacy, exclusivity**.

---

## E — Playlist Cover Maker (editorial bento / light)

### E.1 Canvas
- [OBS·H] Light grey tiles (`#F4F6F7`); tile 1 has a lavender tint (`#F1ECF4`).
- [OBS·H] **Bento within a tile**: tile 1 is split into a hero card (stacked cover art) over a separate award card. Tile 2 is a 3-cell bento (Photos / Web images / 100+ designs collage).
- [OBS·H] Tiles 3–4 are **numbered steps** ("1. FIND WHAT YOU LIKE", "2. PICK YOUR PLAYLIST") with a front-facing phone, bottom-cropped, about 85% of tile width.

### E.2 Type
- [OBS·H] Heavy condensed caps, black, **centred**, 2–3 lines. One word set in colour: blue `#2198E3` ("YOU LIKE"), magenta `#B73968` ("PLAYLIST"). [MEAS·M]
- [MEAS·L] Cap height about 3.9% of tile height (≈110 px at 2868), line pitch about 6.2%. The type is smaller than A, B and D because the bento content carries the message.

### E.3 Colour & content
- The background stays neutral so the **user content (colourful cover art) is the colour**. [INF·M] This is deliberate: in a creative tool, the output is the hero.
- Award badge "APPLE DESIGN AWARD Finalist – Delight and Fun". [OBS·H] **This is a claim.** Use it only if it is true. ⚠︎ Tile 1 cover art includes photos with **human faces** (content rules: replace them with non-face imagery).

### E.4 Story
Promise → inputs (photos / web / templates) → step 1 → step 2 → (cropped) step 3. [INF·M] This **tutorial sequence** works for tools whose value only shows once you understand the workflow.

---

## F — LeanBites, healthy eating out (orange / white)

### F.1 Canvas
- [OBS·H] Tile 1 is orange and the rest are white or cream. [MEAS] Orange is `#FD8206` with darker `#F86B07`/`#FB4B11` at the edges. [INF·M] **Radial or edge vignette**: brighter centre, deeper edges.

### F.2 Per-tile

| Tile | Headline | Visual |
|---|---|---|
| 1 "Eat Out Smarter" | White, centred, top, X20 Y9 W60 H10 | ★★★★★ laurel "Top Health Apps"; **Before/After cards** (1320 cal → 1050 cal, red ✕ / green ✓ tags) with a curved arrow; app logo + name lockup at the bottom |
| 2 "Smarter choices / wherever you eat" | Two-tier: small lead-in + big line, "eat" with an orange brush underline | Phone "Meals" list; speech-bubble chip "Craving for breakfast?" (orange) breaks the phone edge |
| 3 "Outsmart the menu / High protein / Low calorie orders" | Bottom | Nutrition card "Cool Wrap" with score 100, macro chips |
| 4 "Thousands of / Menu items analyzed" | Top | Burger photo with "Healthy to eat for you" chip; macro tiles |

### F.3 Type
- [OBS·H] Rounded-geometric bold, sentence case, centred. Lead-in at about 45% of the main line.
- [INF·M] Candidates: *Nunito ExtraBold*, *Poppins Bold*, *Plus Jakarta Sans ExtraBold*.
- [OBS·H] **Hand-drawn accent** (brush underline) on one word.

### F.4 Psychology
- Before/After with real numbers is **the strongest "proof" device in the whole set**: a quantified outcome in tile 1. [REC] The numbers must come from the real product's data for real menu items.
- "Top Health Apps" laurel and "Thousands of menu items analyzed" are claims. Verify them.
- Food photography provides appetite appeal, and the orange is appetite-stimulating [INF·L; colour-appetite links are popular lore with weak evidence].

---

## Cross-reference: measured accent colours

| Ref | Accent | HEX [MEAS] |
|---|---|---|
| A | brand orange (headline) | `#EB8442` |
| A | coral background | `#FDA273 → #FE8D6C` |
| B | primary blue | `#2682FD` |
| B | coin gold | `#F7CD1A` |
| C | primary blue | `#1B76F5` |
| D | neon lime | `#C8FC49` |
| D | hot pink | `#EE3497` |
| D | background | `#110F15` |
| E | step blue | `#2198E3` |
| E | step magenta | `#B73968` |
| F | orange | `#FD8206` (edge `#F86B07`) |

## What stays unknown [UNK]
Exact font families · original export resolution and device class (6.9″ vs 6.5″) · whether device frames are 3D renders or 2D mockups (except where perspective is visible) · tool used (Figma, Photoshop, etc.) · real colours of thin text (anti-aliasing at low resolution) · the hidden fifth or sixth tiles of C–F · whether ratings, awards and "#1" claims are true · the original designers' intent.
