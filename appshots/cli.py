"""Command line: discover, init, check, render, validate.

  python -m appshots discover <project-dir>
  python -m appshots init <store-dir>                    # writes a project.json template
  python -m appshots check <project.json>                # validates config + finds raw files
  python -m appshots render <project.json> [--styles a,b] [--platforms iphone,android] [--out DIR]
  python -m appshots validate <out-dir>
"""
import argparse
import os
import shutil
import sys

from PIL import Image, ImageDraw

from . import discover, engine as E, validate
from .project import Project, ConfigError
from .styles import STYLES

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def cmd_render(a):
    proj = Project(a.project)
    styles = list(STYLES) if a.styles in (None, "all") else [s.strip() for s in a.styles.split(",")]
    for s in styles:
        if s not in STYLES:
            sys.exit(f"unknown style '{s}'. Available: {', '.join(STYLES)}")
    plats = list(proj.platforms) if not a.platforms else [p.strip() for p in a.platforms.split(",")]
    out = os.path.abspath(a.out or os.path.join(proj.root, "final"))
    for plat in plats:
        if not proj.messages_for(plat):
            print(f"skip {plat}: no messages have ui for it")
            continue
        sheets = []
        for name in styles:
            d = os.path.join(out, plat, name)
            os.makedirs(d, exist_ok=True)
            imgs = [im.convert("RGB") for im in STYLES[name].render(proj, plat)]
            for f in os.listdir(d):
                if f.startswith("screenshot-") and f.endswith(".png"):
                    os.remove(os.path.join(d, f))  # only our own previous exports in this output folder
            for i, im in enumerate(imgs, 1):
                im.save(os.path.join(d, f"screenshot-{i:02d}.png"), optimize=True)
            sheets.append((STYLES[name].TITLE, E.contact_sheet(imgs, os.path.join(d, "contact-sheet.png"))))
            print(f"{plat:10s} {name:18s} {len(imgs)} x {imgs[0].size[0]}x{imgs[0].size[1]} -> {d}")
        if len(sheets) > 1:
            w = max(s.width for _, s in sheets)
            lab = 70
            m = Image.new("RGB", (w, sum(s.height + lab for _, s in sheets)), (250, 250, 248))
            y = 0
            for title, s in sheets:
                ImageDraw.Draw(m).text((28, y + 14), title.upper(), font=E.font("manrope", 44), fill=(30, 30, 30))
                m.paste(s, (0, y + lab))
                y += s.height + lab
            m.save(os.path.join(out, plat, "master-comparison.png"))
    expect = {p: proj.canvas(p) for p in plats}
    _, bad = validate.check_dir(out, expect)
    return 1 if bad else 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="appshots", description="Reference-driven store screenshot composer")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("discover", help="find existing raw screenshots in a project")
    p.add_argument("root"); p.add_argument("--json", action="store_true")
    p = sub.add_parser("init", help="write a project.json template")
    p.add_argument("dir")
    p = sub.add_parser("check", help="validate a project.json")
    p.add_argument("project")
    p = sub.add_parser("render", help="render styles")
    p.add_argument("project"); p.add_argument("--styles"); p.add_argument("--platforms"); p.add_argument("--out")
    p = sub.add_parser("validate", help="check exported files")
    p.add_argument("out")
    sub.add_parser("styles", help="list styles")
    a = ap.parse_args(argv)
    try:
        if a.cmd == "discover":
            discover.main(a.root, a.json)
        elif a.cmd == "init":
            os.makedirs(a.dir, exist_ok=True)
            dst = os.path.join(a.dir, "project.json")
            if os.path.exists(dst):
                sys.exit(f"{dst} exists; not overwriting")
            shutil.copy(os.path.join(HERE, "templates", "project.template.json"), dst)
            print(dst)
        elif a.cmd == "check":
            pr = Project(a.project)
            for plat in pr.platforms:
                print(f"{plat}: {len(pr.messages_for(plat))} messages, canvas {pr.canvas(plat)}")
            print("config OK")
        elif a.cmd == "render":
            return cmd_render(a)
        elif a.cmd == "validate":
            _, bad = validate.check_dir(a.out)
            return 1 if bad else 0
        elif a.cmd == "styles":
            for n, m in STYLES.items():
                print(f"{n:18s} {m.TITLE:18s} reference {m.REFERENCE}")
    except ConfigError as e:
        sys.exit(f"config error: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
