#!/usr/bin/env python3
"""Build the three gta6-meme-x-01 memes: overlay PIL-drawn make.fun ghost
+ Impact-style caption text on the generated scenes. Outputs 1024x1024 PNGs
plus 480px / 300px readability check renders."""
import math
from PIL import Image, ImageDraw, ImageFont

BASE = "/home/hatch/workspace/makefun/gta6-meme-x-01-entry/memes"
FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
MAGENTA = (230, 0, 126)
WHITE = (255, 255, 255)
BLACK = (10, 10, 12)
NAVY = (22, 41, 74)

SCENES = {
    "v1": "media-generation-scene-v1-download-0-0d75baaf-4e43-41e4-bafd-831b27bafe34.png",
    "v2": "media-generation-scene-v2-savings-0-45bf0e07-1917-4c95-aadf-e9668ad6b802.png",
    "v3": "media-generation-scene-v3-cashier-0-14e54fbd-ace0-4432-9f9c-527e86d67523.png",
}


def font(size):
    return ImageFont.truetype(FONT_BOLD, size)


def sparkle(draw, cx, cy, r, fill=BLACK):
    """4-point star sparkle."""
    pts = []
    for i in range(8):
        ang = math.pi / 2 + i * math.pi / 4
        rad = r if i % 2 == 0 else r * 0.30
        pts.append((cx + rad * math.cos(ang), cy - rad * math.sin(ang)))
    draw.polygon(pts, fill=fill)


def ghost(draw, cx, base_y, h, sleeping=False, coin=False, arm_to=None):
    """Chubby white ghost with thick black outline, sparkle eyes, small smile.
    base_y = bottom of the ghost body. arm_to = (x, y) to reach toward."""
    w = int(0.74 * h)
    x0, x1 = cx - w // 2, cx + w // 2
    dome_cy = base_y - h + w // 2
    # outline points: dome arc, right side, 3 scallops, left side
    pts = []
    for deg in range(180, -1, -6):
        a = math.radians(deg)
        pts.append((cx + (w / 2) * math.cos(a), dome_cy - (w / 2) * math.sin(a)))
    side_bottom = base_y - int(0.10 * h)
    pts.append((x1, side_bottom))
    n = 3
    seg = w / n
    for i in range(n):
        sx = x1 - i * seg
        for deg in range(0, 181, 12):
            a = math.radians(deg)
            ccx = sx - seg / 2
            pts.append((ccx + (seg / 2) * math.cos(a),
                        side_bottom + (seg / 2) * math.sin(a) * 0.9))
    pts.append((x0, dome_cy))
    draw.polygon(pts, fill=WHITE)
    draw.line(pts + [pts[0]], fill=BLACK, width=7, joint="curve")
    eye_y = base_y - int(0.66 * h)
    eye_dx = int(0.17 * w)
    eye_r = int(0.085 * h)
    if sleeping:
        for ex in (cx - eye_dx, cx + eye_dx):
            draw.arc([ex - eye_r, eye_y - eye_r // 2, ex + eye_r, eye_y + eye_r // 2],
                     200, 340, fill=BLACK, width=6)
        # Zzz
        zf = font(int(h * 0.16))
        for i, (zx, zy, s) in enumerate(((cx + w // 2 + 6, eye_y - int(h * 0.42), 1.0),
                                         (cx + w // 2 + 26, eye_y - int(h * 0.55), 0.85),
                                         (cx + w // 2 + 42, eye_y - int(h * 0.66), 0.7))):
            draw.text((zx, zy), "Z", font=font(int(h * 0.16 * s)), fill=BLACK)
    else:
        sparkle(draw, cx - eye_dx, eye_y, eye_r)
        sparkle(draw, cx + eye_dx, eye_y, eye_r)
        # small smile
        draw.arc([cx - int(0.10 * w), eye_y + int(0.10 * h),
                  cx + int(0.10 * w), eye_y + int(0.22 * h)],
                 15, 165, fill=BLACK, width=6)
    # small round hand on the ghost's right side (viewer right)
    hx, hy = x1 - 4, base_y - int(0.34 * h)
    if arm_to is not None:
        draw.line([(hx, hy), arm_to], fill=BLACK, width=24)
        draw.line([(hx, hy), arm_to], fill=WHITE, width=14)
        hx, hy = arm_to
    r = int(0.075 * h)
    draw.ellipse([hx - r, hy - r, hx + r, hy + r], fill=WHITE, outline=BLACK, width=5)
    if coin:
        cr = int(0.16 * h)
        ccx, ccy = hx + int(0.10 * h), hy - int(0.10 * h)
        draw.ellipse([ccx - cr, ccy - cr, ccx + cr, ccy + cr],
                     fill=MAGENTA, outline=BLACK, width=6)
        draw.ellipse([ccx - int(cr * 0.72), ccy - int(cr * 0.72),
                      ccx + int(cr * 0.72), ccy + int(cr * 0.72)],
                     outline=(255, 255, 255), width=3)
        sparkle(draw, ccx, ccy, int(cr * 0.55), fill=WHITE)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def caption(draw, text, y_top, size, fill=WHITE, max_w=960, stroke=8):
    fnt = font(size)
    lines = wrap(draw, text, fnt, max_w)
    y = y_top
    for ln in lines:
        w = draw.textlength(ln, font=fnt)
        draw.text(((1024 - w) / 2, y), ln, font=fnt, fill=fill,
                  stroke_width=stroke, stroke_fill=BLACK)
        y += int(size * 1.12)
    return y


def coin_stack(draw, cx, base_y, coins=3, r=26):
    for i in range(coins):
        y = base_y - i * 16
        draw.ellipse([cx - r, y - 12, cx + r, y + 12], fill=MAGENTA,
                     outline=BLACK, width=4)
        draw.ellipse([cx - int(r * 0.6), y - 7, cx + int(r * 0.6), y + 7],
                     outline=(255, 255, 255), width=2)


def build_v1():
    img = Image.open(f"{BASE}/{SCENES['v1']}").convert("RGB").resize((1024, 1024))
    d = ImageDraw.Draw(img)
    # --- redraw the TV progress bar: 2% magenta + "47 HOURS REMAINING"
    d.rectangle([318, 330, 762, 448], fill=(23, 42, 77))
    d.rounded_rectangle([340, 348, 680, 388], radius=18, fill=(10, 22, 46),
                        outline=(150, 190, 235), width=4)
    d.rounded_rectangle([344, 352, 352, 384], radius=8, fill=MAGENTA)
    f2 = font(40)
    d.text((692, 346), "2%", font=f2, fill=WHITE, stroke_width=5, stroke_fill=BLACK)
    f3 = font(36)
    t = "47 HOURS REMAINING"
    d.text(((1024 - d.textlength(t, font=f3)) / 2, 402), t, font=f3, fill=WHITE,
           stroke_width=5, stroke_fill=BLACK)
    # --- ghost napping on the sofa (right cushion), eyes closed
    ghost(d, 285, 790, 215, sleeping=True)
    # --- captions
    caption(d, "WAITED 13 YEARS FOR GTA 6.", 22, 60)
    caption(d, "NOW I WAIT 47 MORE HOURS.", 868, 62)
    caption(d, "my agent earns on make.fun while I wait", 946, 34,
            fill=MAGENTA, stroke=5)
    return img


def build_v2():
    img = Image.open(f"{BASE}/{SCENES['v2']}").convert("RGB").resize((1024, 1024))
    d = ImageDraw.Draw(img)
    # --- ghost sitting on the table at right, counting magenta coins
    coin_stack(d, 620, 868, coins=3)
    ghost(d, 745, 872, 235, coin=True)
    # --- captions (top wall is plain warm tan; bottom is dark table edge)
    caption(d, "SAVED $5 A MONTH FOR GTA 6 SINCE 2013.", 18, 58)
    caption(d, "GAME: $70. MY AGENT EARNED THE REST ON MAKE.FUN.", 872, 56)
    return img


def build_v3():
    img = Image.open(f"{BASE}/{SCENES['v3']}").convert("RGB").resize((1024, 1024))
    d = ImageDraw.Draw(img)
    # --- shop sign on the blank board
    fs = font(58)
    t = "LEONIDA GAMES"
    d.text(((1024 - d.textlength(t, font=fs)) / 2, 232), t, font=fs,
           fill=(30, 30, 40))
    # --- ghost cashier behind the counter, reaching toward the coin
    ghost(d, 470, 668, 250, arm_to=(640, 640))
    # --- captions
    caption(d, "FINALLY AT THE COUNTER.", 18, 66)
    caption(d, "THE CASHIER IS A GHOST. HE ONLY TAKES MAGENTA COINS.", 868, 56)
    return img


if __name__ == "__main__":
    for name, fn in (("v1", build_v1), ("v2", build_v2), ("v3", build_v3)):
        out = fn()
        out.save(f"{BASE}/meme-{name}.png")
        out.resize((480, 480), Image.LANCZOS).save(f"{BASE}/check-{name}-480.png")
        out.resize((300, 300), Image.LANCZOS).save(f"{BASE}/check-{name}-300.png")
        print(f"meme-{name}.png  {out.size}  saved")
