import json,html,re
E=html.escape
src=open('this-day-in-history.html').read()
d=json.load(open('legends-data.json'))
head=src[:src.index('</style></head><body>')]
head=re.sub(r'<title>.*?</title>','<title>Sprint Car &amp; Midget Racing Legends: World of Outlaws, USAC, High Limit &amp; More | DirtSprintCars.com</title>',head,1,re.S)
head=re.sub(r'<meta name="description"[^>]*>','<meta name="description" content="Career profiles of sprint car and midget racing legends, including Steve Kinser, Donny Schatz, Tony Stewart and Kody Swanson. Championships, record win totals and crown-jewel victories across World of Outlaws, High Limit, USAC Sprint, Midget and Silver Crown, ASCS, USCS, NARC and NCRA.">',head,1)
head=re.sub(r'<meta property="og:title"[^>]*>','<meta property="og:title" content="Sprint Car &amp; Midget Racing Legends | DirtSprintCars.com"><meta property="og:description" content="Career profiles of sprint car and midget racing legends, including Steve Kinser, Donny Schatz, Tony Stewart and Kody Swanson. Championships, record win totals and crown-jewel victories across World of Outlaws, High Limit, USAC Sprint, Midget and Silver Crown, ASCS, USCS, NARC and NCRA."><meta property="og:type" content="article">',head,1)
css=""".lhero{padding:40px 0 8px}.lhero h1{font-size:clamp(44px,7vw,84px);margin:0;color:#fff}.lhero p{font-size:20px;color:var(--mute);max-width:60ch}
.ser{margin-top:36px}.ser>summary{cursor:pointer;list-style:none}.ser>summary::-webkit-details-marker{display:none}.ser>summary h2{font-size:36px;margin:0 0 10px;border-bottom:3px solid var(--red);padding-bottom:6px}.ser>summary h2:before{content:"+ ";color:var(--red)}.ser[open]>summary h2:before{content:"\\2212  "}
.intro{font-size:18px;line-height:1.6;color:var(--mute);max-width:75ch}.top5{background:var(--panel);border-top:3px solid var(--red);padding:16px 20px;margin:18px 0;max-width:520px}.top5 ol{margin:8px 0 0;padding-left:22px}.top5 li{padding:3px 0}.top5 b{float:right;color:var(--fg)}
.leg{border-bottom:1px solid var(--line);padding:18px 0}.leg h3{font-size:28px;margin:0 0 6px}.nick{color:var(--dirt);font-size:16px;margin-left:8px}.leg p{line-height:1.6;color:var(--fg);max-width:75ch}.ach{color:var(--mute);margin:8px 0 0 18px}.more{background:none;border:0;padding:4px 0;color:var(--red);cursor:pointer;font:inherit;font-weight:700;text-transform:uppercase;letter-spacing:.06em;font-size:13px}.more:hover{color:var(--red-hi)}.full[hidden],.snip[hidden]{display:none}.stats{font-size:14px;font-weight:700;color:var(--dirt);margin:6px 0 2px;letter-spacing:.02em}.tnote{font-size:13px;color:var(--dim);margin-top:8px}
.srcfoot{display:block;margin-top:10px;padding-top:6px;border-top:1px solid var(--line);font-size:12px;color:var(--dim)}.srcfoot a{color:var(--dim);margin-right:10px}.srcfoot a:hover{color:var(--red-hi)}
"""
ABBR=('Jr.','Sr.','St.','Mt.','Dr.','Aug.','Oct.','Sept.','Nov.','Dec.','Jan.','Feb.','Ind.','J.J.','A.J.','C.J.','U.S.')
def sents(p):
  out,cur=[],''
  for w in p.split(' '):
    cur=(cur+' '+w).strip()
    if re.search(r'[.!?]"?$',w) and not w.endswith(ABBR) and not re.fullmatch(r'[A-Z]\.',w): out.append(cur);cur=''
  if cur: out.append(cur)
  return out
def snippet(g):
  if g.get('snippet'): return g['snippet']
  ss=[x for p in g.get('synopsis',[]) for x in sents(p)]
  n=3 if sum(len(x) for x in ss[:3])<=420 else 2
  return ' '.join(ss[:n])
def host(u): return re.sub(r'^https?://(www\.)?','',u).split('/')[0]
def srcs(l):
  l=[u for u in (l or []) if u]
  return '' if not l else '<footer class="srcfoot">Sources: '+''.join(f'<a href="{E(u)}" target="_blank" rel="noopener">{E(host(u))}</a>' for u in l)+'</footer>'
out=[]
for s in d['series']:
  b=[f'<section class="ser-wrap" aria-labelledby="h-{s["id"]}"><details class="ser" id="{s["id"]}" open><summary><h2 class="disp" id="h-{s["id"]}">{E(s["name"])}</h2></summary>']
  if s.get('intro'): b.append(f'<p class="intro">{E(s["intro"])}</p>')
  if s.get('top5'):
    b.append('<aside class="top5" aria-label="All-time feature wins, top five"><span class="lbl">All-time feature wins: top five</span><ol>'+''.join(f'<li>{E(n)} <b>{E(str(w))}</b></li>' for n,w in s['top5'])+'</ol>')
    if s.get('top5_note'): b.append(f'<p class="tnote">{E(s["top5_note"])}</p>')
    b.append(srcs(s.get('top5_sources'))+'</aside>')
  for g in s.get('legends',[]):
    fid=f'bio-{s["id"]}-'+re.sub(r'[^a-z0-9]+','-',g['name'].lower()).strip('-')
    x=[f'<article class="leg" aria-labelledby="{fid}-h"><h3 class="disp" id="{fid}-h">{E(g["name"])}'+(f'<span class="nick">"{E(g["nickname"])}"</span>' if g.get('nickname') else '')+'</h3>']
    x.append(f'<p class="snip">{E(snippet(g))}</p><div class="full" id="{fid}" hidden>'+''.join(f'<p>{E(p)}</p>' for p in g.get('synopsis',[]) if p))
    if g.get('achievements'): x.append('<span class="lbl">Notable achievements</span><ul class="ach">'+''.join(f'<li>{E(a)}</li>' for a in g['achievements'])+'</ul>')
    x.append('</div>'+(f'<p class="stats">'+' <span aria-hidden="true">&middot;</span> '.join(E(t) for t in g['stats'])+'</p>' if g.get('stats') else '')+f'<button type="button" class="more" aria-expanded="false" aria-controls="{fid}">Read more</button>')
    x.append(srcs(g.get('sources'))+'</article>'); b+=x
  out.append(''.join(b)+'</details></section>')
hdr=src[src.index('<header>'):src.index('</header>')+9]
hdr=hdr.replace('<li><a href="legends.html" class="lbl">Legends</a></li>','<li><a href="legends.html" class="lbl" aria-current="page">Legends</a></li>')
ftr=src[src.index('<footer>'):src.index('</footer>')+9]
jump='<nav class="jump" aria-label="Series">'+''.join(f'<a href="#{s["id"]}" class="lbl">{E(s["name"])}</a>' for s in d['series'])+'</nav>'
js="<script>function oh(){var e=document.getElementById(location.hash.slice(1));if(e&&e.tagName=='DETAILS')e.open=true}window.addEventListener('hashchange',oh);oh();document.addEventListener('click',function(ev){var b=ev.target.closest('.more');if(!b)return;var f=document.getElementById(b.getAttribute('aria-controls')),o=b.getAttribute('aria-expanded')=='true';f.hidden=o;f.parentNode.querySelector('.snip').hidden=!o;b.setAttribute('aria-expanded',String(!o));b.textContent=o?'Read more':'Show less';if(o)f.parentNode.scrollIntoView({block:'nearest'})});</script>"
page=head+'</style><style>'+css+'</style></head><body>\n'+hdr+'\n<main class="wrap">\n<header class="lhero"><span class="lbl tag">Guide</span><h1 class="disp">Legends</h1><p>The drivers and moments that built sprint car and midget racing.</p></header>\n'+jump+'\n'+'\n'.join(out)+'\n</main>\n'+js+'\n'+ftr+'\n</body></html>\n'
open('legends.html','w').write(page)
