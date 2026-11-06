# Project file (`project.json`)

One file per app. Paths in it are relative to the file. Create one with `python -m appshots init <dir>` and check it with `python -m appshots check <file>`.

```json
{
  "app": {"name": "Your App"},
  "platforms": {
    "iphone":  {"device": "iphone",  "canvas": [1320, 2868], "raw_dir": "raw/iphone"},
    "android": {"device": "android", "canvas": [1080, 1920], "raw_dir": "raw/android",
                "blur": {"screen-name": [[x0, y0, x1, y1]]}}
  },
  "messages": [ … ]
}
```

- `device`: `iphone` (Dynamic Island frame) or `android` (punch-hole frame). Both are drawn in code and carry no logos.
- `canvas`: the export size. iPhone 6.9″ is 1320×2868. For Google Play, keep the long side at most 2× the short side; 1080×1920 is safe.
- `raw_dir`: the folder of raw captures. Screens are named in messages without their extension.
- `blur` (optional): privacy blurs, applied in memory only, for example to hide a person in a thumbnail. Report every blur you use.

## Messages

Each message becomes one screenshot, in the listed order. A platform only gets the messages that have `ui` for it.

| Field | Meaning |
|---|---|
| `id` | Short name |
| `kind` | `hero`, `detail`, `catalogue`, `feature`, `list` or `output`. This picks the layout inside each style. |
| `headline` | 2-6 word benefit. Must be true. |
| `key` | The word or phrase that gets the accent colour (or sticker or pill) |
| `sub` | One supporting line |
| `qualifier` | Optional small caps line for `feature-led` (defaults to the headline's second half) |
| `badges` | Optional real labels shown as tiles on `output` layouts, e.g. `["SRT","VTT"]` |
| `copy.<style>` | Optional exact headline lines for one style (see below) |
| `ui.<platform>` | The real screen and the UI regions to show |

### UI roles (all boxes are `[x0, y0, x1, y1]` in raw-screenshot pixels)

| Role | Used for | Required by |
|---|---|---|
| `screen` | The screen inside the phone | all |
| `callout` | The component enlarged over or next to the phone | every kind except hero and catalogue |
| `anchor` | Where the callout sits on the phone (defaults to the callout box) | — |
| `card` | Hero visual (e.g. a frame of the main result) | `hero` |
| `strip` | Secondary hero row (e.g. one list item) | — |
| `frames` | 1-3 `{file, box}` regions fanned on the editorial hero | — |
| `tiles` | Boxes of catalogue items (templates, styles, presets); `tiles_file` names the screen | `catalogue` |
| `rows` | A list region for editorial bento cells | — |
| `top` | The first few rows of a long list | — |
| `lens` | The proof detail magnified by feature-led's lens | — |
| `chip` | Screen that `lens` reads from, if not the callout's | — |

Each region is `{"file": "screen-name", "box": [...], "radius": 28}`. `file` defaults to `screen`, and `radius` is the component's own corner radius in raw pixels.

**Picking boxes:** each box should hold one complete component, edge to edge, with no text cut off. Open a crop of every box before rendering.

### Copy overrides

The defaults split the headline into two balanced lines and tag `key`. To control one style exactly:

```json
"copy": {
  "dark-neon": [[["EVERY ", null], ["WORD.", "k"]], [["YOURS TO FIX.", null]]],
  "bold-blue": [{"spans": [["Fix any", null]], "scale": 0.62},
                {"spans": [["word", "stk"]], "scale": 1.25},
                {"spans": [["in one tap", null]], "scale": 0.62}],
  "feature-led": {"big": "FIX ANY WORD", "small": "IN ONE TAP"}
}
```

Span tags: `null` is plain text, `"k"` is the accent colour, `"stk"` is an outlined sticker word (bold-blue), and `"pill"` is a label pill (bold-blue).

A complete real example is [examples/example-project/project.json](../examples/example-project/project.json).
