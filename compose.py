#!/usr/bin/env python3
"""Draw entry.png for make.fun news-image-20261121.

Saturday 21 November 2026: 12 stories, 6 cities, one day around the world.
Drawn from scratch with PIL in this session. Deterministic: same code,
same bytes, every run. No network, no downloaded images.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_TITLE = font("DejaVuSans-Bold.ttf", 40)
F_SUB = font("DejaVuSans-Bold.ttf", 22)
F_META = font("DejaVuSans.ttf", 15)
F_CITY = font("DejaVuSans-Bold.ttf", 20)
F_TAG = font("DejaVuSans.ttf", 13)
F_HEAD = font("DejaVuSans-Bold.ttf", 19)
F_DEK = font("DejaVuSans.ttf", 15)
F_SRC = font("DejaVuSans.ttf", 13)
F_SEC = font("DejaVuSans-Bold.ttf", 17)
F_BRIEF_B = font("DejaVuSans-Bold.ttf", 14)
F_BRIEF = font("DejaVuSans.ttf", 14)
F_CHECK = font("DejaVuSans.ttf", 13)
F_FOOT = font("DejaVuSans.ttf", 13)

NAVY = (15, 36, 64)
GOLD = (242, 201, 76)
LIGHT = (201, 212, 227)
INK = (20, 24, 32)
GRAY = (90, 98, 110)
BORDER = (213, 220, 229)
CREAM = (255, 248, 225)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to pixel width; returns list of lines."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


# ---------------- pictograms (all drawn with primitives) ----------------

def pic_rocket(d, x, y, s=64):
    # missile rising, with speed lines and a burst
    d.polygon([(x + 30, y + 4), (x + 40, y + 22), (x + 34, y + 44),
               (x + 26, y + 44), (x + 20, y + 22)], fill=(139, 30, 30))
    d.polygon([(x + 26, y + 44), (x + 34, y + 44), (x + 30, y + 58)],
              fill=(242, 140, 40))
    d.polygon([(x + 20, y + 22), (x + 12, y + 34), (x + 22, y + 30)],
              fill=(90, 90, 90))
    d.polygon([(x + 40, y + 22), (x + 48, y + 34), (x + 38, y + 30)],
              fill=(90, 90, 90))
    d.ellipse([x + 27, y + 14, x + 33, y + 20], fill=(255, 255, 255))
    for i, yy in enumerate((14, 26, 38)):
        d.line([x + 4, y + yy, x + 14, y + yy], fill=(150, 160, 170), width=3)


def pic_sun(d, x, y, s=64):
    cx, cy, r = x + 32, y + 30, 17
    for ang in range(0, 360, 45):
        import math
        a = math.radians(ang)
        d.line([cx + int(24 * math.cos(a)), cy + int(24 * math.sin(a)),
                cx + int(30 * math.cos(a)), cy + int(30 * math.sin(a))],
               fill=(242, 160, 40), width=3)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(242, 201, 76),
              outline=(200, 140, 20), width=2)
    for i, yy in enumerate((52, 58)):
        d.line([x + 8, y + yy, x + 56, y + yy], fill=(29, 107, 79), width=3)


def pic_star(d, x, y, s=64):
    cx, cy = x + 32, y + 32
    d.polygon([(cx, cy - 28), (cx + 7, cy - 7), (cx + 28, cy),
               (cx + 7, cy + 7), (cx, cy + 28), (cx - 7, cy + 7),
               (cx - 28, cy), (cx - 7, cy - 7)], fill=(31, 58, 138))
    d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(255, 255, 255))
    d.ellipse([cx - 28, cy - 28, cx + 28, cy + 28], outline=(31, 58, 138),
              width=2)


def pic_cricket(d, x, y, s=64):
    # stumps
    for sx in (14, 20, 26):
        d.rectangle([x + sx, y + 34, x + sx + 3, y + 58], fill=(120, 82, 40))
    # bat
    d.rounded_rectangle([x + 34, y + 8, x + 50, y + 48], radius=6,
                        fill=(210, 170, 110), outline=(120, 82, 40), width=2)
    d.rectangle([x + 40, y + 2, x + 44, y + 10], fill=(120, 82, 40))
    # ball
    d.ellipse([x + 48, y + 46, x + 62, y + 60], fill=(178, 34, 34),
              outline=(120, 20, 20), width=1)
    d.arc([x + 48, y + 46, x + 62, y + 60], 200, 340, fill=(255, 255, 255),
          width=1)


def pic_controller(d, x, y, s=64):
    d.rounded_rectangle([x + 4, y + 18, x + 60, y + 50], radius=12,
                        fill=(122, 46, 166))
    d.rounded_rectangle([x + 12, y + 26, x + 26, y + 40], radius=2,
                        fill=(255, 255, 255))
    d.rounded_rectangle([x + 17, y + 21, x + 21, y + 45], radius=2,
                        fill=(255, 255, 255))
    d.ellipse([x + 40, y + 26, x + 48, y + 34], fill=(242, 201, 76))
    d.ellipse([x + 50, y + 34, x + 58, y + 42], fill=(80, 200, 120))
    d.ellipse([x + 30, y + 42, x + 36, y + 48], fill=(255, 255, 255))
    d.ellipse([x + 52, y + 20, x + 58, y + 26], fill=(255, 255, 255))


def pic_train(d, x, y, s=64):
    d.rounded_rectangle([x + 10, y + 8, x + 54, y + 48], radius=8,
                        fill=(176, 106, 0))
    d.rounded_rectangle([x + 16, y + 14, x + 29, y + 28], radius=3,
                        fill=(200, 225, 240))
    d.rounded_rectangle([x + 35, y + 14, x + 48, y + 28], radius=3,
                        fill=(200, 225, 240))
    d.ellipse([x + 16, y + 36, x + 24, y + 44], fill=(255, 240, 150))
    d.ellipse([x + 40, y + 36, x + 48, y + 44], fill=(255, 240, 150))
    d.line([x + 6, y + 56, x + 58, y + 56], fill=(90, 98, 110), width=3)
    d.line([x + 14, y + 52, x + 10, y + 60], fill=(90, 98, 110), width=2)
    d.line([x + 50, y + 52, x + 54, y + 60], fill=(90, 98, 110), width=2)


# ---------------- content ----------------

CARDS = [
    dict(city="RIYADH", tag="MIDDLE EAST", color=(139, 30, 30), pic=pic_rocket,
         head="Three missiles aimed at Riyadh shot down",
         dek=("Saudi defences intercept three Houthi ballistic missiles fired "
              "at Riyadh on Saturday — the second attack on the capital in "
              "days. The Houthis threaten Saudi Red Sea ports and warn "
              "airlines away."),
         src="Reuters"),
    dict(city="ANTALYA", tag="CLIMATE", color=(29, 107, 79), pic=pic_sun,
         head="COP31 runs into overtime",
         dek=("The climate talks miss their Friday deadline. The closing "
              "plenary resumes Saturday morning with a third draft due — "
              "stripped of every fossil-fuel mention and the $120bn "
              "adaptation target."),
         src="Health Policy Watch"),
    dict(city="WARSAW", tag="EUROPE", color=(31, 58, 138), pic=pic_star,
         head="NATO chief flies to Warsaw",
         dek=("Rutte heads to Warsaw today after Russian missiles landed in "
              "Poland on Friday. Tusk calls it a deliberate provocation. "
              "Three objects came down; no one was hurt in Poland, eight "
              "were killed in Ukraine."),
         src="AP"),
    dict(city="WELLINGTON", tag="SPORT", color=(14, 107, 107), pic=pic_cricket,
         head="Rahul's century puts India on top",
         dek=("KL Rahul's 119 not out carries India to 326 for 2 on day "
              "three, trailing by 42. New Zealand made 368, built on "
              "Nicholls' 175 not out and Phillips' 118."),
         src="IANS / AP"),
    dict(city="VICE CITY", tag="CULTURE", color=(122, 46, 166),
         pic=pic_controller,
         head="GTA VI passes $3 billion",
         dek=("An estimated 31.4 million digital copies sold by Saturday, "
              "tracker figures show. Take-Two's official day-one figure: "
              "$3.79 billion — the biggest entertainment launch ever."),
         src="AppGazer / Take-Two"),
    dict(city="ROME", tag="EUROPE", color=(176, 106, 0), pic=pic_train,
         head="Italy's rail strike runs into Saturday",
         dek=("A rail strike runs until 20:00 tonight after Friday's CGIL "
              "general strike, which the union says drew over a million "
              "people in 100-plus cities. Students clashed with police in "
              "Rome."),
         src="Reuters"),
]

BRIEFS = [
    ("COP31 — Vanuatu:", "Regenvanu warns: phase out fossil fuels or Pacific islands won't survive. (RNZ Pacific)"),
    ("COP31 — RSF:", "Protect environmental journalism to fight the climate crisis. (Evening Report)"),
    ("Botswana:", "President Boko urges Africans to trade more with each other. (Pfumojena)"),
    ("Las Vegas GP:", "Qualifying at 04:00 UTC; the race runs tonight, 20:00 PST. (F1)"),
    ("After Akvan:", "Odisha counts the cost a day after landfall: 300,000 evacuated, 209 mm of rain, no deaths. (IMD)"),
    ("Storm Xavier:", "Atlantic gale warnings narrow as the storm passes. (AppiSToS)"),
]


def main():
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 104], fill=NAVY)
    d.rectangle([0, 104, W, 108], fill=GOLD)
    t = "SATURDAY 21 NOVEMBER 2026"
    d.text(((W - d.textlength(t, font=F_TITLE)) / 2, 12), t, font=F_TITLE,
           fill=(255, 255, 255))
    t = "THE WORLD IN SIX CITIES"
    d.text(((W - d.textlength(t, font=F_SUB)) / 2, 56), t, font=F_SUB,
           fill=GOLD)
    t = "12 stories  ·  as reported by 03:00 UTC  ·  drawn in code"
    d.text(((W - d.textlength(t, font=F_META)) / 2, 84), t, font=F_META,
           fill=LIGHT)

    # ---- city cards: 2 rows x 3 ----
    cw, ch, gap = 320, 330, 12
    x0, y0 = 16, 116
    for i, c in enumerate(CARDS):
        cx = x0 + (i % 3) * (cw + gap)
        cy = y0 + (i // 3) * (ch + gap)
        d.rectangle([cx, cy, cx + cw, cy + ch], fill=(255, 255, 255),
                    outline=BORDER, width=1)
        d.rectangle([cx, cy, cx + cw, cy + 36], fill=c["color"])
        d.text((cx + 12, cy + 7), c["city"], font=F_CITY, fill=(255, 255, 255))
        tag = c["tag"]
        d.text((cx + cw - 12 - d.textlength(tag, font=F_TAG), cy + 11),
               tag, font=F_TAG, fill=(230, 230, 230))
        # pictogram + headline
        c["pic"](d, cx + 12, cy + 48)
        head_lines = wrap(d, c["head"], F_HEAD, cw - 96)
        yy = draw_lines(d, head_lines, cx + 88, cy + 50, F_HEAD, INK, 23)
        # dek
        dek_lines = wrap(d, c["dek"], F_DEK, cw - 28)
        draw_lines(d, dek_lines, cx + 14, cy + 128, F_DEK, (40, 46, 56), 19)
        # source
        src = "Source: " + c["src"]
        d.text((cx + 14, cy + ch - 26), src, font=F_SRC, fill=GRAY)

    # ---- briefs strip ----
    by = 796
    d.text((16, by), "THE REST OF THE DAY — IN BRIEF", font=F_SEC, fill=NAVY)
    d.line([16, by + 26, W - 16, by + 26], fill=BORDER, width=1)
    for i, (lead, rest) in enumerate(BRIEFS):
        bx = 16 + (i % 2) * 512
        byy = by + 34 + (i // 2) * 34
        d.text((bx, byy), "•  ", font=F_BRIEF_B, fill=NAVY)
        full = lead + " " + rest
        lines = wrap(d, full, F_BRIEF_B, 450)
        yy = byy
        for j, line in enumerate(lines[:2]):
            fnt = F_BRIEF_B if j == 0 else F_BRIEF
            d.text((bx + 14, yy), line, font=fnt, fill=INK)
            yy += 17

    # ---- date check strip ----
    cy0 = 934
    d.rectangle([16, cy0, W - 16, cy0 + 34], fill=CREAM, outline=(220, 200, 140))
    l1 = "DATE CHECK — NOT TODAY'S NEWS, LEFT OUT ON PURPOSE:"
    l2 = ("Russian missiles in Poland  ·  Akvan's landfall  ·  Zecler verdict  ·  "
          "Gupta sentence  ·  Denmark plot  ·  AI-chip disclosure — all Friday (or earlier).")
    d.text(((W - d.textlength(l1, font=F_CHECK)) / 2, cy0 + 3), l1,
           font=F_CHECK, fill=(90, 70, 10))
    d.text(((W - d.textlength(l2, font=F_CHECK)) / 2, cy0 + 19), l2,
           font=F_CHECK, fill=(90, 70, 10))

    # ---- footer ----
    fy = 976
    t = "Still to come today: COP31's third draft this morning  ·  the Las Vegas Grand Prix tonight  ·  India bat on in Wellington"
    d.text(((W - d.textlength(t, font=F_FOOT)) / 2, fy), t, font=F_FOOT,
           fill=INK)
    t = "Sources: Reuters  ·  AP  ·  Health Policy Watch  ·  Asia Today  ·  IANS  ·  AppGazer  ·  RNZ Pacific  ·  F1  ·  IMD"
    d.text(((W - d.textlength(t, font=F_FOOT)) / 2, fy + 20), t, font=F_FOOT,
           fill=GRAY)

    out = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out, exist_ok=True)
    img.save(os.path.join(out, "entry.png"))


if __name__ == "__main__":
    main()
