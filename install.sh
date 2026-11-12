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

# Codex: a skill (shared ~/.agents/skills, linked into ~/.codex/skills) and a custom prompt.
SK="$HOME/.agents/skills/app-store-screenshots"
mkdir -p "$SK"
{ echo "---"; echo "name: app-store-screenshots";
  sed -n 's/^description: /description: /p' "$HERE/.claude/commands/app-store-screenshots.md";
  echo "---"; awk 'BEGIN{n=0} /^---$/{n++; next} n>=2' "$HERE/.claude/commands/app-store-screenshots.md"; } > "$SK/SKILL.md"
if [ -d "$HOME/.codex" ]; then
  mkdir -p "$HOME/.codex/skills" "$HOME/.codex/prompts"
  [ -e "$HOME/.codex/skills/app-store-screenshots" ] || ln -s "$SK" "$HOME/.codex/skills/app-store-screenshots"
  cp "$HERE/.claude/commands/app-store-screenshots.md" "$HOME/.codex/prompts/app-store-screenshots.md"
  echo "Codex: skill app-store-screenshots and prompt /prompts:app-store-screenshots installed."
fi
if [ "$HERE" != "$HOME/app-store-screenshot" ]; then
  echo "Engine is not at ~/app-store-screenshot. Add to your shell profile:  export APPSHOTS_HOME=\"$HERE\""
fi
echo "Installed. In any app repo, run /app-store-screenshots in Claude Code."
