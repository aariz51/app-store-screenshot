"""MINIMAL EDITORIAL — reference E (playlist cover maker).

Light grey fields (lavender hero). Numbered steps 01..N, centred condensed caps
with one blue or magenta key word. Bento cells hold real UI (fanned real frames,
an editor field over transcript rows, a grid of catalogue tiles); later tiles
are a clean centred phone, bottom-cropped, with no ornament.
"""
from PIL import Image, ImageDraw

from .. import engine as E
from ._base import flat_override, key_spans, unit

NAME = "minimal-editorial"
TITLE = "Minimal Editorial"
REFERENCE = "E: playlist cover maker"
P = dict(bg="#F4F5F7", lav="#F1ECF4", ink="#101114", blue="#2198E3", mag="#B73968", card="#FFFFFF", shadow="#6C7280")


def copy(project, m):
    return flat_override(project, NAME, m) or key_spans(m, upper=True)


def cell(cv, box, s, fill=None):
    x0, y0, x1, y1 = [int(v) for v in box]
    c = Image.new("RGBA", (x1 - x0, y1 - y0), E.hx(fill or P["card"]))
    c.putalpha(E.rounded_mask(c.size, int(46 * s)))
    E.drop(cv, c, (x0, y0), P["shadow"], 0.10, 24 * s, (0, 10 * s))


def tile(project, plat, m, idx):
    W, H, s, dk = unit(project, plat)
    u = project.ui(plat, m)
    kind = m["kind"]
    cv = Image.new("RGBA", (W, H), E.hx(P["lav"] if kind == "hero" else P["bg"]))
    acc = P["blue"] if idx % 2 == 0 else P["mag"]
    g = W * 0.035
    lines = copy(project, m)

    def head(y, step=None):
        sp = ([(f"{step}. ", None)] + lines) if step else lines   # reference E: "1. FIND WHAT YOU LIKE"
        b = E.headline(cv, sp, "barlow", 200 * s, W * 0.07, y + 24 * s, W * 0.86, max_lines=3, align="center", lh=0.92, color=P["ink"], accent=acc)
        return E.para(cv, project.sub(m), "manrope-md", 42 * s, W * 0.12, b + 22 * s, W * 0.76, "#5A5E68", align="center")

    def crop(spec, scale, maxw, **kw):
        return E.crop_card(project.screen(plat, spec[0]), spec[1], spec[2], scale, maxw, **kw)

    if kind == "hero":  # reference E tile 1: hero card of fanned real frames over a second card
        cell(cv, (g, g, W - g, H * 0.70), s, "#E7E0EE")
        fr = u["frames"]
        n = len(fr)
        for i, (f, box) in enumerate(fr[:3]):
            c = crop((f, box, 40), 0.92 * dk, W * (0.5 if n == 3 else 0.62), rot=[8, -8, 0][i] if n == 3 else -3)
            ox = [-0.20, 0.20, 0.0][i] if n == 3 else 0
            E.drop(cv, c, (W / 2 - c.width / 2 + W * ox, H * 0.05 + (0 if i == min(n, 3) - 1 else H * 0.03)), "#4A3A5C", 0.22, 30 * s, (0, 20 * s))
        E.headline(cv, lines, "barlow", 190 * s, W * 0.07, H * 0.52, W * 0.86, max_lines=3, align="center", lh=0.92, color=P["ink"], accent=acc)
        bot = (g, H * 0.70 + g, W - g, H - g)
        cell(cv, bot, s)
        mid_y = (bot[1] + bot[3]) / 2
        if "strip" in u:
            st = crop(u["strip"], 0.86 * dk, W * 0.84, hair=False)
            E.paste_any(cv, st, (int(W / 2 - st.width / 2), int(mid_y - st.height / 2 - 20 * s)))
            mid_y += st.height / 2
        E.para(cv, project.sub(m), "manrope-md", 40 * s, W * 0.12, mid_y, W * 0.76, "#5A5E68", align="center")
    elif kind in ("detail", "catalogue"):  # reference E tile 2: bento cells of real UI under centred copy
        b = head(H * 0.04)
        y0 = b + H * 0.03
        if kind == "detail":
            c = crop(u["callout"], 1.0 * dk, (W - 2 * g) * 0.9, hair=False)
            a = (g, y0, W - g, y0 + c.height + 2 * W * (0.06 if "rows" in u else 0.08))
            cell(cv, a, s)
            E.paste_any(cv, c, (int(W / 2 - c.width / 2), int((a[1] + a[3]) / 2 - c.height / 2)))
            if "rows" not in u:  # no second cell: the real screen continues below, bottom-cropped
                dev, _ = E.device(project.device_kind(plat), project.screen(plat, u["screen"]), W * 0.80 * dk)
                E.drop(cv, dev, ((W - dev.width) / 2, a[3] + H * 0.035), P["shadow"], 0.18, 40 * s, (0, 24 * s))
            if "rows" in u:
                bb = (g, a[3] + g, W - g, H - g)
                cell(cv, bb, s)
                r = crop(u["rows"], 0.9 * dk, (bb[2] - bb[0]) * 0.92, hair=False)
                r = r.crop((0, 0, r.width, min(r.height, int(bb[3] - bb[1] - 2 * g))))
                E.paste_any(cv, r, (int(W / 2 - r.width / 2), int(bb[1] + g)))
        else:
            cw = (W - g * 3) / 2
            for i, (f, box) in enumerate(u["tiles"][:8]):
                t = project.screen(plat, f).crop(box).convert("RGB")
                ch = cw * t.height / t.width
                cx0, cy0 = g + (i % 2) * (cw + g), y0 + (i // 2) * (ch + g)
                if cy0 + ch > H:
                    break
                t = t.resize((int(cw), int(ch)), Image.LANCZOS).convert("RGBA")
                t.putalpha(E.rounded_mask(t.size, int(40 * s)))
                E.drop(cv, t, (cx0, cy0), P["shadow"], 0.12, 24 * s, (0, 10 * s))
    else:  # reference E tiles 3-4: numbered step, centred copy, full-width phone bottom-cropped, no ornament
        step = 1 + sum(1 for mm in project.messages_for(plat)[:idx] if mm["kind"] not in ("hero", "detail", "catalogue"))
        b = head(H * 0.04, step)
        dev, _ = E.device(project.device_kind(plat), project.screen(plat, u["screen"]), W * 0.86 * dk)
        E.drop(cv, dev, ((W - dev.width) / 2, b + H * 0.04), P["shadow"], 0.18, 40 * s, (0, 24 * s))
    return cv


def render(project, plat):
    return [tile(project, plat, m, i) for i, m in enumerate(project.messages_for(plat))]
