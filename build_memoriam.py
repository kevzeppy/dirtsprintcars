import json,re,html,datetime,urllib.parse
src=open('this-day-in-history.html').read()
head=src[:src.index('<main class="wrap">')]
foot=src[src.index('</main>'):]
head=re.sub(r'(og:title" content=")[^"]*','\\1In Memoriam — DirtSprintCars.com',head)
head=re.sub(r'<title>.*?</title>','<title>In Memoriam | DirtSprintCars.com</title>',head,flags=re.S)
head=head.replace('</style></head>','.mon summary{cursor:pointer;list-style:none}.mon summary::-webkit-details-marker{display:none}.mon summary h2::before{content:"\\25B8 ";color:var(--red)}.mon[open] summary h2::before{content:"\\25BE "}.ev .src2{margin-left:12px}\n</style></head>',1)
d=sorted(json.load(open('memoriam-data.json')),key=lambda e:e['date'])
M=['January','February','March','April','May','June','July','August','September','October','November','December']
host=lambda u:urllib.parse.urlparse(u).netloc.replace('www.','')
e=html.escape;out=[];cur=None
for x in d:
  y,m,dd=x['date'].split('-');m=int(m)
  if y!=cur:
    if cur:out.append('</details>')
    out.append(f'<details class="mon" id="y{y}" open><summary><h2 class="disp">{y}</h2></summary>');cur=y
  lk=' '.join(f'<a href="{e(u)}" target="_blank" rel="noopener">{"Wikipedia" if "wikipedia.org" in u else e(host(u))}</a>' for u in x['sources'])
  body=''.join(f'<p>{e(p)}</p>' for p in x['career'])
  out.append(f'<article class="day"><div class="dd disp">{M[m-1][:3]} <b>{int(dd)}</b></div><div><div class="ev"><span class="yr disp">{y}</span><span class="chip lbl">{e(x["series"])}</span><h3>{e(x["name"])}</h3>{body}<p class="meta rip" style="font-style:italic;opacity:.8">{e(x["death_note"])}</p><footer class="srcfoot">Sources: {lk}</footer></div></div></article>')
out.append('</details>')
jump=' '.join(f'<a href="#y{y}" class="lbl">{y}</a>' for y in sorted({x["date"][:4] for x in d}))
body=f'''<main class="wrap">
<h1 class="disp" style="font-size:48px;margin:24px 0 8px">In Memoriam</h1>
<p class="meta">Remembering drivers who lost their lives racing sprint cars and midgets. Listed in order of date of death, oldest first; each entry is confirmed by at least two independent sources.</p>
<div class="note">This list is a starting point, not a complete record. Corrections and additions welcome via Contribute.</div>
<p class="jump">{jump}</p>
{''.join(out)}
'''
open('in-memoriam.html','w').write(head+body+foot)
