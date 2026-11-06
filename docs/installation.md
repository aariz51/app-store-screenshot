# Installation

```bash
git clone https://github.com/aariz51/app-store-screenshot ~/app-store-screenshot
cd ~/app-store-screenshot && ./install.sh
```

`install.sh`:
1. creates `.venv` and installs Pillow and numpy;
2. runs `tests/test_smoke.py`;
3. copies `.claude/commands/app-store-screenshots.md` to `~/.claude/commands/` (and backs up any existing file with the same name).

**Command in one project only:** instead of the global install, copy the command file into `<your-repo>/.claude/commands/`.

**Engine in another folder:** `export APPSHOTS_HOME=/path/to/app-store-screenshot`. The command looks for `$APPSHOTS_HOME` first, then `~/app-store-screenshot`.

**Update:** run `git pull`, then `./install.sh` again.

**Uninstall:** delete `~/.claude/commands/app-store-screenshots.md` and the clone.
