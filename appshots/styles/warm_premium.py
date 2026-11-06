"""WARM PREMIUM — reference A (couples expense tracker).

Coral gradient fields alternating with warm cream. Heavy sentence-case sans,
left-aligned, one brand-orange key word. Tiles 1-2 are one panorama: a giant
tilted phone straddles the seam. Real UI cards are enlarged wider than the
phone. Phones bleed off the top or bottom. Shadows are warm-tinted, never grey.
"""
from PIL import Image, ImageChops, ImageDraw, ImageFilter

from .. import engine as E
from ._base import default_two_tone, override_lines, region, unit

NAME = "warm-premium"
TITLE = "Warm Premium"
REFERENCE = "A: couples expense tracker"
P = dict(coral=("#FDA273", "#FE8D6C"), cream=("#F9F8F4", "#F3F0EA"), ink="#201B19", orange="#EB8442", shadow="#8A3E22")
FIELD = {"hero": "coral", "detail": "cream", "catalogue": "cream", "feature": "cream", "list": "coral", "output": "cream"}


def copy(project, m):
    return override_lines(project, NAME, m) or default_two_tone(m, period=True)


def bg(W, H, field):
    cv = E.linear(W, H, *P[field])
    if field == "coral":
        E.blob(cv, W * 0.85, H * 0.08, W * 0.5, "#FFC7A3", 0.35, W * 0.2)
    return cv


def head(cv, project, m, field, x, y, maxw, s):
    on = field == "coral"
    b = E.text(cv, copy(project, m), "manrope", 168 * s, x, y, maxw, lh=1.02,
               color="#FFFFFF" if on else P["ink"], accent="#FFFFFF" if on else P["orange"])
    return E.para(cv, project.sub(m), "manrope-md", 52 * s, x, b + 30 * s, maxw * 0.9, "#FFF4EC" if on else "#5B524D")


def card(project, plat, spec, scale, maxw, **kw):
    img, box, r = region(project, plat, spec)
    return E.crop_card(img, box, r, scale, maxw, **kw)


def panorama(project, plat, m1, m2):
    """Tiles 1+2 share one 2W canvas; a giant tilted phone (tile 2's screen) crosses the seam."""
    W, H, s, dk = unit(project, plat)
    u1, u2 = project.ui(plat, m1), project.ui(plat, m2)
    cv = Image.new("RGBA", (W * 2, H))
    cv.alpha_composite(bg(W, H, "coral"), (0, 0))
    cv.alpha_composite(bg(W, H, "coral"), (W, 0))
    mx = W * 0.115
    t1 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    head(t1, project, m1, "coral", mx, H * 0.075, W * 0.72, s)
    dev, _ = E.device(project.device_kind(plat), project.screen(plat, u2["screen"]), W * 1.30 * dk)
    rot = dev.rotate(-9, resample=Image.BICUBIC, expand=True)
    E.drop(cv, rot, (W * 1.08 - rot.width / 2 + W * 0.34, H * 0.40 - rot.height / 2), P["shadow"], 0.35, 60 * s, (0, 50 * s))
    cv.alpha_composite(t1)
    c = card(project, plat, u1["card"], 1.05 * dk, W * 0.46, rot=-4)
    E.drop(cv, c, (mx * 0.9, H * 0.44), P["shadow"], 0.30, 40 * s, (0, 32 * s))
    if "strip" in u1:
        st = card(project, plat, u1["strip"], 0.86 * dk, W * 0.86, rot=2)
        E.drop(cv, st, (W * 0.30, H * 0.44 + c.height * 0.98), P["shadow"], 0.28, 36 * s, (0, 28 * s))
    # tile 2: caption band under the oversized phone (reference A tile 2)
    t2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(t2).rectangle([0, H * 0.80, W, H], fill=E.hx(P["coral"][1]))
    yb = E.text(t2, copy(project, m2), "manrope", 120 * s, W * 0.1, H * 0.835, W * 0.8, align="center", lh=1.02,
                color="#FFFFFF", accent="#FFFFFF")
    E.para(t2, project.sub(m2), "manrope-md", 46 * s, W * 0.1, yb + 22 * s, W * 0.8, "#FFF4EC", align="center")
    fade = Image.new("L", (W, H), 0)
    ImageDraw.Draw(fade).rectangle([0, H * 0.80, W, H], fill=255)
    t2.putalpha(ImageChops.multiply(t2.getchannel("A"), fade.filter(ImageFilter.GaussianBlur(2))))
    cv.alpha_composite(t2, (W, 0))
    fld = card(project, plat, u2["callout"], 1.0 * dk, W * 0.86, rot=-2)
    E.drop(cv, fld, (W + W * 0.07, H * 0.50), P["shadow"], 0.30, 36 * s, (0, 28 * s))
    E.grain(cv)
    return [cv.crop((0, 0, W, H)), cv.crop((W, 0, 2 * W, H))]


def tile(project, plat, m):
    W, H, s, dk = unit(project, plat)
    u = project.ui(plat, m)
    kind = m["kind"]
    field = FIELD[kind]
    cv = bg(W, H, field)
    mx = W * 0.115
    kd = E.device(project.device_kind(plat), project.screen(plat, u["screen"]), W * (0.86 if kind == "feature" else 0.84 if kind != "output" else 0.78) * dk)
    dev = kd[0]
    if kind == "feature":  # reference A tile 4: phone from the top, copy at the bottom
        dx, dy = (W - dev.width) / 2, H * 0.60 - dev.height
        E.drop(cv, dev, (dx, dy), P["shadow"], 0.22, 50 * s, (0, 40 * s))
        c = card(project, plat, u["callout"], 1.15 * dk, W * 0.94)
        E.drop(cv, c, ((W - c.width) / 2, H * 0.50 - c.height / 2), P["shadow"], 0.30, 36 * s, (0, 30 * s))
        head(cv, project, m, field, mx, H * 0.665, W * 0.78, s)
    elif kind == "output":  # reference A tile 6: tilted phone, floating object tiles (no hand)
        b = head(cv, project, m, field, mx, H * 0.075, W * 0.78, s)
        rot = dev.rotate(10, resample=Image.BICUBIC, expand=True)
        E.drop(cv, rot, ((W - rot.width) / 2 + W * 0.06, b + H * 0.07), P["shadow"], 0.28, 60 * s, (0, 50 * s))
        spots = [(0.04, 0.42, 12), (0.74, 0.55, -10), (0.06, 0.70, -8), (0.76, 0.80, 8)]
        for lab, (x, y, r) in zip(u["badges"], spots):
            t = E.badge_tile(W * 0.20, lab, "#FFFFFF", P["orange"]).rotate(r, resample=Image.BICUBIC, expand=True)
            E.drop(cv, t, (W * x, H * y), P["shadow"], 0.25, 30 * s, (0, 22 * s))
    else:  # reference A tiles 3/5: copy top-left, phone bottom-cropped, magnified cards wider than the phone
        b = head(cv, project, m, field, mx, H * 0.075, W * 0.78, s)
        dx, dy = (W - dev.width) / 2, b + H * 0.045
        E.drop(cv, dev, (dx, dy), P["shadow"], 0.22, 50 * s, (0, 40 * s))
        if kind == "catalogue":
            tiles = u["tiles"]
            for i, (f, box) in enumerate([tiles[0], tiles[min(7, len(tiles) - 1)]]):
                c = card(project, plat, (f, box, 34), 1.05 * dk * (1.25 if i == 0 else 1.0), W * 0.62, rot=(-3 if i == 0 else 2))
                x = W * 0.04 if i == 0 else W - c.width - W * 0.04
                E.drop(cv, c, (x, dy + H * (0.08 if i == 0 else 0.30)), P["shadow"], 0.28, 36 * s, (0, 30 * s))
        else:
            spec = u.get("top") or u.get("callout") or u.get("card")
            c = card(project, plat, spec, 1.15 * dk, W * 0.70, rot=-2)
            E.drop(cv, c, (W - c.width - W * 0.03, dy + H * 0.12), P["shadow"], 0.30, 36 * s, (0, 30 * s))
    E.grain(cv)
    return cv


def render(project, plat):
    ms = project.messages_for(plat)
    if len(ms) >= 2 and ms[0]["kind"] == "hero" and "callout" in project.ui(plat, ms[1]):
        return panorama(project, plat, ms[0], ms[1]) + [tile(project, plat, m) for m in ms[2:]]
    return [tile(project, plat, m) for m in ms]
