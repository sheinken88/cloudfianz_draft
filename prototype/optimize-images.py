"""Re-encode large rendered raster images without changing their content.

Optional maintenance command: python3 prototype/optimize-images.py (Pillow).
Variants and manifest are committed; normal builds need only Python's stdlib.
Run after a preview build when original images change. Logos stay untouched.
"""
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'


class Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            self.paths.add(dict(attrs).get('src', ''))


images = Images()
for page in (DIST / 'es').rglob('*.html'):
    images.feed(page.read_text())
manifest_path = ROOT / 'image-variants.json'
previous = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
paths = images.paths | set(previous)
manifest = {}
for src in sorted(paths):
    path = DIST / src.lstrip('/')
    if not src.startswith('/assets/') or '/brand/' in src or '/optimized/' in src:
        continue
    if path.suffix.lower() not in ('.jpg', '.jpeg', '.png') or not path.is_file() or path.stat().st_size < 65000:
        continue
    with Image.open(path) as original:
        original = ImageOps.exif_transpose(original).convert('RGB')
        width, height = original.size
        variants = []
        for size in sorted({min(w, width) for w in (640, 960, 1280, width)}):
            output = DIST / 'assets/optimized' / f'{path.stem}-{size}.webp'
            output.parent.mkdir(exist_ok=True)
            resized = original.resize((size, round(height * size / width)), Image.Resampling.LANCZOS)
            resized.save(output, 'WEBP', quality=86, method=6)
            variants.append({'src': '/' + str(output.relative_to(DIST)), 'width': size})
        manifest[src] = {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'width': width,
                         'height': height, 'variants': variants}
        print(f'{path.name}: {path.stat().st_size // 1024} KiB → {output.stat().st_size // 1024} KiB (full size), {len(variants)} variants')
manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
