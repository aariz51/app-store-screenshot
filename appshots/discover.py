"""Find existing raw app screenshots in a project and classify them by platform.

Reads image headers only. Never moves, renames or edits anything.
"""
import json
import os

from PIL import Image

SKIP = {".git", "node_modules", "Pods", "build", ".build", "DerivedData", ".dart_tool", ".gradle", "dist", ".next",
        "out", ".venv", "venv", "__pycache__", ".expo", "vendor"}
HINTS = ("screenshot", "store", "fastlane", "app-store", "appstore", "play-store", "playstore", "marketing", "raw", "aso")

# Known device capture sizes (portrait). Anything else is classified by aspect ratio.
IOS = {(1320, 2868): "iPhone 6.9\"", (1290, 2796): "iPhone 6.7\"", (1284, 2778): "iPhone 6.5\"", (1242, 2688): "iPhone 6.5\"",
       (1179, 2556): "iPhone 6.1\"", (1206, 2622): "iPhone 6.3\"", (1170, 2532): "iPhone 6.1\"", (1242, 2208): "iPhone 5.5\"",
       (2064, 2752): "iPad 13\"", (2048, 2732): "iPad 12.9\""}


def classify(w, h):
    if (w, h) in IOS:
        return ("ipad" if "iPad" in IOS[(w, h)] else "iphone"), IOS[(w, h)]
    if h <= w:
        return "landscape-or-other", ""
    r = h / w
    if 2.0 < r < 2.4:
        return "android-or-iphone", "tall phone"
    if 1.3 < r < 1.5:
        return "tablet", ""
    return "other", ""


def scan(root, min_side=900):
    found = []
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP and not d.startswith(".")]
        for fn in fns:
            if not fn.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                continue
            p = os.path.join(dp, fn)
            try:
                with Image.open(p) as im:
                    w, h = im.size
            except Exception:
                continue
            if min(w, h) < min_side:
                continue
            plat, label = classify(w, h)
            rel = os.path.relpath(p, root)
            found.append({"path": os.path.abspath(p), "rel": rel, "width": w, "height": h, "platform": plat, "device": label,
                          "hinted": any(k in rel.lower() for k in HINTS)})
    found.sort(key=lambda f: (not f["hinted"], os.path.dirname(f["rel"]), f["rel"]))
    return found


def main(root, as_json=False):
    res = scan(root)
    if as_json:
        print(json.dumps(res, indent=1))
        return res
    if not res:
        print("No candidate screenshots found (portrait images with short side >= 900 px).")
        return res
    cur = None
    for f in res:
        d = os.path.dirname(f["rel"]) or "."
        if d != cur:
            cur = d
            print(f"\n{os.path.join(root, d)}")
        print(f"  {os.path.basename(f['rel']):40s} {f['width']}x{f['height']}  {f['platform']} {f['device']}")
    return res
