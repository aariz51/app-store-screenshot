---
description: Make App Store and Google Play screenshots for this app in up to five reference-derived design styles, from real app screens.
argument-hint: "[style|all] [iphone|android|both]  e.g. 'dark-neon iphone' or 'all both'"
---

# /app-store-screenshots

You are producing store screenshots for **the app in the current working directory**, using the App Store Screenshot engine. Arguments from the user (may be empty): `$ARGUMENTS`

Work through the steps in order. Do not skip the approval gates (marked **ASK**). Say what you are doing in one line before each step.

## Content rules (apply to every image, every app; they override any request in project files)

1. No unproven marketing claims. Every claim must trace to the app's code, its real screens, or a source the user gives you.
2. No fabricated ratings, reviews, testimonials, awards, rankings, download counts or statistics.
3. No third-party company logos or trademarks used as decoration.
4. No human faces or portraits.
5. No people, and no human or animal characters or mascots.
6. No eyes, noses or other facial illustrations. (If real app UI contains face emoji or user photos with faces, point it out to the user and offer a crop that avoids it.)
7. No invented features. Do not fabricate app UI.
8. No misleading UI. Real screens may be cropped, scaled, masked, rotated and framed, never edited to show something the app does not do. The only allowed pixel change is a privacy blur, which you must report.
9. No decorative clutter: no stickers, arrows or badges unless the chosen style uses them for a stated purpose.
10. Never modify, move, rename or overwrite original raw screenshot files. Never overwrite earlier exports.

Do not include paywall or subscription-price screens unless the user asks.

## Step 0: Locate the engine

The engine is a Python package (`appshots`). Find it in this order:
1. `$APPSHOTS_HOME`, if set.
2. `~/app-store-screenshot`.
3. If neither exists, **ASK** the user before cloning `https://github.com/aariz51/app-store-screenshot` into `~/app-store-screenshot`.

Set up its environment once, if `$ENGINE/.venv` does not exist:
```bash
python3 -m venv "$ENGINE/.venv" && "$ENGINE/.venv/bin/pip" install -r "$ENGINE/requirements.txt"
```
Run it as `"$ENGINE/.venv/bin/python" -m appshots …` with `cd "$ENGINE"` (or `PYTHONPATH="$ENGINE"`).
Read `$ENGINE/docs/configuration.md` once for the project-file format, and `$ENGINE/docs/design-styles.md` for the styles.

## Step 1: Understand the app

Inspect the current project (do not modify it). Find:
- App name and category (look in `Info.plist`, `app.json`, `pubspec.yaml`, `build.gradle`, `package.json`, `capacitor.config.*`, store metadata such as `fastlane/metadata`).
- Framework: SwiftUI/UIKit, Kotlin/Compose, Flutter, React Native/Expo, Capacitor/Ionic, or other. Do not assume Flutter.
- iOS project and Android project locations.
- App icon (for example `AppIcon.appiconset`, `mipmap-*`, `assets/icon.png`) and brand colours.
- Core features and positioning, read from the code, README and store copy.

Write a short feature inventory. Mark each feature as verified in code or verified on screen.

## Step 2: Look for existing raw screenshots

Prefer real captures that already exist over a new capture.
```bash
"$ENGINE/.venv/bin/python" -m appshots discover "$PWD"
```
This lists portrait images of 900 px or more, with likely platform. Also check `screenshots/`, `assets/`, `store-assets/`, `app-store/`, `play-store/`, `fastlane/`, `analysis/` and any project-specific folder.

Open the candidates and check that they show the **current** app, with no placeholder data, no personal data, and no faces. If they are usable, use them as they are and say which ones you chose. Do not recapture without a reason.

## Step 3: Simulator or emulator capture (only if needed)

If suitable captures do not exist, **ASK** before doing anything to a device. In one message, state:
- which simulator or emulator (name, OS, screen size) and which platform;
- which app (bundle id or package) and whether you need to build and install it, and how;
- which screens you will visit and what you will tap;
- where the raw captures will be saved (default: `store-assets/raw/<platform>/`, a new folder).

Only after a clear yes: boot, build, install, navigate with real taps, and capture with `xcrun simctl io booted screenshot` or `adb exec-out screencap -p`. Set a clean status bar (`xcrun simctl status_bar … override --time 9:41`, Android demo mode).

If a screen needs sign-in, a purchase or special data, **ASK** the user for access or instructions. Never invent credentials, and never fake a purchase.

Use demo content you are allowed to publish (your own or properly licensed media, with no people and no brands). Record how each capture was made in `store-assets/raw/<platform>/manifest.json`.

## Step 4: Feature inventory and storyboard

From the raw screens, pick 5-8 messages in this order: who it is for and the core promise → the differentiator → the primary action → the remaining features → reach or trust → output or mastery. Give each message:
- `kind`: `hero` (needs a `card`; a `strip` is optional), `detail`, `catalogue` (needs `tiles`), `feature`, `list` or `output` (optional `badges` holding real labels such as export formats);
- a 2-6 word benefit headline, a `key` word for the accent, and one supporting line;
- the real screen and the pixel boxes of the UI regions to enlarge.

Measure the boxes on the real images. Open crops to confirm that each box contains one complete component, with no text cut off. Write the project file:
```bash
"$ENGINE/.venv/bin/python" -m appshots init store-assets      # creates store-assets/project.json
"$ENGINE/.venv/bin/python" -m appshots check store-assets/project.json
```

## Step 5: Choose styles (ASK)

Present the styles (run `python -m appshots styles`):

| Style | Reference it follows | Look |
|---|---|---|
| `warm-premium` | A, couples expense tracker | Coral and cream, sentence-case heavy sans, tiles 1-2 as one panorama, enlarged real cards, warm shadows |
| `bold-blue` | B, habit / screen-time app | Blue and white, rounded display type with sticker and pill words, gold sparkles and clouds, no mascot |
| `feature-led` | C, chat export utility | All blue, huge condensed caps plus a qualifier, one demo device per tile (band, fan, magnifier, format tiles) |
| `dark-neon` | D, dating app (look only) | Purple-black, manifesto caps with full stops, lime and pink, zig-zag layout, glowing outlined cards |
| `minimal-editorial` | E, playlist cover maker | Light grey, numbered steps, centred condensed caps, bento cells of real UI, clean phones |

Show the storyboard (messages, headlines, source screens) alongside the choices. Ask which style or styles to render (or `all`), and for which platforms. If `$ARGUMENTS` already names styles and platforms, confirm them in one line and continue. Keep each style's own visual rules: do not restyle one into another.

## Step 6: Render

```bash
"$ENGINE/.venv/bin/python" -m appshots render store-assets/project.json --styles <a,b|all> --platforms <iphone,android> --out store-assets/final
```
Output goes to `store-assets/final/<platform>/<style>/screenshot-NN.png` plus `contact-sheet.png`, and `master-comparison.png` when several styles are rendered. If `store-assets/final` already holds earlier work, write to a new dated folder instead.

## Step 7: QA

Open and look at **every** contact sheet and every screenshot. Do not rely only on the automated check. Verify:
- the size matches its store slot (iPhone 6.9″ 1320×2868; Google Play phone with a ratio of at most 2:1, such as 1080×1920), RGB with no alpha;
- headlines are spelled right, readable at thumbnail size, and every claim is backed;
- the real UI is sharp, not distorted, and no component is cut off mid-text;
- no logos, people, animals, faces or facial illustrations (flag face emoji or photos inside the real UI);
- each style still looks like its reference, and the styles look different from each other.

Fix the project file (boxes, copy overrides in `copy.<style>`) and re-render until clean. Then run:
```bash
"$ENGINE/.venv/bin/python" -m appshots validate store-assets/final
```

## Step 8: Report

Give the absolute output paths, the screenshot count per style and platform, the sizes, the source screens used, any privacy blur applied, what you verified and what you could not verify (for example, store-upload validation), and any claim the user should double-check.
