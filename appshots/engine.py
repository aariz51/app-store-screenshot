"""Shared rendering primitives: masks, devices, shadows, glows, cards, type.

Everything here is style-agnostic. Styles in appshots/styles/ compose these.
Raw screenshots are only read: cropped, scaled, masked, rotated.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONTS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "fonts")
SS = 4  # supersampling for anti-aliased masks


def hx(h, a=255):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (a,)


# ------------------------------------------------------------------ fonts
_FONT_FILES = {
    "anton": ("Anton-Regular.ttf", None),
    "barlow": ("BarlowCondensed-ExtraBold.ttf", None),
    "baloo": ("Baloo2-Variable.ttf", 800),
    "manrope": ("Manrope-Variable.ttf", 800),
    "manrope-sb": ("Manrope-Variable.ttf", 600),
    "manrope-md": ("Manrope-Variable.ttf", 500),
}
_fc = {}


def font(name, px):
    key = (name, int(px))
    if key not in _fc:
        file, weight = _FONT_FILES[name]
        f = ImageFont.truetype(os.path.join(FONTS, file), max(1, int(px)))
        if weight:
            f.set_variation_by_axes([weight])
        _fc[key] = f
    return _fc[key]


# ------------------------------------------------------------------ compositing
def rounded_mask(size, radius):
    w, h = size
    m = Image.new("L", (w * SS, h * SS), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w * SS - 1, h * SS - 1], radius * SS, fill=255)
    return m.resize((w, h), Image.LANCZOS)


def paste_any(canvas, img, xy):
    """alpha_composite that tolerates negative offsets and overflow."""
    x, y = int(xy[0]), int(xy[1])
    cx0, cy0 = max(0, -x), max(0, -y)
    cx1, cy1 = min(img.width, canvas.width - x), min(img.height, canvas.height - y)
    if cx1 <= cx0 or cy1 <= cy0:
        return
    canvas.alpha_composite(img.crop((cx0, cy0, cx1, cy1)), (x + cx0, y + cy0))


def linear(W, H, top, bot):
    g = Image.new("RGBA", (1, 256))
    a, b = hx(top), hx(bot)
    for y in range(256):
        t = y / 255
        g.putpixel((0, y), tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(4)))
    return g.resize((int(W), int(H)), Image.BICUBIC)


def blob(cv, cx, cy, r, color, alpha, blur):
    W, H = cv.size
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).ellipse([cx - r, cy - r, cx + r, cy + r], fill=int(255 * alpha))
    m = m.filter(ImageFilter.GaussianBlur(blur))
    layer = Image.new("RGBA", (W, H), hx(color)[:3] + (0,))
    layer.putalpha(m)
    cv.alpha_composite(layer)


def grain(cv, amt=5):
    """1-2% luminance noise so large gradients do not band."""
    W, H = cv.size
    n = Image.effect_noise((W, H), 6).convert("L")
    cv.alpha_composite(Image.merge("RGBA", (n, n, n, Image.new("L", (W, H), amt))))


def drop(cv, img, xy, color="#000000", alpha=0.25, blur=40, off=(0, 30)):
    """Paste with a soft, tinted drop shadow."""
    pad = int(blur * 3)
    sh = Image.new("L", (img.width + 2 * pad, img.height + 2 * pad), 0)
    sh.paste(img.getchannel("A"), (pad, pad))
    sh = sh.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * alpha))
    layer = Image.new("RGBA", sh.size, hx(color)[:3] + (0,))
    layer.putalpha(sh)
    paste_any(cv, layer, (xy[0] - pad + off[0], xy[1] - pad + off[1]))
    paste_any(cv, img, xy)


def glow_paste(cv, img, xy, color, strength=0.7, blur=30):
    """Paste with an emitted glow instead of a shadow (dark fields)."""
    pad = int(blur * 3)
    g = Image.new("L", (img.width + 2 * pad, img.height + 2 * pad), 0)
    g.paste(img.getchannel("A"), (pad, pad))
    g = g.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * strength))
    layer = Image.new("RGBA", g.size, hx(color)[:3] + (0,))
    layer.putalpha(g)
    paste_any(cv, layer, (xy[0] - pad, xy[1] - pad))
    paste_any(cv, img, xy)


# ------------------------------------------------------------------ devices
def device(kind, screen, dev_w):
    """Draw a generic, logo-free phone around a real screenshot.

    kind: "iphone" (Dynamic Island, titanium rim) or "android" (punch-hole, matte rim).
    Returns (RGBA image, geometry) where geometry maps screen pixels into the device.
    """
    dev_w = int(dev_w)
    if kind == "iphone":
        bezel, rim = round(dev_w * 0.030), round(dev_w * 0.009)
        scr_r_k, rim_col = 0.125, [(196, 198, 204), (122, 124, 131)]
    else:
        bezel, rim = round(dev_w * 0.026), round(dev_w * 0.006)
        scr_r_k, rim_col = 0.075, [(70, 72, 77), (34, 35, 38)]
    scr_w = dev_w - 2 * (bezel + rim)
    scr_h = round(scr_w * screen.height / screen.width)
    dev_h = scr_h + 2 * (bezel + rim)
    scr_r = round(scr_w * scr_r_k)
    out_r = scr_r + bezel + rim
    dev = Image.new("RGBA", (dev_w, dev_h), (0, 0, 0, 0))
    g = Image.new("RGB", (1, 2))
    g.putpixel((0, 0), rim_col[0]); g.putpixel((0, 1), rim_col[1])
    rimimg = g.resize((dev_w, dev_h), Image.BICUBIC).convert("RGBA")
    rimimg.putalpha(rounded_mask((dev_w, dev_h), out_r))
    dev.alpha_composite(rimimg)
    body = Image.new("RGBA", (dev_w - 2 * rim, dev_h - 2 * rim), (10, 10, 12, 255))
    body.putalpha(rounded_mask(body.size, out_r - rim))
    dev.alpha_composite(body, (rim, rim))
    scr = screen.resize((scr_w, scr_h), Image.LANCZOS).convert("RGBA")
    scr.putalpha(rounded_mask((scr_w, scr_h), scr_r))
    ox = oy = bezel + rim
    dev.alpha_composite(scr, (ox, oy))
    if kind == "iphone":
        iw, ih = round(scr_w * 0.286), round(scr_w * 0.084)
        m = Image.new("L", (iw * SS, ih * SS), 0)
        ImageDraw.Draw(m).rounded_rectangle([0, 0, iw * SS - 1, ih * SS - 1], ih * SS // 2, fill=255)
        isl = Image.new("RGBA", (iw, ih), (0, 0, 0, 255)); isl.putalpha(m.resize((iw, ih), Image.LANCZOS))
        dev.alpha_composite(isl, (ox + (scr_w - iw) // 2, oy + round(scr_w * 0.026)))
    else:
        dmt = round(scr_w * 0.034)
        m = Image.new("L", (dmt * SS, dmt * SS), 0)
        ImageDraw.Draw(m).ellipse([0, 0, dmt * SS - 1, dmt * SS - 1], fill=255)
        cam = Image.new("RGBA", (dmt, dmt), (6, 6, 8, 255)); cam.putalpha(m.resize((dmt, dmt), Image.LANCZOS))
        dev.alpha_composite(cam, (ox + scr_w // 2 - dmt // 2, oy + round(scr_w * 0.034) - dmt // 2))
    hm = Image.new("L", (dev_w, dev_h), 0)
    ImageDraw.Draw(hm).rounded_rectangle([rim, rim, dev_w - rim - 1, dev_h - rim - 1], out_r - rim, outline=38, width=max(2, rim // 2))
    hl = Image.new("RGBA", (dev_w, dev_h), (255, 255, 255, 0)); hl.putalpha(hm)
    dev.alpha_composite(hl)
    return dev, {"scr_x": ox, "scr_y": oy, "scale": scr_w / screen.width}


def map_box(geo, dxy, box):
    """Centre of a raw-pixel box after the screen is placed in a device at dxy."""
    s = geo["scale"]
    return ((box[0] + box[2]) / 2 * s + geo["scr_x"] + dxy[0], (box[1] + box[3]) / 2 * s + geo["scr_y"] + dxy[1])


def crop_card(screen_img, box, radius, scale, maxw, rot=0, stroke=None, stroke_w=3, hair=True):
    """A real UI region, enlarged, rounded, optionally outlined and rotated."""
    c = screen_img.crop(box)
    s = min(scale, maxw / c.width)
    w, h = max(1, round(c.width * s)), max(1, round(c.height * s))
    c = c.resize((w, h), Image.LANCZOS).convert("RGBA")
    r = round(radius * s)
    c.putalpha(rounded_mask((w, h), r))
    if stroke or hair:
        st = Image.new("L", (w, h), 0)
        ImageDraw.Draw(st).rounded_rectangle([0, 0, w - 1, h - 1], r, outline=255, width=stroke_w if stroke else max(2, round(2 * s)))
        lay = Image.new("RGBA", (w, h), hx(stroke or "#FFFFFF")[:3] + (0,))
        lay.putalpha(st if stroke else st.point(lambda v: int(v * 0.55)))
        c.alpha_composite(lay)
    if rot:
        c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    return c


def badge_tile(size, label, bg, fg, radius=0.24):
    """A plain rounded tile carrying a short real label (e.g. an export format)."""
    size = int(size)
    t = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(t)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=int(size * radius), fill=hx(bg))
    if label in ("▶", "play"):
        c, r = size / 2, size * 0.2
        d.polygon([(c - r * 0.7, c - r), (c - r * 0.7, c + r), (c + r, c)], fill=hx(fg))
    else:
        f = font("manrope", size * (0.30 if len(label) <= 4 else 0.20))
        d.text((size / 2, size / 2), label, font=f, fill=hx(fg), anchor="mm")
    return t


def sparkle(cv, cx, cy, r, color):
    pts = []
    for i in range(8):
        a = math.pi / 4 * i
        rr = r if i % 2 == 0 else r * 0.28
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    ImageDraw.Draw(cv).polygon(pts, fill=hx(color))


# ------------------------------------------------------------------ type
def _measure(f, spans):
    return sum(f.getlength(t) for t, _ in spans)


def text(cv, lines, fname, size, x, y, maxw, align="left", lh=0.95, color="#FFFFFF", accent="#FFFFFF",
         sticker=("#FFFFFF", "#1C3A63"), pill=("#FFFFFF", "#2682FD"), upper=False):
    """Draw a headline. lines: [(spans, scale)], spans: [(text, tag)], tag in None|'k'|'stk'|'pill'.

    Size auto-fits so the widest line fits maxw. Returns the bottom y.
    """
    if upper:
        lines = [([(t.upper(), g) for t, g in sp], sc) for sp, sc in lines]
    probe = font(fname, 200)
    fit = min(size, min(maxw * 200 / (_measure(probe, sp) * sc + 1e-6) for sp, sc in lines))
    d = ImageDraw.Draw(cv)
    cy = y
    for spans, sc in lines:
        fs = fit * sc
        f = font(fname, fs)
        asc = f.getbbox("H")[1]
        cap = f.getbbox("H")[3] - asc
        wline = _measure(f, spans)
        cx = x if align == "left" else x + (maxw - wline) / 2
        for t, tag in spans:
            tw = f.getlength(t)
            if tag == "pill":
                bg, fg = pill
                pad = fs * 0.16
                d.rounded_rectangle([cx - pad * 0.2, cy - pad * 0.55, cx + f.getlength(t.rstrip()) + pad * 1.4, cy + cap + pad * 0.75],
                                    radius=fs * 0.28, fill=hx(bg))
                d.text((cx + pad * 0.6, cy - asc), t, font=f, fill=hx(fg))
                tw += pad * 1.6
            elif tag == "stk":
                fill, edge = sticker
                sw = max(3, int(fs * 0.075))
                d.text((cx + fs * 0.05, cy - asc + fs * 0.06), t, font=f, fill=hx(edge), stroke_width=sw, stroke_fill=hx(edge))
                d.text((cx, cy - asc), t, font=f, fill=hx(fill), stroke_width=sw, stroke_fill=hx(edge))
            else:
                d.text((cx, cy - asc), t, font=f, fill=hx(accent if tag == "k" else color))
            cx += tw
        cy += cap + fs * (lh - 0.72)
    return cy


def para(cv, s, fname, px, x, y, maxw, color, align="left", lh=1.3, upper=False):
    """Wrapped supporting copy. Returns the bottom y."""
    if not s:
        return y
    if upper:
        s = s.upper()
    f = font(fname, px)
    ls, cur = [], ""
    for w_ in s.split():
        t = (cur + " " + w_).strip()
        if f.getlength(t) <= maxw:
            cur = t
        else:
            ls.append(cur); cur = w_
    ls.append(cur)
    d = ImageDraw.Draw(cv)
    for i, l in enumerate(ls):
        lx = x if align == "left" else x + (maxw - f.getlength(l)) / 2
        d.text((lx, y + i * px * lh), l, font=f, fill=hx(color))
    return y + len(ls) * px * lh


def contact_sheet(imgs, path, th=900, bg=(232, 231, 228)):
    W, H = imgs[0].size
    tw, g = round(th * W / H), 28
    sh = Image.new("RGB", (len(imgs) * (tw + g) + g, th + 2 * g), bg)
    for i, im in enumerate(imgs):
        sh.paste(im.resize((tw, th), Image.LANCZOS), (g + i * (tw + g), g))
    sh.save(path)
    return sh
