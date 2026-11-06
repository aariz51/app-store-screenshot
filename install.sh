#!/usr/bin/env bash
# Install the engine's Python environment and the /app-store-screenshots command for all projects.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 -m venv "$HERE/.venv"
"$HERE/.venv/bin/pip" install -q -r "$HERE/requirements.txt"
"$HERE/.venv/bin/python" "$HERE/tests/test_smoke.py"
mkdir -p "$HOME/.claude/commands"
DST="$HOME/.claude/commands/app-store-screenshots.md"
if [ -e "$DST" ] && ! cmp -s "$HERE/.claude/commands/app-store-screenshots.md" "$DST"; then
  cp "$DST" "$DST.bak"
  echo "Existing command backed up to $DST.bak"
fi
cp "$HERE/.claude/commands/app-store-screenshots.md" "$DST"
if [ "$HERE" != "$HOME/app-store-screenshot" ]; then
  echo "Engine is not at ~/app-store-screenshot. Add to your shell profile:  export APPSHOTS_HOME=\"$HERE\""
fi
echo "Installed. In any app repo, run /app-store-screenshots in Claude Code."
