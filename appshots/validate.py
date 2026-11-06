"""Technical checks for exported store screenshots."""
import os

from PIL import Image

# Accepted portrait sizes. Re-check the stores' current lists before uploading.
STORE_SIZES = {
    "app-store-iphone-6.9": [(1320, 2868), (1290, 2796), (1260, 2736)],
    "app-store-iphone-6.5": [(1284, 2778), (1242, 2688)],
    "app-store-ipad-13": [(2064, 2752), (2048, 2732)],
}


def play_ok(w, h):
    """Google Play phone screenshots: 320-3840 px per side, long side at most 2x the short side."""
    lo, hi = min(w, h), max(w, h)
    return 320 <= lo and hi <= 3840 and hi <= 2 * lo


def check_file(path, expect=None):
    problems = []
    with Image.open(path) as im:
        w, h = im.size
        if im.mode != "RGB":
            problems.append(f"mode {im.mode} (needs RGB, no alpha)")
        if "transparency" in im.info:
            problems.append("has transparency")
    if expect and (w, h) != tuple(expect):
        problems.append(f"size {w}x{h}, expected {expect[0]}x{expect[1]}")
    store = [k for k, v in STORE_SIZES.items() if (w, h) in v]
    if not store and play_ok(w, h):
        store = ["google-play-phone"]
    if not store:
        problems.append(f"{w}x{h} matches no store size")
    if os.path.getsize(path) > 8 * 1024 * 1024:
        problems.append("larger than 8 MB")
    return (w, h), store, problems


def check_dir(root, expect_by_platform=None):
    bad = 0
    n = 0
    for dp, _, fns in sorted(os.walk(root)):
        for fn in sorted(fns):
            if not fn.startswith("screenshot-") or not fn.endswith(".png"):
                continue
            n += 1
            plat = os.path.basename(os.path.dirname(dp))
            exp = (expect_by_platform or {}).get(plat)
            size, store, probs = check_file(os.path.join(dp, fn), exp)
            status = "OK " if not probs else "FAIL"
            bad += bool(probs)
            print(f"{status} {os.path.relpath(os.path.join(dp, fn), root)}  {size[0]}x{size[1]}  {','.join(store)}  {'; '.join(probs)}")
    print(f"\n{n} screenshots checked, {bad} failing")
    return n, bad
