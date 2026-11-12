# Usage

## With the slash command (recommended)

Run `/app-store-screenshots` in Claude Code from the root of an app repository. Optional arguments: a style name or `all`, then `iphone`, `android` or `both`.

**Example 1: the repo already has screenshots.** The agent runs `discover`, opens the candidates, and says which it will use. It builds `store-assets/project.json`, writes the storyboard, and renders all five styles.

**Example 2: there are no screenshots, or they are stale.** The agent builds the app, boots a simulator and captures real screens with a clean status bar, then continues. See [simulator-capture.md](simulator-capture.md).

**Example 3: one platform.** Run `/app-store-screenshots iphone`. You get all five styles for iPhone plus `master-comparison.png`.

To render a single style by hand, use the engine: `--styles dark-neon`.

## With the engine alone

```bash
E=~/app-store-screenshot; PY=$E/.venv/bin/python; cd $E
$PY -m appshots discover ~/code/my-app
$PY -m appshots init ~/code/my-app/store-assets
# put raw captures in store-assets/raw/iphone and raw/android, then edit project.json
$PY -m appshots check ~/code/my-app/store-assets/project.json
$PY -m appshots render ~/code/my-app/store-assets/project.json --styles warm-premium,dark-neon --platforms iphone
$PY -m appshots validate ~/code/my-app/store-assets/final
```

The default output is `final/` next to `project.json`. Use `--out` to choose another folder.
