"""FEATURE-LED — reference C (chat export utility).

One saturated blue on every tile with a light ellipse behind the phone. Huge
condensed all-caps benefit line plus a small caps qualifier, centred; the
detail tile flips the copy to the bottom. One demonstration device per tile:
a highlight band across the live content, a fan of real tiles, a magnifier
lens on the detail that proves the claim, fanned real format labels.
"""
from PIL import Image, ImageDraw

from .. import engine as E
from ..project import two_lines
from ._base import unit

NAME = "feature-led"
TITLE = "Feature-Led"
REFERENCE = "C: chat export utility"
P = dict(top="#2A82FA", deep="#145FD6", light="#BFD9FF", red="#FF4769", shadow="#06327A")


def copy(project, m):
    o = project.copy_override(NAME, m)
    if isinstance(o, dict):
        return o["big"], o["small"]
    ls = two_lines(m["headline"].upper())
    small = (m.get("qualifier") or (ls[1] if len(ls) > 1 else m.get("sub", ""))).upper()
    return ls[0], small


def card(project, plat, spec, scale, maxw, **kw):
    return E.crop_card(project.screen(plat, spec[0]), spec[1], spec[2], scale, maxw, **kw)


def lens(project, plat, file, box, d, s):
    src = project.screen(plat, file).crop(box).convert("RGBA")
    k = d * 0.92 / src.width
    src = src.resize((int(src.width * k), int(src.height * k)), Image.LANCZOS)
    out = Image.new("RGBA", (d, d), E.hx("#F6F4EE"))
    out.alpha_composite(src, ((d - src.width) // 2, max(0, (d - src.height) // 2)))
    m = Image.new("L", (d * 4, d * 4), 0)
    ImageDraw.Draw(m).ellipse([0, 0, d * 4 - 1, d * 4 - 1], fill=255)
    out.putalpha(m.resize((d, d), Image.LANCZOS))
    ring = Image.new("RGBA", (d, d), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse([4, 4, d - 5, d - 5], outline=(255, 255, 255, 255), width=int(14 * s))
    out.alpha_composite(ring)
    return out


def tile(project, plat, m):
    W, H, s, dk = unit(project, plat)
    u = project.ui(plat, m)
    kind = m["kind"]
    cv = E.linear(W, H, P["top"], P["deep"])
    big, small = copy(project, m)
    bottom = kind == "detail"
    dev, geo = E.device(project.device_kind(plat), project.screen(plat, u["screen"]), W * 0.80 * dk)
    dw = dev.width
    if not bottom:
        y1 = E.text(cv, [([(big, None)], 1.0)], "anton", 250 * s, W * 0.06, H * 0.06, W * 0.88, align="center", lh=0.9)
        y2 = E.text(cv, [([(small, None)], 1.0)], "anton", 92 * s, W * 0.10, y1 + 28 * s, W * 0.80, align="center", color=P["light"])
        E.blob(cv, W / 2, y2 + H * 0.33, W * 0.55, "#FFFFFF", 0.42, W * 0.14)
        dx, dy = (W - dw) / 2, y2 + H * 0.05
    else:
        E.blob(cv, W / 2, H * 0.32, W * 0.55, "#FFFFFF", 0.42, W * 0.14)
        dx, dy = (W - dw) / 2, H * 0.67 - dev.height
    E.drop(cv, dev, (dx, dy), P["shadow"], 0.35, 50 * s, (0, 36 * s))
    if kind == "hero":
        cx, cy = E.map_box(geo, (dx, dy), u["card"][1])
        band = Image.new("RGBA", (W, int(130 * s)), E.hx(P["red"])[:3] + (0,))
        band.putalpha(Image.new("L", band.size, 95))
        cv.alpha_composite(band.rotate(-6, expand=True, resample=Image.BICUBIC), (0, int(cy + H * 0.06)))
        c = card(project, plat, u.get("strip") or u["card"], 1.0 * dk, W * 0.9)
        E.drop(cv, c, ((W - c.width) / 2, cy + H * 0.20), P["shadow"], 0.35, 30 * s, (0, 24 * s))
    elif kind == "catalogue":
        t = u["tiles"]
        picks = [t[min(2, len(t) - 1)], t[-1], t[0]]
        for (f, box), r, ox in zip(picks, (10, -10, 0), (-0.30, 0.30, 0.0)):
            c = card(project, plat, (f, box, 34), 0.95 * dk, W * 0.6, rot=r)
            E.drop(cv, c, (W / 2 - c.width / 2 + W * ox, H * 0.66), P["shadow"], 0.35, 30 * s, (0, 24 * s))
    elif kind == "feature" and "lens" in u:
        cx, cy = E.map_box(geo, (dx, dy), u["lens"])
        d = int(W * 0.56)
        ln = lens(project, plat, (u.get("chip") or u["callout"])[0], u["lens"], d, s)
        E.drop(cv, ln, (W * 0.40, cy - d * 0.3), P["shadow"], 0.4, 30 * s, (0, 24 * s))
        c = card(project, plat, u["callout"], 1.05 * dk, W * 0.94)
        E.drop(cv, c, ((W - c.width) / 2, H * 0.80), P["shadow"], 0.35, 30 * s, (0, 24 * s))
    else:
        cx, cy = E.map_box(geo, (dx, dy), u["anchor"])
        c = card(project, plat, u["callout"], (0.95 if kind == "list" else 1.05) * dk * (1.25 if bottom else 1.0), W * 0.94)
        y = min(max(cy - c.height / 2, H * 0.03), H * 0.97 - c.height)
        E.drop(cv, c, ((W - c.width) / 2 + (W * 0.03 if kind == "output" else 0), y), P["shadow"], 0.35, 30 * s, (0, 24 * s))
        labels = [b for b in u["badges"] if b not in ("▶", "play")][:2]
        for lab, (x, r) in zip(labels, [(0.08, 10), (0.70, -10)]):
            t = E.badge_tile(W * 0.22, lab, "#FFFFFF", "#1B76F5").rotate(r, expand=True, resample=Image.BICUBIC)
            E.drop(cv, t, (W * x, H * 0.80), P["shadow"], 0.35, 24 * s, (0, 20 * s))
    if bottom:
        y1 = E.text(cv, [([(big, None)], 1.0)], "anton", 250 * s, W * 0.06, H * 0.74, W * 0.88, align="center", lh=0.9)
        E.text(cv, [([(small, None)], 1.0)], "anton", 92 * s, W * 0.10, y1 + 28 * s, W * 0.80, align="center", color=P["light"])
    E.grain(cv, 4)
    return cv


def render(project, plat):
    return [tile(project, plat, m) for m in project.messages_for(plat)]
