#!/usr/bin/python3

import sys
from PIL import Image, ImageDraw, ImageFont

fontpath = "OpenTTD-Small.ttf"
size = 6
line = size + 1
background = (152, 132, 92)
background_shade = [(212, 188, 148), (104, 80, 44)]
foreground = (16, 16, 16)
shadow = (16, 16, 16)

def shadowtext(draw, scale, position, string, font, foreground, background):
    if background is not None:
        draw.text(((position[0] + 1) * scale, (position[1] + 1) * scale), string, font=font, fill=background)
    draw.text((position[0] * scale, position[1] * scale), string, font=font, fill=foreground)

scales = [1, 2, 4]
fontmodes = [{
    "mode": None,
    "description": "anti-aliased"
}, {
    "mode": "1",
    "description": "aliased"
}]

for scale in scales:
    for fontmode in fontmodes:
        image = Image.new("RGB", (270 * scale, int(9.5 * line * scale)), background_shade[1])
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, image.size[0] - scale - 1, image.size[1] - scale - 1), fill=background_shade[0], outline=None)
        draw.rectangle((0 + scale, 0 + scale, image.size[0] - scale - 1, image.size[1] - scale - 1), fill=background, outline=None)
        if fontmode["mode"] is not None:
            draw.fontmode = fontmode["mode"]
        font = ImageFont.truetype(fontpath, size * scale)
        shadowtext(draw, scale, (3, 2 + line * 0), "OpenTTD Small", font, (252, 176, 48), None)
        shadowtext(draw, scale, (3, 2 + line * 1), "A pixel art-style typeface for OᴘᴇɴTTD, inspired by Transport Tycoon Deluxe.", font, foreground, None)
        shadowtext(draw, scale, (3, 2 + line * 2), "Numerics: 0123456789 ⁰¹²³⁴ ½¾¾ 6×7=42 95%", font, foreground, None)
        shadowtext(draw, scale, (3, 2 + line * 3), "Upper case: ABCDEFGHIJKLMNOPQRSTUVWXYZ", font, foreground, None)
        shadowtext(draw, scale, (3, 2 + line * 4), "Lower case: abcdefghijklmnopqrstuvwxyz", font, foreground, None)
        shadowtext(draw, scale, (3, 2 + line * 5), "Symbols: !\"#$%@()*+,-./;<=>?[\]^_{|}~¡¤¦§©ª«¬­®", font, foreground, None)
        shadowtext(draw, scale, (3, 2 + line * 6), "Diacritics: ÀÁÂÃÄÅĀĂĄÆāàáâãäåăąæ ÇçÈèÍíÐðÑñÔôÜüÞþŊŋ", font, foreground, None)
        shadowtext(draw, scale, (3, 2 + line * 7), "Currencies: $£¥¢֏฿₠₡₢₣₤₥₦₧₨₩₪₫€₭₮₯₰₱₲₳₴₵₶₷₸₹₺₻₼₽₾₿", font, foreground, None)
        shadowtext(draw, scale, (3, 2 + line * 8), "Greek: ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ αβγδεζηθικλμνξοπρςστυφχψω", font, foreground, None)
        image.save("OpenTTD-Small-" + str(scale * size) + "px-" + fontmode["description"] + ".png", "PNG")