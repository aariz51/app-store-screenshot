"""BOLD BLUE — reference B (habit / screen-time app).

Saturated blue fields with white rest tiles. Centred heavy rounded display type
with word-level size jumps: the key word is set as an outlined sticker or a
label pill. Gold sparkles and a cloud band replace the reference's mascot and
characters (no people, animals or faces). Oversized real UI breaks the phone edge.
"""
from PIL import ImageDraw

from .. import engine as E
from ._base import override_lines, unit

NAME = "bold-blue"
TITLE = "Bold Blue"
REFERENCE = "B: habit / screen-time app"
P = dict(blue=("#3A95FF", "#1F74F0"), white=("#FFFFFF", "#F1F6FF"), navy="#15325C", gold="#F7CD1A", blue_k="#2682FD")
FIELDS = ["blue", "blue", "white", "blue", "white", "blue"]


def copy(project, m):
    o = override_lines(project, NAME, m)
    if o:
        return o
    head, key = m["headline"], m.get("key", "")
    if key and key.lower() in head.lower():
        i = head.lower().index(key.lower())
        pre, k, post = head[:i].strip(), head[i:i + len(key)], head[i + len(key):].strip()
    else:
        w = head.split(); pre, k, post = "", w[0], " ".join(w[1:])
    tag = "pill" if k[:1].isdigit() else "stk"
    lines = []
    if pre: lines.append(([(pre, None)], 0.62))
    lines.append(([(k, tag)], 1.18))
    if post: lines.append(([(post, None)], 0.62))
    return lines


def clouds(cv, W, H, y, s):
    lay = cv.copy(); lay.putalpha(0)
    d = ImageDraw.Draw(lay)
    for cx, r in [(0.02, 0.22), (0.26, 0.17), (0.50, 0.24), (0.76, 0.18), (0.98, 0.23)]:
        d.ellipse([W * cx - W * r, y - W * r * 0.6, W * cx + W * r, y + W * r * 1.4], fill=(255, 255, 255, 255))
    d.rectangle([0, y + W * 0.1, W, H], fill=(255, 255, 255, 255))
    E.drop(cv, lay, (0, 0), "#0B3E91", 0.18, 30 * s, (0, -10 * s))


def tile(project, plat, m, idx):
    W, H, s, dk = unit(project, plat)
    u = project.ui(plat, m)
    kind = m["kind"]
    field = FIELDS[idx % len(FIELDS)]
    blue = field == "blue"
    cv = E.linear(W, H, *P[field])
    if blue:
        E.blob(cv, W * 0.5, -H * 0.05, W * 0.75, "#8FC3FF", 0.45, W * 0.18)
    b = E.text(cv, copy(project, m), "baloo", 250 * s, W * 0.07, H * 0.055, W * 0.86, align="center", lh=0.98,
               color="#FFFFFF" if blue else "#10213F",
               sticker=("#FFFFFF", P["navy"]) if blue else (P["blue_k"], P["navy"]),
               pill=("#FFFFFF", P["blue_k"]) if blue else (P["blue_k"], "#FFFFFF"))
    b = E.para(cv, project.sub(m), "manrope-sb", 46 * s, W * 0.1, b + 26 * s, W * 0.8, "#E8F2FF" if blue else "#41557A", align="center")
    E.sparkle(cv, W * 0.88, H * 0.05, 46 * s, P["gold"])
    E.sparkle(cv, W * 0.11, b + 34 * s, 28 * s, "#FFFFFF" if blue else P["gold"])
    dev, geo = E.device(project.device_kind(plat), project.screen(plat, u["screen"]), W * 0.80 * dk)
    dx, dy = (W - dev.width) / 2, b + H * 0.05
    E.drop(cv, dev, (dx, dy), "#0B3E91" if blue else "#5C7BB0", 0.30, 50 * s, (0, 36 * s))
    if kind == "catalogue":
        f, box = u["tiles"][0]; spec = (f, box, 34)
    elif kind == "hero":
        spec = u.get("strip") or u["card"]
    else:
        spec = u["callout"]
    cx, cy = E.map_box(geo, (dx, dy), u["anchor"] if kind not in ("hero", "catalogue") and u["anchor"] else spec[1])
    c = E.crop_card(project.screen(plat, spec[0]), spec[1], spec[2], (1.0 if kind == "list" else 1.22) * dk, W * 1.02,
                    rot=(-5 if kind in ("hero", "feature") else 4))
    x = cx - c.width / 2 + (W * 0.10 if kind in ("detail", "output") else -W * 0.08)
    x = (W - c.width) / 2 if c.width >= W else min(max(x, 0), W - c.width)  # break the phone edge, never the canvas edge
    y = min(max(cy - c.height / 2, b + H * 0.02), H * 0.97 - c.height)
    if kind == "hero":
        y = dy + H * 0.36
    if kind == "feature":
        y = min(y, H * 0.78 - c.height)
    E.drop(cv, c, (x, y), P["navy"], 0.30, 30 * s, (0, 26 * s))
    if kind in ("hero", "feature"):
        clouds(cv, W, H, H * 0.93, s)
    E.grain(cv, 4)
    return cv


def render(project, plat):
    return [tile(project, plat, m, i) for i, m in enumerate(project.messages_for(plat))]
