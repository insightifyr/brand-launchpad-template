import json, os, re
from pathlib import Path
from urllib.parse import urlparse
root=Path(__file__).resolve().parent
settings={k:os.environ.get(env,default) for k,env,default in [('name','BRAND_NAME','Orbit'),('message','WELCOME_MESSAGE','Your favorite tools and inspiration, one click away.'),('accent','ACCENT_COLOR','#b6f46b'),('background','BACKGROUND_COLOR','#101b20'),('logo','LOGO_URL','')]}
for key in ['accent','background']:
 if not re.fullmatch(r'#[0-9a-fA-F]{6}',settings[key]): raise ValueError(key+' must be a six-digit hex color, e.g. #b6f46b')
if settings['logo'] and (urlparse(settings['logo']).scheme!='https' or not urlparse(settings['logo']).netloc): raise ValueError('Logo URL must be a public HTTPS image URL')
source=(root/'index.html').read_text()
marker='<script type="application/json" id="defaults">'
start=source.index(marker)+len(marker)
end=source.index('</script>',start)
payload=json.dumps(settings).replace('<','\\u003c')
public=root/'public'
public.mkdir(exist_ok=True)
(public/'index.html').write_text(source[:start]+payload+source[end:])
print('Deployment branding rendered successfully')
