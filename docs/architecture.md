# Architecture

```
slash command (.claude/commands/app-store-screenshots.md)
  │  discovery → (ask) capture → storyboard → (ask) styles → render → visual QA → report
  ▼
appshots CLI (appshots/cli.py)
  ├─ discover.py   scan a repo for portrait captures, classify by size
  ├─ project.py    load and validate project.json, read raw screens (read-only, in-memory blur)
  ├─ styles/       one independent module per design language
  │    warm_premium · bold_blue · feature_led · dark_neon · minimal_editorial
  ├─ engine.py     shared primitives: device frames, rounded masks, tinted shadows, glow,
  │                gradients, grain, real-UI cards, auto-fitting multi-span headlines, contact sheets
  └─ validate.py   store-size, RGB and alpha checks
```

**Design rules encoded in the code:**
- Styles never share layout code: they share only primitives. Adding a style means adding a module with `NAME`, `TITLE`, `REFERENCE` and `render(project, platform) -> [PIL.Image]`, then registering it in `styles/__init__.py`.
- Layouts are picked by message `kind`, so any app maps onto them through its own story.
- All coordinates are proportional to the canvas (a 1320×2868 design grid), so any store size works. Android phones are drawn at 0.8× width to fit taller screens.
- Raw files are opened read-only. Exports go only to the output folder.

**Design knowledge:** `references/` holds the measured analysis that the styles implement. `design-system/design-tokens.json` holds generic tokens for building new styles. `templates/qa-checklist.md` is the full manual QA.
