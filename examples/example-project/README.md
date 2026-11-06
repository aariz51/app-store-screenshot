# Example project

`project.json` is the exact config that produced the gallery in `../preview/`. It covers six messages on iPhone and five on Android, with per-style copy overrides.

The raw captures are not distributed. To run it, put your own captures in `raw/iphone/` and `raw/android/` with the screen names used in the file, adjust the boxes, then:

```bash
.venv/bin/python -m appshots render examples/example-project/project.json --styles all
```
