"""Project config: which real screens, which UI regions, which messages.

A project file (JSON) describes one app. See templates/project.template.json
and docs/configuration.md. Paths in it are relative to the file itself.
"""
import json
import os

from PIL import Image, ImageFilter

KINDS = ("hero", "detail", "catalogue", "feature", "list", "output")
REGION_ROLES = ("callout", "card", "strip", "rows", "chip", "top")


class ConfigError(ValueError):
    pass


class Project:
    def __init__(self, path):
        self.path = os.path.abspath(path)
        self.root = os.path.dirname(self.path)
        with open(self.path) as f:
            self.cfg = json.load(f)
        self.app = self.cfg.get("app", {})
        self.platforms = self.cfg["platforms"]
        self.messages = self.cfg["messages"]
        self._cache = {}
        self.check()

    # ---------------------------------------------------------- validation
    def check(self):
        if not self.messages:
            raise ConfigError("project has no messages")
        for p, P in self.platforms.items():
            if P.get("device") not in ("iphone", "android"):
                raise ConfigError(f"platform {p}: device must be 'iphone' or 'android'")
            if len(P.get("canvas", [])) != 2:
                raise ConfigError(f"platform {p}: canvas must be [width, height]")
        for m in self.messages:
            for k in ("id", "kind", "headline"):
                if k not in m:
                    raise ConfigError(f"message {m.get('id', '?')}: missing '{k}'")
            if m["kind"] not in KINDS:
                raise ConfigError(f"message {m['id']}: kind must be one of {KINDS}")
            for plat, ui in m.get("ui", {}).items():
                if plat not in self.platforms:
                    raise ConfigError(f"message {m['id']}: ui for unknown platform '{plat}'")
                if "screen" not in ui:
                    raise ConfigError(f"message {m['id']} [{plat}]: ui needs 'screen'")
                need = {"hero": ("card",), "catalogue": ("tiles",)}.get(m["kind"], ())
                for role in need:
                    if role not in ui:
                        raise ConfigError(f"message {m['id']} [{plat}]: kind '{m['kind']}' needs ui.{role}")
                if m["kind"] not in ("hero", "catalogue") and "callout" not in ui:
                    raise ConfigError(f"message {m['id']} [{plat}]: ui needs 'callout'")
                for name in self._files(ui):
                    p = self.raw_path(plat, name)
                    if not os.path.exists(p):
                        raise ConfigError(f"message {m['id']} [{plat}]: screenshot not found: {p}")

    def _files(self, ui):
        names = {ui["screen"]}
        for role in REGION_ROLES:
            if role in ui:
                names.add(ui[role].get("file", ui["screen"]))
        for fr in ui.get("frames", []):
            names.add(fr.get("file", ui["screen"]))
        if "tiles" in ui:
            names.add(ui.get("tiles_file", ui["screen"]))
        return names

    # ---------------------------------------------------------- access
    def raw_path(self, plat, name):
        d = os.path.join(self.root, self.platforms[plat]["raw_dir"])
        for ext in ("", ".png", ".jpg", ".jpeg", ".webp"):
            p = os.path.join(d, name + ext)
            if os.path.isfile(p):
                return p
        return os.path.join(d, name + ".png")

    def screen(self, plat, name):
        """A raw screenshot, read-only. Configured privacy blurs are applied in memory only."""
        key = (plat, name)
        if key not in self._cache:
            im = Image.open(self.raw_path(plat, name)).convert("RGB")
            for box in self.platforms[plat].get("blur", {}).get(name, []):
                im.paste(im.crop(box).filter(ImageFilter.GaussianBlur(18)), tuple(box[:2]))
            self._cache[key] = im
        return self._cache[key]

    def canvas(self, plat):
        return tuple(self.platforms[plat]["canvas"])

    def device_kind(self, plat):
        return self.platforms[plat]["device"]

    def messages_for(self, plat):
        return [m for m in self.messages if plat in m.get("ui", {})]

    def ui(self, plat, m):
        """Resolve UI roles to (file, box, radius) tuples the styles consume."""
        ui = m["ui"][plat]
        out = {"screen": ui["screen"]}
        for role in REGION_ROLES:
            if role in ui:
                r = ui[role]
                out[role] = (r.get("file", ui["screen"]), r["box"], r.get("radius", 28))
        out["anchor"] = ui.get("anchor", ui["callout"]["box"] if "callout" in ui else None)
        if "lens" in ui:
            out["lens"] = ui["lens"]
        out["frames"] = [(fr.get("file", ui["screen"]), fr["box"]) for fr in ui.get("frames", [])]
        if not out["frames"] and "card" in out:
            out["frames"] = [(out["card"][0], out["card"][1])]
        if "tiles" in ui:
            tf = ui.get("tiles_file", ui["screen"])
            out["tiles"] = [(tf, b) for b in ui["tiles"]]
        out["badges"] = m.get("badges", [])
        return out

    def copy_override(self, style, m):
        return m.get("copy", {}).get(style)

    def sub(self, m):
        return m.get("sub", "")


# ------------------------------------------------------------- copy helpers
def two_lines(headline):
    """Split a headline into two lines of balanced width."""
    w = headline.split()
    if len(w) < 2:
        return [headline]
    best = min(range(1, len(w)), key=lambda i: max(len(" ".join(w[:i])), len(" ".join(w[i:]))))
    return [" ".join(w[:best]), " ".join(w[best:])]


def tag_key(line, key, tag="k"):
    """[(text, tag)] spans with the key phrase tagged."""
    if key and key.lower() in line.lower():
        i = line.lower().index(key.lower())
        spans = [(line[:i], None), (line[i:i + len(key)], tag), (line[i + len(key):], None)]
        return [s for s in spans if s[0]]
    return [(line, None)]


def spans_from_json(lines):
    """Override format: [[["TEXT","k"], ["MORE", null]], ...] or [{"spans": [...], "scale": 1.2}, ...]."""
    out = []
    for ln in lines:
        if isinstance(ln, dict):
            out.append(([(t, g) for t, g in ln["spans"]], ln.get("scale", 1.0)))
        else:
            out.append(([(t, g) for t, g in ln], 1.0))
    return out
