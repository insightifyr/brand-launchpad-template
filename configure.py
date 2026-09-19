import base64, json, mimetypes, os, re
from pathlib import Path

root = Path(__file__).resolve().parent
settings = {
    "name": os.environ.get("BRAND_NAME", "Orbit"),
    "message": os.environ.get("WELCOME_MESSAGE", "Your favorite tools and inspiration, one click away."),
    "accent": os.environ.get("ACCENT_COLOR", "#b6f46b"),
    "background": os.environ.get("BACKGROUND_COLOR", "#101b20"),
    "logo": "",
}

for key in ("accent", "background"):
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", settings[key]):
        raise ValueError(f"{key} must be a six-digit hex color, e.g. #b6f46b")

logo_path = os.environ.get("LOGO_FILE", "").strip()
if logo_path:
    path = Path(logo_path)
    if not path.is_file():
        raise FileNotFoundError(f"Uploaded logo was not found: {path}")
    mime, _ = mimetypes.guess_type(path.name)
    allowed = {"image/png", "image/jpeg", "image/webp"}
    if mime not in allowed:
        raise ValueError("Logo must be a PNG, JPEG, or WebP image")
    if path.stat().st_size > 500_000:
        raise ValueError("Logo must be 500 KB or smaller")
    settings["logo"] = "data:" + mime + ";base64," + base64.b64encode(path.read_bytes()).decode("ascii")

source = (root / "index.html").read_text()
marker = '<script type="application/json" id="defaults">'
start = source.index(marker) + len(marker)
end = source.index("</script>", start)
payload = json.dumps(settings).replace("<", "\\u003c")
public = root / "public"
public.mkdir(exist_ok=True)
(public / "index.html").write_text(source[:start] + payload + source[end:])
print("Deployment branding rendered successfully" + (" with uploaded logo" if settings["logo"] else ""))
