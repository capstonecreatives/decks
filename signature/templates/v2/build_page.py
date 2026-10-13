import sys, html
SLUG, NAME, TITLE, WA = sys.argv[1:5]
ABS='https://ranielponesto.github.io/decks/signature/'
SH=ABS+'images/slices/'; PP=ABS+f'people/{SLUG}/'; IM=ABS+'images/'
L={'web':'https://capstoneproperty.com/','map':'https://maps.app.goo.gl/vUx1QU2z1e2iej6c6','wa':f'https://wa.me/974{WA}',
   'ig':'https://www.instagram.com/capstone.property/','li':'https://www.linkedin.com/company/capstone-property',
   'fb':'https://www.facebook.com/CapstonePropertyQatar/','x':'https://x.com/CapstoneQa'}
TD='style="padding:0;margin:0;line-height:0;font-size:0;mso-line-height-rule:exactly;"'
TB='cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;"'
def img(src,w,h,alt): return f'<img src="{src}" width="{w}" height="{h}" alt="{html.escape(alt)}" border="0" style="display:block;border:0;outline:none;width:{w}px;height:{h}px;">'
def a(href,inner): return f'<a href="{href}" target="_blank" style="text-decoration:none;display:block;">{inner}</a>'
num='+974 '+WA[:4]+' '+WA[4:]
def fimg(src,w,alt):
    return f'<img src="{src}" width="{w}" alt="{html.escape(alt)}" border="0" style="display:block;border:0;outline:none;width:100%;max-width:{w}px;height:auto;">'
def cell(pct,inner,extra='',bg=True):
    bgs=' bgcolor="#003850"' if bg else ''
    bgc='background-color:#003850;' if bg else ''
    return f'<td width="{pct}%" valign="top"{bgs} style="{bgc}width:{pct}%;padding:0;margin:0;line-height:0;font-size:0;mso-line-height-rule:exactly;{extra}">{inner}</td>'
FT='cellpadding="0" cellspacing="0" border="0" role="presentation" width="100%" style="border-collapse:collapse;width:100%;mso-table-lspace:0;mso-table-rspace:0;"'
alt=NAME+" | "+TITLE+" | Capstone Property | WhatsApp "+num+" | Marina Way 27, Porto Arabia, The Pearl, Qatar | capstoneproperty.com"
sig=(f'<a href="{L["web"]}" target="_blank" style="text-decoration:none;display:block;max-width:420px;">'
     f'<img src="{PP}card-202610131150.gif" width="420" alt="{html.escape(alt)}" border="0" '
     f'style="display:block;border:0;outline:none;width:420px;max-width:100%;height:auto;"></a>')
page=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>{html.escape(NAME)} — Email Signature</title>
<style>
:root{{--navy:#003850;--teal:#45828C;--line:#E3E6EB;--muted:#6B7480;--bg:#F7F8FA}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:"Segoe UI",Tahoma,Arial,sans-serif;background:var(--bg);color:#212721;line-height:1.5}}
.wrap{{max-width:760px;margin:0 auto;padding:32px 20px 60px}}
a.back{{font-size:14px;font-weight:600;color:var(--navy);text-decoration:none}}
h1{{font-size:30px;color:var(--navy);margin:14px 0 6px}}
p.lead{{color:var(--muted);margin-bottom:24px}}
.box{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:28px;overflow-x:auto;margin-bottom:18px}}
.box.dark{{background:#1F1F1F;border-color:#1F1F1F}}
.btns{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:22px}}
button{{font:inherit;font-size:14px;font-weight:700;border-radius:10px;padding:12px 18px;cursor:pointer;border:1px solid var(--navy);background:#fff;color:var(--navy)}}
button.primary{{background:var(--navy);color:#fff}}
ol{{padding-left:20px;font-size:14px}} li{{margin:6px 0}}
.note{{font-size:13px;color:var(--muted);border-left:3px solid var(--teal);padding-left:12px;margin-top:16px}}
.toast{{position:fixed;left:50%;bottom:28px;transform:translateX(-50%);background:var(--navy);color:#fff;padding:12px 20px;border-radius:999px;font-weight:600;font-size:14px;opacity:0;transition:opacity .25s}}
.toast.show{{opacity:1}}
</style></head><body><div class="wrap">
<a class="back" href="../../">← Signature tool</a>
<h1>{html.escape(NAME)}</h1>
<p class="lead">Image signature: looks identical in every email app, light or dark mode, on phone and desktop.</p>
<div class="btns"><button class="primary" id="copy">Copy signature</button><button id="mode">Show on dark inbox</button></div>
<div class="box" id="box"><div id="sig">{sig}</div></div>
<div class="box"><ol>
<li>Click <b>Copy signature</b>.</li>
<li>Outlook: <b>Settings → Accounts → Signatures</b> (Classic Outlook: File → Options → Mail → Signatures).</li>
<li>Delete the old signature completely, paste (<b>Ctrl+V</b> / <b>Cmd+V</b>), and save.</li>
<li>Send a test email from your <b>computer</b> to yourself and check it on your phone.</li></ol>\n<p class="note"><b>Sending from the Outlook iPhone app?</b> It uses its own separate signature (Outlook app → Settings → your account → Signature), which can't hold images. Emails sent from the phone will show that one instead.</p>
<p class="note">Every part of the card is an image, so email apps can't change its colours, font or layout. The whole card is a single picture, so no email app can split, shift or recolour it. Tapping it opens capstoneproperty.com.</p></div>
</div><div class="toast" id="toast"></div>
<script>
(function(){{
 var sig=document.getElementById('sig'),t=document.getElementById('toast');
 function toast(m){{t.textContent=m;t.classList.add('show');setTimeout(function(){{t.classList.remove('show')}},2200)}}
 function fallback(){{var r=document.createRange();r.selectNodeContents(sig);var s=getSelection();s.removeAllRanges();s.addRange(r);var ok=false;try{{ok=document.execCommand('copy')}}catch(e){{}}s.removeAllRanges();return ok}}
 document.getElementById('copy').onclick=function(){{
  var h=sig.innerHTML;
  if(window.ClipboardItem&&navigator.clipboard&&navigator.clipboard.write){{
   navigator.clipboard.write([new ClipboardItem({{'text/html':new Blob([h],{{type:'text/html'}}),'text/plain':new Blob(['{html.escape(NAME)}'],{{type:'text/plain'}})}})]).then(function(){{toast('Signature copied. Paste it into Outlook.')}},function(){{toast(fallback()?'Signature copied. Paste it into Outlook.':'Copy failed — select the card and copy it.')}});
  }} else toast(fallback()?'Signature copied. Paste it into Outlook.':'Copy failed — select the card and copy it.');
 }};
 var dark=false;document.getElementById('mode').onclick=function(){{dark=!dark;document.getElementById('box').classList.toggle('dark',dark);this.textContent=dark?'Show on light inbox':'Show on dark inbox'}};
}})();
</script></body></html>'''
open(f'../../people/{SLUG}/index.html','w').write(page)
print(len(sig))
