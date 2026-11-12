# trmnl-art

Public-domain artworks prepared for a TRMNL X e-ink screen: grayscale, 1872×1404, cropped to fill.

A TRMNL private plugin (`full.liquid`, `settings.yml`) shows one image per hour, picked from the list of names at the top of `full.liquid`. `manifest.json` records each image and its source.
To add an artwork, put a 1872×1404 grayscale JPEG in `img/`, add its name to `full.liquid` and the manifest, and upload the layout to the plugin. `prepare.py` does the crop and conversion.

All source works are in the public domain; each manifest entry links its Wikimedia Commons page.
