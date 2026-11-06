"""Smoke tests: every style renders every message kind on both platforms.

Uses synthetic fixture screens (plain blocks, labelled TEST FIXTURE) so the
suite needs no real app screenshots. Run: python -m pytest  or  python tests/test_smoke.py
"""
import json
import os
import sys
import tempfile

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from appshots import discover, validate  # noqa: E402
from appshots.project import Project, ConfigError, two_lines, tag_key  # noqa: E402
from appshots.styles import STYLES  # noqa: E402

SIZES = {"iphone": (1320, 2868), "android": (1080, 2400)}


def fixture(path, size, hue):
    w, h = size
    im = Image.new("RGB", size, (244, 242, 236))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, w, int(h * 0.05)], fill=(20, 20, 24))
    d.rectangle([int(w * 0.2), int(h * 0.12), int(w * 0.8), int(h * 0.45)], fill=hue)
    for i in range(10):
        y = int(h * 0.5) + i * int(h * 0.045)
        d.rounded_rectangle([int(w * 0.05), y, int(w * 0.95), y + int(h * 0.035)], 20, fill=(255, 255, 255), outline=(220, 220, 220))
    d.text((40, int(h * 0.07)), "TEST FIXTURE", fill=(0, 0, 0))
    im.save(path)


def make_project(tmp):
    plats = {}
    for p, size in SIZES.items():
        d = os.path.join(tmp, "raw", p)
        os.makedirs(d)
        for i, n in enumerate(["home", "edit", "grid", "auto", "list", "out"]):
            fixture(os.path.join(d, n + ".png"), size, (60 + 30 * i, 90, 200 - 20 * i))
        plats[p] = {"device": "iphone" if p == "iphone" else "android", "canvas": [1320, 2868] if p == "iphone" else [1080, 1920], "raw_dir": f"raw/{p}"}

    def ui(p, screen, kind):
        w, h = SIZES[p]
        box = [int(w * 0.05), int(h * 0.5), int(w * 0.95), int(h * 0.62)]
        u = {"screen": screen, "callout": {"box": box, "radius": 24}}
        if kind == "hero":
            u = {"screen": screen, "card": {"box": [int(w * 0.2), int(h * 0.12), int(w * 0.8), int(h * 0.45)], "radius": 30},
                 "strip": {"box": box, "radius": 24}}
        if kind == "catalogue":
            u["tiles"] = [[int(w * 0.05), int(h * (0.5 + 0.045 * i)), int(w * 0.95), int(h * (0.535 + 0.045 * i))] for i in range(10)]
        if kind == "feature":
            u["lens"] = box
        return u

    kinds = [("home", "hero"), ("edit", "detail"), ("grid", "catalogue"), ("auto", "feature"), ("list", "list"), ("out", "output")]
    msgs = [{"id": n, "kind": k, "headline": f"Test headline number {i + 1}", "key": "headline", "sub": "Supporting line for the test.",
             "badges": ["ONE", "TWO"] if k == "output" else [], "ui": {p: ui(p, n, k) for p in SIZES}} for i, (n, k) in enumerate(kinds)]
    path = os.path.join(tmp, "project.json")
    json.dump({"app": {"name": "Fixture"}, "platforms": plats, "messages": msgs}, open(path, "w"))
    return path


def test_all_styles_render():
    with tempfile.TemporaryDirectory() as tmp:
        proj = Project(make_project(tmp))
        for plat in SIZES:
            for name, mod in STYLES.items():
                imgs = mod.render(proj, plat)
                assert len(imgs) == 6, (plat, name, len(imgs))
                for im in imgs:
                    assert im.size == proj.canvas(plat), (plat, name, im.size)
                    out = os.path.join(tmp, "x.png")
                    im.convert("RGB").save(out)
                    _, store, probs = validate.check_file(out, proj.canvas(plat))
                    assert not probs, (plat, name, probs)


def test_raw_files_untouched():
    with tempfile.TemporaryDirectory() as tmp:
        path = make_project(tmp)
        raw = os.path.join(tmp, "raw", "iphone", "home.png")
        before = open(raw, "rb").read()
        proj = Project(path)
        for mod in STYLES.values():
            mod.render(proj, "iphone")
        assert open(raw, "rb").read() == before


def test_config_errors():
    with tempfile.TemporaryDirectory() as tmp:
        path = make_project(tmp)
        cfg = json.load(open(path))
        cfg["messages"][0]["kind"] = "nope"
        json.dump(cfg, open(path, "w"))
        try:
            Project(path)
            assert False, "expected ConfigError"
        except ConfigError:
            pass


def test_copy_helpers_and_discover():
    assert two_lines("Auto captions for any video") == ["Auto captions", "for any video"]
    assert tag_key("Fix any word", "word") == [("Fix any ", None), ("word", "k")]
    assert discover.classify(1320, 2868)[0] == "iphone"
    assert validate.play_ok(1080, 1920) and not validate.play_ok(1280, 2856)


if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"):
            f(); print("ok", n)
