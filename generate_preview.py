from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
LOGO = ROOT / "pkd-bachok-26.jpg"
OUTPUT = ROOT / "og-preview.jpg"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

canvas = Image.new("RGB", (1200, 630), "white")
logo = Image.open(LOGO).convert("RGB")
logo.thumbnail((620, 560), Image.Resampling.LANCZOS)

logo_x = 25 + (600 - logo.width) // 2
logo_y = (630 - logo.height) // 2
canvas.paste(logo, (logo_x, logo_y))

draw = ImageDraw.Draw(canvas)

green = (11, 92, 50)
orange = (236, 92, 8)
light_green = (237, 246, 240)

font_title = ImageFont.truetype(FONT, 38)
font_event = ImageFont.truetype(FONT, 31)
font_region = ImageFont.truetype(FONT, 24)
font_label = ImageFont.truetype(FONT, 28)

panel_x1, panel_y1, panel_x2, panel_y2 = 650, 42, 1170, 588
draw.rounded_rectangle((panel_x1, panel_y1, panel_x2, panel_y2), radius=28, fill=light_green)
draw.rounded_rectangle((panel_x1, panel_y1, panel_x2, 58), radius=8, fill=orange)

x = 690
y = 100

# Cleaner spacing and alignment for WhatsApp preview.
lines = [
    ("JELAJAH LARIAN OBOR", font_title, green, 16),
    ("KESIHATAN MENTAL", font_title, green, 18),

    ("& SAMBUTAN HARI", font_event, orange, 6),
    ("PENCEGAHAN BUNUH DIRI", font_event, orange, 18),

    ("PERINGKAT NEGERI", font_region, green, 4),
    ("KELANTAN 2026", font_region, green, 18),
]

for text, font, colour, spacing in lines:
    draw.text((x, y), text, font=font, fill=colour)
    bbox = draw.textbbox((x, y), text, font=font)
    y = bbox[3] + spacing

line_y = y + 2
draw.line((690, line_y, 1125, line_y), fill=orange, width=5)

y = line_y + 34
draw.text((x, y), "LAMAN RASMI PROGRAM", font=font_label, fill=green)

canvas.save(OUTPUT, "JPEG", quality=88, optimize=True, progressive=True)
print(f"Created: {OUTPUT}")
