# Usage

## With the slash command (recommended)

Run `/app-store-screenshots` in Claude Code from the root of an app repository. Optional arguments: a style name or `all`, then `iphone`, `android` or `both`.

**Example 1: the repo already has screenshots.** The agent runs `discover`, opens the candidates, and says which it will use. It builds `store-assets/project.json`, shows the storyboard and asks which styles you want, then renders.

**Example 2: there are no screenshots.** The agent tells you which simulator, build, screens and output folder it plans to use, and waits for your yes. Then it captures real screens with a clean status bar. See [simulator-capture.md](simulator-capture.md).

**Example 3: one style.** Run `/app-store-screenshots dark-neon iphone`. You get six (or however many messages you have) iPhone screenshots plus a contact sheet.

**Example 4: all styles.** Run `/app-store-screenshots all both`. You get every style on both platforms, plus `master-comparison.png` per platform.

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
