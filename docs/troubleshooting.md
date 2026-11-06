# Troubleshooting

| Problem | Fix |
|---|---|
| `/app-store-screenshots` not listed | Check that `~/.claude/commands/app-store-screenshots.md` (or the project's `.claude/commands/`) exists, then restart Claude Code. |
| `ModuleNotFoundError: PIL` | Use the engine's venv: `~/app-store-screenshot/.venv/bin/python -m appshots …`, or rerun `./install.sh`. |
| `config error: screenshot not found` | `raw_dir` is relative to `project.json`. Screen names have no extension. |
| `kind 'catalogue' needs ui.tiles` | Give catalogue messages a list of tile boxes, or change the kind. |
| Text cut off inside a callout | The box cuts through a component. Widen it to the whole card and check a crop. |
| Headline too small | The size auto-fits the widest line. Shorten the headline or set a `copy.<style>` override with better line breaks. |
| Callout covers the phone's key area | Set `anchor` to where the component sits on the screen, or pick a smaller box. |
| `matches no store size` | Set `canvas` to a store size. For Play, keep the long side at most 2× the short side. |
| `xcrun simctl` hangs | Shut the device down and boot it again (`xcrun simctl shutdown <UDID>; xcrun simctl boot <UDID>`). |
| Emulator: "Cannot find AVD system path" | The AVD's system image is not installed. Install it with `sdkmanager` (large download; ask first). |
| Appium sees only `NATIVE_APP` on a WebView app | WebView inspection may be off on new simulator runtimes. Drive the app with real taps by coordinate or accessibility label. |
| Gradient banding | Grain is added by default. Export PNG, not JPEG. |
