"""Generate the printable phongnt570 keymap layout."""

from hashlib import sha256
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


KEYMAP_DIR = Path(__file__).resolve().parent
OUTPUT = KEYMAP_DIR / "layout.pdf"
SOURCE_FILES = ("keymap.c", "config.h", "rules.mk")

PAGE_W, PAGE_H = landscape(A4)
UNIT = 43.0
GAP = 3.0
KEY_H = 37.0
X0 = 61.0
KEYBOARD_DY = -12.0

PALETTE = {
    "paper": colors.HexColor("#F4F1E9"),
    "paper_2": colors.HexColor("#E9E6DC"),
    "ink": colors.HexColor("#19343A"),
    "muted": colors.HexColor("#63767A"),
    "plate": colors.HexColor("#D5D9D5"),
    "plate_edge": colors.HexColor("#939C99"),
    "key": colors.HexColor("#174B58"),
    "key_alt": colors.HexColor("#1D5B69"),
    "key_text": colors.HexColor("#F5EEDC"),
    "yellow": colors.HexColor("#F4C542"),
    "yellow_text": colors.HexColor("#4A3B14"),
    "shadow": colors.HexColor("#102F36"),
    "inactive": colors.HexColor("#D8DEDA"),
    "inactive_text": colors.HexColor("#81908D"),
    "system": colors.HexColor("#287E9A"),
    "media": colors.HexColor("#73547D"),
    "rgb": colors.HexColor("#C6812A"),
    "nav": colors.HexColor("#397B64"),
    "danger": colors.HexColor("#B84B47"),
    "white": colors.white,
}


def source_fingerprint():
    digest = sha256()
    for filename in SOURCE_FILES:
        digest.update(filename.encode("utf-8"))
        digest.update(b"\0")
        digest.update((KEYMAP_DIR / filename).read_bytes())
    return digest.hexdigest()[:10]


def key(
    key_id,
    x,
    y,
    label,
    width=1.0,
    style="normal",
    category=None,
):
    return {
        "id": key_id,
        "x": x,
        "y": y,
        "label": label if isinstance(label, list) else [label],
        "width": width,
        "style": style,
        "category": category,
    }


TOP_Y = 474.0
ROW_Y = [417.0, 375.0, 333.0, 291.0, 249.0]


KEYS = [
    key("ESC", 0, TOP_Y, "Esc", style="yellow"),
    key("F1", 1.25, TOP_Y, "F1"),
    key("F2", 2.25, TOP_Y, "F2"),
    key("F3", 3.25, TOP_Y, "F3"),
    key("F4", 4.25, TOP_Y, "F4"),
    key("F5", 5.75, TOP_Y, "F5"),
    key("F6", 6.75, TOP_Y, "F6"),
    key("F7", 7.75, TOP_Y, "F7"),
    key("F8", 8.75, TOP_Y, "F8"),
    key("F9", 10.25, TOP_Y, "F9", style="alt"),
    key("F10", 11.25, TOP_Y, "F10", style="alt"),
    key("F11", 12.25, TOP_Y, "F11", style="alt"),
    key("F12", 13.25, TOP_Y, "F12", style="alt"),
    key("PB", 14.75, TOP_Y, "PB", style="yellow"),

    key("GRV", 0, ROW_Y[0], ["~", "`"]),
    key("1", 1, ROW_Y[0], ["!", "1"]),
    key("2", 2, ROW_Y[0], ["@", "2"]),
    key("3", 3, ROW_Y[0], ["#", "3"]),
    key("4", 4, ROW_Y[0], ["$", "4"]),
    key("5", 5, ROW_Y[0], ["%", "5"]),
    key("6", 6, ROW_Y[0], ["^", "6"]),
    key("7", 7, ROW_Y[0], ["&", "7"]),
    key("8", 8, ROW_Y[0], ["*", "8"]),
    key("9", 9, ROW_Y[0], ["(", "9"]),
    key("0", 10, ROW_Y[0], [")", "0"]),
    key("MINS", 11, ROW_Y[0], ["_", "-"]),
    key("EQL", 12, ROW_Y[0], ["+", "="]),
    key("BSPC", 13, ROW_Y[0], "Backspace", width=2.0),
    key("DEL", 15.75, ROW_Y[0], "Del"),

    key("TAB", 0, ROW_Y[1], "Tab", width=1.5),
    key("Q", 1.5, ROW_Y[1], "Q"),
    key("W", 2.5, ROW_Y[1], "W"),
    key("E", 3.5, ROW_Y[1], "E"),
    key("R", 4.5, ROW_Y[1], "R"),
    key("T", 5.5, ROW_Y[1], "T"),
    key("Y", 6.5, ROW_Y[1], "Y"),
    key("U", 7.5, ROW_Y[1], "U"),
    key("I", 8.5, ROW_Y[1], "I"),
    key("O", 9.5, ROW_Y[1], "O"),
    key("P", 10.5, ROW_Y[1], "P"),
    key("LBRC", 11.5, ROW_Y[1], ["{", "["]),
    key("RBRC", 12.5, ROW_Y[1], ["}", "]"]),
    key("BSLS", 13.5, ROW_Y[1], ["|", "\\"], width=1.5),
    key("PGUP", 15.75, ROW_Y[1], "PgUp"),

    key("CAPS", 0, ROW_Y[2], "Caps", width=1.75),
    key("A", 1.75, ROW_Y[2], "A"),
    key("S", 2.75, ROW_Y[2], "S"),
    key("D", 3.75, ROW_Y[2], "D"),
    key("F", 4.75, ROW_Y[2], "F"),
    key("G", 5.75, ROW_Y[2], "G"),
    key("H", 6.75, ROW_Y[2], "H"),
    key("J", 7.75, ROW_Y[2], "J"),
    key("K", 8.75, ROW_Y[2], "K"),
    key("L", 9.75, ROW_Y[2], "L"),
    key("SCLN", 10.75, ROW_Y[2], [":", ";"]),
    key("QUOT", 11.75, ROW_Y[2], ['"', "'"]),
    key("ENT", 12.75, ROW_Y[2], "Enter", width=2.25),
    key("PGDN", 15.75, ROW_Y[2], "PgDn"),

    key("LSFT", 0, ROW_Y[3], "Shift", width=2.25),
    key("Z", 2.25, ROW_Y[3], "Z"),
    key("X", 3.25, ROW_Y[3], "X"),
    key("C", 4.25, ROW_Y[3], "C"),
    key("V", 5.25, ROW_Y[3], "V"),
    key("B", 6.25, ROW_Y[3], "B"),
    key("N", 7.25, ROW_Y[3], "N"),
    key("M", 8.25, ROW_Y[3], "M"),
    key("COMM", 9.25, ROW_Y[3], ["<", ","]),
    key("DOT", 10.25, ROW_Y[3], [">", "."]),
    key("SLSH", 11.25, ROW_Y[3], ["?", "/"]),
    key("RSFT", 12.25, ROW_Y[3], "Shift", width=1.75),
    key("UP", 14.75, ROW_Y[3], "Up", style="yellow"),
    key("END", 15.75, ROW_Y[3], "End"),

    key("LCTL", 0, ROW_Y[4], "Ctrl", width=1.25),
    key("LOPT", 1.25, ROW_Y[4], "Opt", width=1.25),
    key("LCMD", 2.5, ROW_Y[4], "Cmd", width=1.25),
    key("SPC", 3.75, ROW_Y[4], "Space", width=6.25, style="yellow"),
    key("RCMD", 10, ROW_Y[4], "Cmd", width=1.25),
    key("ROPT", 11.25, ROW_Y[4], "Opt", width=1.25),
    key("FN", 12.5, ROW_Y[4], "Fn", width=1.25),
    key("LEFT", 13.75, ROW_Y[4], "Left", style="yellow"),
    key("DOWN", 14.75, ROW_Y[4], "Down", style="yellow"),
    key("RIGHT", 15.75, ROW_Y[4], "Right", style="yellow"),
]


FN_MAP = {
    "ESC": (["RGB", "toggle"], "rgb"),
    "F1": (["Display", "dim"], "system"),
    "F2": (["Display", "bright"], "system"),
    "F3": (["Mission", "Control"], "system"),
    "F4": (["Spotlight"], "system"),
    "F5": (["RGB", "dim"], "rgb"),
    "F6": (["RGB", "bright"], "rgb"),
    "F7": (["Previous", "track"], "media"),
    "F8": (["Play", "Pause"], "media"),
    "F9": (["Next", "track"], "media"),
    "F10": (["Mute"], "media"),
    "F11": (["Volume", "down"], "media"),
    "F12": (["Volume", "up"], "media"),
    "Q": (["RGB", "dim"], "rgb"),
    "W": (["RGB", "bright"], "rgb"),
    "A": (["RGB sat", "down"], "rgb"),
    "S": (["RGB sat", "up"], "rgb"),
    "Z": (["RGB hue", "down"], "rgb"),
    "X": (["RGB hue", "up"], "rgb"),
    "N": (["NKRO", "toggle"], "system"),
    "BSLS": (["DFU", "boot"], "danger"),
    "SPC": (["Emoji &", "Symbols"], "system"),
    "PGUP": (["RGB speed", "up"], "rgb"),
    "PGDN": (["RGB speed", "down"], "rgb"),
    "UP": (["Next RGB", "effect"], "rgb"),
    "DOWN": (["Previous", "RGB effect"], "rgb"),
    "LEFT": (["Home"], "nav"),
    "RIGHT": (["End"], "nav"),
    "FN": (["Hold", "Fn"], "yellow"),
}


def set_fill(c, color):
    c.setFillColor(color)


def draw_wrapped(c, text, x, y, max_width, font="Helvetica", size=8.4, leading=11.0, color=None):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if stringWidth(candidate, font, size) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    if color is not None:
        c.setFillColor(color)
    c.setFont(font, size)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_key(c, item, layer="base"):
    x = X0 + item["x"] * UNIT
    y = item["y"] + KEYBOARD_DY
    w = item["width"] * UNIT - GAP

    if layer == "base":
        fill = PALETTE["key"]
        text_color = PALETTE["key_text"]
        if item["style"] == "yellow":
            fill = PALETTE["yellow"]
            text_color = PALETTE["yellow_text"]
        elif item["style"] == "alt":
            fill = PALETTE["key_alt"]
        label = item["label"]
        active = True
    else:
        mapped = FN_MAP.get(item["id"])
        active = mapped is not None
        if active:
            label, category = mapped
            fill = PALETTE[category]
            text_color = PALETTE["yellow_text"] if category == "yellow" else PALETTE["white"]
        else:
            fill = PALETTE["inactive"]
            text_color = PALETTE["inactive_text"]
            label = item["label"][:1]

    c.setFillColor(PALETTE["shadow"] if active else PALETTE["plate_edge"])
    c.roundRect(x, y - 2.3, w, KEY_H, 5.0, fill=1, stroke=0)
    c.setFillColor(fill)
    c.setStrokeColor(colors.Color(1, 1, 1, alpha=0.23) if active else PALETTE["plate_edge"])
    c.setLineWidth(0.55)
    c.roundRect(x, y, w, KEY_H, 5.0, fill=1, stroke=1)

    count = len(label)
    longest = max(len(line) for line in label)
    if active and layer == "fn":
        size = 7.3 if longest > 8 else 8.0 if longest > 6 else 8.8
    else:
        size = 7.8 if longest > 8 else 9.2 if longest > 5 else 10.0
    if w > 70 and longest < 10:
        size += 0.6
    leading = size + 1.2
    total_h = (count - 1) * leading
    baseline = y + KEY_H / 2 + total_h / 2 - size * 0.34

    c.setFillColor(text_color)
    c.setFont("Helvetica-Bold" if active else "Helvetica", size)
    for idx, line in enumerate(label):
        c.drawCentredString(x + w / 2, baseline - idx * leading, line)


def draw_knob(c, layer="base"):
    cx = X0 + 16.25 * UNIT
    cy = TOP_Y + KEY_H / 2 + KEYBOARD_DY
    if layer == "base":
        ring = PALETTE["key"]
        label = ["VOL", "MUTE"]
        sub = "turn / press"
    else:
        ring = PALETTE["rgb"]
        label = ["RGB", "+ / -"]
        sub = "turn"
    c.setFillColor(PALETTE["shadow"])
    c.circle(cx, cy - 2, 19.5, fill=1, stroke=0)
    c.setFillColor(PALETTE["plate"])
    c.setStrokeColor(ring)
    c.setLineWidth(3.0)
    c.circle(cx, cy, 18.2, fill=1, stroke=1)
    c.setFillColor(PALETTE["ink"])
    c.setFont("Helvetica-Bold", 6.3)
    c.drawCentredString(cx, cy + 2, label[0])
    c.drawCentredString(cx, cy - 6, label[1])
    c.setFillColor(PALETTE["muted"])
    c.setFont("Helvetica", 5.4)
    c.drawCentredString(cx, cy - 28, sub)


def draw_keyboard(c, layer="base"):
    c.setFillColor(PALETTE["plate_edge"])
    c.roundRect(48, 231 + KEYBOARD_DY, 746, 294, 12, fill=1, stroke=0)
    c.setFillColor(PALETTE["plate"])
    c.roundRect(48, 235 + KEYBOARD_DY, 746, 294, 12, fill=1, stroke=0)
    c.setStrokeColor(colors.HexColor("#EEF0EB"))
    c.setLineWidth(0.8)
    c.roundRect(51, 238 + KEYBOARD_DY, 740, 286, 10, fill=0, stroke=1)
    for item in KEYS:
        draw_key(c, item, layer=layer)
    draw_knob(c, layer=layer)


def draw_header(c, layer_title, subtitle, page_num):
    c.setFillColor(PALETTE["paper"])
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(PALETTE["yellow"])
    c.rect(0, PAGE_H - 9, PAGE_W, 9, fill=1, stroke=0)
    c.setFillColor(PALETTE["ink"])
    c.setFont("Helvetica-Bold", 10.0)
    c.drawString(49, 566, "PHONGNT570 KEYMAP")
    c.setFont("Helvetica-Bold", 22.0)
    c.drawString(49, 539, layer_title)
    c.setFillColor(PALETTE["muted"])
    c.setFont("Helvetica", 9.0)
    c.drawString(49, 525, subtitle)
    c.setFillColor(PALETTE["ink"])
    c.setFont("Helvetica-Bold", 8.0)
    c.drawRightString(PAGE_W - 49, 547, f"LAYER {page_num} / 2")


def draw_card(c, x, y, w, h, title, lines, accent):
    c.setFillColor(colors.white)
    c.setStrokeColor(PALETTE["paper_2"])
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, 7, fill=1, stroke=1)
    c.setFillColor(accent)
    c.roundRect(x, y, 5, h, 2.5, fill=1, stroke=0)
    c.setFillColor(PALETTE["ink"])
    c.setFont("Helvetica-Bold", 9.2)
    c.drawString(x + 14, y + h - 20, title)
    cursor = y + h - 37
    for line in lines:
        cursor = draw_wrapped(
            c,
            line,
            x + 14,
            cursor,
            w - 27,
            font="Helvetica",
            size=8.0,
            leading=10.4,
            color=PALETTE["muted"],
        ) - 3.0


def draw_footer(c, page_num):
    c.setStrokeColor(PALETTE["paper_2"])
    c.setLineWidth(0.7)
    c.line(49, 30, PAGE_W - 49, 30)
    c.setFillColor(PALETTE["muted"])
    c.setFont("Helvetica", 7.3)
    c.drawString(
        49,
        18,
        f"GMMK Pro Rev 1 ANSI | phongnt570 | source {source_fingerprint()}",
    )
    c.drawRightString(PAGE_W - 49, 18, f"{page_num} / 2")


def draw_base_page(c):
    draw_header(
        c,
        "BASE LAYER - macOS",
        "Physical keycaps and flashed firmware are aligned.",
        1,
    )
    draw_keyboard(c, layer="base")
    draw_card(
        c,
        49,
        72,
        232,
        124,
        "MEDIA + KNOB",
        [
            "PB plays or pauses media.",
            "Turn the knob for system volume. Press the knob to mute.",
        ],
        PALETTE["media"],
    )
    draw_card(
        c,
        293,
        72,
        232,
        124,
        "NAVIGATION",
        [
            "Right column: Del, PgUp, PgDn, End.",
            "Hold Fn: Left = Home and Right = End.",
        ],
        PALETTE["nav"],
    )
    draw_card(
        c,
        537,
        72,
        256,
        124,
        "KEYCAP LEGENDS",
        [
            "WIN keycap = Command. ALT keycap = Option.",
            "The single bottom-right Fn key opens Layer 2.",
            "RGB sleeps after 20 minutes and wakes on input.",
        ],
        PALETTE["yellow"],
    )
    draw_footer(c, 1)
    c.showPage()


def draw_legend(c, x, y, label, color):
    c.setFillColor(color)
    c.circle(x, y + 2, 4.2, fill=1, stroke=0)
    c.setFillColor(PALETTE["muted"])
    c.setFont("Helvetica", 7.7)
    c.drawString(x + 9, y - 1, label)


def draw_fn_page(c):
    draw_header(
        c,
        "FN LAYER - hold Fn",
        "Highlighted keys change function; pale keys keep their Base action.",
        2,
    )
    draw_keyboard(c, layer="fn")

    draw_legend(c, 52, 204, "macOS / system", PALETTE["system"])
    draw_legend(c, 163, 204, "media", PALETTE["media"])
    draw_legend(c, 226, 204, "RGB", PALETTE["rgb"])
    draw_legend(c, 279, 204, "navigation", PALETTE["nav"])
    draw_legend(c, 371, 204, "bootloader", PALETTE["danger"])

    draw_card(
        c,
        49,
        64,
        232,
        121,
        "SYSTEM + MEDIA",
        [
            "F1-F4: display, Mission Control, Spotlight.",
            "F7-F12: previous, play/pause, next, mute, volume down/up.",
            "Space: Emoji & Symbols. N: toggle NKRO.",
        ],
        PALETTE["system"],
    )
    draw_card(
        c,
        293,
        64,
        232,
        121,
        "RGB CONTROLS",
        [
            "Esc toggles RGB: full or indicators-only. F5/F6 or Q/W adjust brightness.",
            "A/S saturation. Z/X hue. PgUp/PgDn speed.",
            "Up/Down changes effect. Knob adjusts brightness.",
        ],
        PALETTE["rgb"],
    )
    draw_card(
        c,
        537,
        64,
        256,
        121,
        "NAVIGATION + FLASHING",
        [
            "Left = Home. Right = End.",
            "Fn + backslash enters the STM32 DFU bootloader. Use it only when flashing firmware.",
        ],
        PALETTE["danger"],
    )
    draw_footer(c, 2)
    c.showPage()


def main():
    pdf = canvas.Canvas(
        str(OUTPUT),
        pagesize=landscape(A4),
        pageCompression=1,
        invariant=1,
    )
    pdf.setTitle("phongnt570 GMMK Pro keymap layout")
    pdf.setAuthor("Tuan Phong")
    pdf.setSubject("Base and Fn layers for the phongnt570 QMK keymap")
    pdf.setCreator("ReportLab")
    draw_base_page(pdf)
    draw_fn_page(pdf)
    pdf.save()
    print(OUTPUT)


if __name__ == "__main__":
    main()
