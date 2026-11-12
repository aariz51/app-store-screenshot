# Changelog

## 0.2.0 — 2026-11-12
- Command renders all five styles with no style question, and captures fresh simulator screens itself when the repo's captures are missing or stale.
- Command states it replaces older poster/image-generation screenshot workflows.
- `install.sh` also installs a Codex skill (`~/.agents/skills/app-store-screenshots`, linked into `~/.codex/skills`) and a Codex prompt.
- Closer reference fidelity: headlines wrap at a fixed, reference-measured size instead of shrinking; Archivo (heavy, narrow) for warm-premium; wide heavy caps for feature-led; inline step numbers for minimal-editorial; punctuation stays with its word.
- Fixes: bottom callouts never clip; editorial detail tiles without a second cell show the real screen below.

## 0.1.0 — 2026-11-07
- First public release.
- Five reference-derived styles: warm-premium, bold-blue, feature-led, dark-neon, minimal-editorial.
- `appshots` CLI: discover, init, check, render, validate, styles.
- `/app-store-screenshots` Claude Code command with approval gates and content rules.
- Reference analysis, design tokens, workflow, blueprint and QA checklist.
