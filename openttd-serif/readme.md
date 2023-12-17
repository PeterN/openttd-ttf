# OpenTTD Serif
OpenTTD Serif is a light regular typeface designed for large text in a pixel art style. Drawn to broadly capture the look and feel of the newspaper pixel font in Transport Tycoon Deluxe.

The glyphs are designed with a pixel art aesthetic, heavily aligned to a pixel grid but with some flourishes for character. Pixel-perfect appearance when rendered at a height of 18 pixel (or multiples thereof).

The small ascender and descender give a compact feel. This is enhanced by the peculiarity of majuscules with diacritics being compressed to fit the diacritic mostly within the ascender space.

## Unicode coverage
OpenTTD Serif uses Unicode basic multilingual plane encoding.

Full coverage:
* Basic Latin (`U+0000..U+007F`)
* Latin-1 Supplement (`U+0080..U+00FF`)
* Latin Extended-A (`U+0100..U+017F`)
* Currency Symbols (`U+20A0..U+20CF`)

Targeted coverage:
* Greek and Coptic (`U+0384..U+03D7`) [contempary Greek only `U+0370..U+03FF`]

Partial coverage:
* IPA Extensions (`U+0250–U+02AF`)
* Combining Diacritical Marks (`U+0300–U+036F`)
These ranges provide glyphs which are combined to build the full coverage core set.

Plus a few additional glyphs - stray small caps and glyphs of particular use in OpenTTD.

## Features
OpenTTD Serif is designed with the creation of standalone bitmap strikes in mind, for example for generation of an image/sprite-based font.

## Technical details
SVG glyphs are drawn in Inkscape, for manual import into FontForge. Source SVGs, occasionally containing source paths pre-union, are included for convenience.

In FontForge, glyphs are composed from referenced copies wherever possible. Majuscule diacritics are generally placed on a "small caps" letter variant.

### Glyph units
SVGs are prepared at 1 pixel = 1 unit
* height: 2000 units
* baseline offset: 400 units
* x height: 1000 units
* ascender: 400 units
* ascent: 1500 units
* descender: 400 units
* overshoot: 10 units
The top 100 units are always empty. During TTF generation from the FontForge SFD file, height is set to 1800.

Bearings are optimised for pixel-perfect rendering:
* left bearing: 100 units, minus overshoot
* right bearing: 100 units, minus overshoot
And, kerning adjusts spacing in steps of 100 units.

Diacritics are similarly positioned in steps of 100 units.

This is designed for rendering at 18 pixel height:
* line height: 19 pixel
* baseline offset: 4 pixel
* x height: 10 pixel
* ascender: 4 pixel
* ascent: 15 pixel
* descender: 4 pixel

The recommended line height of 19 pixel is the same as the potential glyph height of 19 pixel. It is intended for diacritics to overflow out of the top of the 19 px nominal glyph height.

### Building
Run `build.sh` to build the output TTD and OTF files.

The master source file is the FontForge SFD file. SVG files are not automatically imported.