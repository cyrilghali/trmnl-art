# trmnl-art

Public-domain artworks prepared for a TRMNL X e-ink screen: grayscale, 1872×1404, cropped to fill.

A TRMNL private plugin (`full.liquid`, `settings.yml`) shows one image per hour, picked from the list of names at the top of `full.liquid`. `manifest.json` records each image and its source.
Captions are in French. Portrait works keep their own shape and show a short note beside them; the others fill the screen with a caption bar.
To add an artwork, put a grayscale JPEG in `img/` (1872×1404, or 1404 tall for a portrait), add its name, French caption and optional note to `captions.py` and its source to the manifest, run `python3 build_layout.py`, and upload `full.liquid` to the plugin. `prepare2.py` does the crop and conversion.

All source works are in the public domain; each manifest entry links its Wikimedia Commons page.
