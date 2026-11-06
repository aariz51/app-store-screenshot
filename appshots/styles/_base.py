"""Helpers shared by the style modules (layout units, copy fallbacks)."""
from ..project import spans_from_json, tag_key, two_lines


def unit(project, plat):
    """W, H, scale relative to the 1320x2868 design grid, device-width factor."""
    W, H = project.canvas(plat)
    s = min(W / 1320, H / 2868)
    dk = 1.0 if project.device_kind(plat) == "iphone" else 0.80  # taller Android screens get a narrower phone
    return W, H, s, dk


def override_lines(project, style, m):
    o = project.copy_override(style, m)
    return spans_from_json(o) if isinstance(o, list) else None


def default_two_tone(m, upper=False, period=False):
    """Two balanced lines, the key phrase tagged 'k'."""
    head = m["headline"].upper() if upper else m["headline"]
    key = m.get("key", "")
    key = key.upper() if upper else key
    lines = [tag_key(l, key) for l in two_lines(head)]
    if period:
        out = []
        for sp in lines:
            t, g = sp[-1]
            if not t.rstrip().endswith((".", "!", "?")):
                sp = sp[:-1] + [(t.rstrip() + ".", g)]
            out.append(sp)
        lines = out
    return [(sp, 1.0) for sp in lines]


def region(project, plat, spec):
    """spec (file, box, radius) -> (PIL image, box, radius)."""
    return project.screen(plat, spec[0]), spec[1], spec[2]
