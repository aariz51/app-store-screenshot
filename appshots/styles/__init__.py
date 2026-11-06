"""Style registry. Each style is an independent design language with its own layouts."""
from . import bold_blue, dark_neon, feature_led, minimal_editorial, warm_premium

STYLES = {mod.NAME: mod for mod in (warm_premium, bold_blue, feature_led, dark_neon, minimal_editorial)}
