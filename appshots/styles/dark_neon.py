"""DARK NEON — reference D (dating app; design language only, not its subject).

Purple-tinted near-black. Condensed all-caps manifesto lines ending in full
stops, one word in neon lime or hot pink, alternating tile to tile. Copy and
phone swap top/bottom every tile (zig-zag). Depth from emitted light: real UI
cards get a 1-2 px neon outline and an outer glow; no drop shadows.
"""
from .. import engine as E
from ._base import flat_override, key_spans, unit

NAME = "dark-neon"
TITLE = "Dark Neon"
REFERENCE = "D: dating app (visual language only)"
P = dict(bg=("#16131C", "#09080C"), lime="#C8FC49", pink="#EE3497", purple="#7B4BFF", grey="#9C98A6")


def copy(project, m):
    return flat_override(project, NAME, m) or key_spans(m, upper=True, period=True)


def tile(project, plat, m, idx):
    W, H, s, dk = unit(project, plat)
    u = project.ui(plat, m)
    kind = m["kind"]
    acc = P["lime"] if idx % 2 == 0 else P["pink"]
    cv = E.linear(W, H, *P["bg"])
    E.blob(cv, W * 0.15, H * 0.30, W * 0.45, P["purple"], 0.35, W * 0.2)
    E.blob(cv, W * 0.90, H * 0.70, W * 0.40, acc, 0.16, W * 0.22)
    top_text = idx % 2 == 1
    dev, geo = E.device(project.device_kind(plat), project.screen(plat, u["screen"]), W * 0.84 * dk)
    lines = copy(project, m)
    if top_text:
        b = E.headline(cv, lines, "anton", 262 * s, W * 0.07, H * 0.06, W * 0.86, max_lines=3, lh=0.9, accent=acc)
        b = E.para(cv, project.sub(m), "manrope-md", 44 * s, W * 0.07, b + 26 * s, W * 0.8, P["grey"])
        dx, dy = (W - dev.width) / 2, b + H * 0.05
    else:
        dx, dy = (W - dev.width) / 2, H * 0.62 - dev.height
    E.glow_paste(cv, dev, (dx, dy), P["purple"], 0.35, 50 * s)
    if kind == "hero":
        spec, anchor = (u.get("strip") or u["card"]), u["card"][1]
    elif kind == "catalogue":
        f, box = u["tiles"][0]; spec, anchor = (f, box, 34), box
    else:
        spec, anchor = u["callout"], u["anchor"]
    cx, cy = E.map_box(geo, (dx, dy), anchor)
    c = E.crop_card(project.screen(plat, spec[0]), spec[1], spec[2], 1.08 * dk * (0.9 if kind == "list" else 1.0), W * 0.9,
                    stroke=acc, stroke_w=int(5 * s))
    y = cy + H * 0.08 if kind == "hero" else cy - c.height / 2
    y = min(max(y, H * 0.03), (H * 0.60 if not top_text else H * 0.96) - c.height)
    E.glow_paste(cv, c, ((W - c.width) / 2 + (W * 0.04 if top_text else -W * 0.04), y), acc, 0.55, 26 * s)
    if not top_text:
        b = E.headline(cv, lines, "anton", 262 * s, W * 0.07, H * 0.66, W * 0.86, max_lines=3, lh=0.9, accent=acc)
        E.para(cv, project.sub(m), "manrope-md", 44 * s, W * 0.07, b + 26 * s, W * 0.8, P["grey"])
    E.grain(cv, 5)
    return cv


def render(project, plat):
    return [tile(project, plat, m, i) for i, m in enumerate(project.messages_for(plat))]
