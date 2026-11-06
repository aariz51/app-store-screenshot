# Contributing

Issues and pull requests are welcome.

- **New style:** add `appshots/styles/<name>.py` with `NAME`, `TITLE`, `REFERENCE` and `render(project, platform)`, register it in `appshots/styles/__init__.py`, and document its reference-derived rules in `docs/design-styles.md`. A style must come from a measured reference (add the analysis to `references/`). Do not reskin an existing style.
- **Do not commit** third-party screenshots, app captures you are not allowed to publish, or images with people, faces or other companies' logos.
- **Run the tests** before opening a PR: `.venv/bin/python tests/test_smoke.py`
- Keep the content rules in `.claude/commands/app-store-screenshots.md` intact.
