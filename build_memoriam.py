import json,re,html,datetime,urllib.parse
src=open('this-day-in-history.html').read()
head=src[:src.index('<main class="wrap">')]
foot=src[src.index('</main>'):]
head=re.sub(r'(og:title" content=")[^"]*','\\1In Memoriam — DirtSprintCars.com',head)
head=re.sub(r'<title>.*?</title>','<title>In Memoriam | DirtSprintCars.com</title>',head,flags=re.S)
head=head.replace('</style></head>','.mon summary{cursor:pointer;list-style:none}.mon summary::-webkit-details-marker{display:none}.mon summary h2::before{content:"\\25B8 ";color:var(--red)}.mon[open] summary h2::before{content:"\\25BE "}.ev .src2{margin-left:12px}\n</style></head>',1)
d=sorted(json.load(open('memoriam-data.json')),key=lambda e:(e['date'][5:],e['date']),reverse=True)
M=['January','February','March','April','May','June','July','August','September','October','November','December']
host=lambda u:urllib.parse.urlparse(u).netloc.replace('www.','')
e=html.escape;out=[];cur=None
for x in d:
  y,m,dd=x['date'].split('-');m=int(m)
  if m!=cur:
    if cur:out.append('</details>')
    out.append(f'<details class="mon" id="m{m:02d}" open><summary><h2 class="disp">{M[m-1]}</h2></summary>');cur=m
  s2=f' <a class="src2" href="{e(x["source2_url"])}" target="_blank" rel="noopener">{e(host(x["source2_url"]))}</a>' if x.get('source2_url') else ''
  nt=f'<p class="meta"><i>{e(x["notes"])}</i></p>' if x.get('notes') else ''
  out.append(f'<article class="day"><div class="dd disp">{M[m-1][:3]} <b>{int(dd)}</b></div><div><div class="ev"><span class="yr disp">{y}</span><span class="chip lbl">{e(x["series"])}</span><h3>{e(x["name"])}</h3><p class="meta">{e(x["track"])}</p><p>{e(x["description"])}</p>{nt}<footer class="srcfoot">Sources: <a href="{e(x["source_url"])}" target="_blank" rel="noopener">{e(host(x["source_url"]))}</a>{s2}</footer></div></div></article>')
out.append('</details>')
jump=' '.join(f'<a href="#m{m:02d}" class="lbl">{M[m-1][:3]}</a>' for m in sorted({int(x["date"][5:7]) for x in d},reverse=True))
body=f'''<main class="wrap">
<div class="chk" style="margin-top:24px"></div>
<h1 class="disp" style="font-size:48px;margin:24px 0 8px">In Memoriam</h1>
<p class="meta">Remembering drivers who lost their lives racing sprint cars and midgets. Listed by calendar day, newest first; each entry is confirmed by at least two independent sources.</p>
<div class="note"><b>DRAFT — not published.</b> Pending Kevin's approval. This list is a starting point, not a complete record. Corrections and additions welcome via Contribute.</div>
<p class="jump">{jump}</p>
{''.join(out)}
'''
open('in-memoriam.html','w').write(head+body+foot)
