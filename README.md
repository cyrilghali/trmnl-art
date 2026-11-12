# trmnl-art

Public-domain artworks prepared for a TRMNL X e-ink screen: grayscale, 1872×1404, cropped to fill.

`manifest.json` lists the images. A TRMNL private plugin polls it and shows one image per hour.
To add an artwork, put a 1872×1404 grayscale JPEG in `img/` and add it to the manifest. `prepare.py` does the crop and conversion.

All source works are in the public domain; each manifest entry links its Wikimedia Commons page.
