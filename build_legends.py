import json,html,re
E=html.escape
src=open('this-day-in-history.html').read()
d=json.load(open('legends-data.json'))
head=src[:src.index('</style></head><body>')]+open('legends-compact.css').read()
head=re.sub(r'<title>.*?</title>','<title>Sprint Car &amp; Midget Racing Legends: World of Outlaws, USAC, High Limit &amp; More | DirtSprintCars.com</title>',head,1,re.S)
head=re.sub(r'<meta name="description"[^>]*>','<meta name="description" content="Career profiles of sprint car and midget racing legends, including Steve Kinser, Donny Schatz, Tony Stewart and Kody Swanson. Championships, record win totals and crown-jewel victories across World of Outlaws, High Limit, All Stars, USAC Sprint, Midget and Silver Crown, ASCS, USCS, NARC and NCRA.">',head,1)
head=re.sub(r'<meta property="og:title"[^>]*>','<meta property="og:title" content="Sprint Car &amp; Midget Racing Legends | DirtSprintCars.com"><meta property="og:description" content="Career profiles of sprint car and midget racing legends, including Steve Kinser, Donny Schatz, Tony Stewart and Kody Swanson. Championships, record win totals and crown-jewel victories across World of Outlaws, High Limit, All Stars, USAC Sprint, Midget and Silver Crown, ASCS, USCS, NARC and NCRA."><meta property="og:type" content="article">',head,1)
css=""".lhero{padding:40px 0 8px}
.lhimg{display:block;width:100%;height:clamp(220px,36vw,440px);object-fit:cover;object-position:50% 42%;margin-bottom:24px}.lhero h1{font-size:clamp(44px,7vw,84px);margin:0;color:#fff}.lhero p{font-size:20px;color:var(--mute);max-width:60ch}
.ser{margin-top:36px}.ser>summary{cursor:pointer;list-style:none}.ser>summary::-webkit-details-marker{display:none}.ser>summary h2{font-size:36px;margin:0 0 10px;border-bottom:3px solid var(--red);padding-bottom:6px}.ser>summary h2:before{content:"+ ";color:var(--red)}.ser[open]>summary h2:before{content:"\\2212  "}
.intro{font-size:18px;line-height:1.6;color:var(--mute);max-width:75ch}.top5{background:var(--panel);border-top:3px solid var(--red);padding:16px 20px;margin:18px 0;max-width:520px}.top5 ol{margin:8px 0 0;padding-left:22px}.top5 li{padding:3px 0}.top5 b{float:right;color:var(--fg)}
.leg{border-bottom:1px solid var(--line);padding:18px 0}.leg h3{font-size:28px;margin:0 0 6px}.nick{color:var(--dirt);font-size:16px;margin-left:8px}.leg p{line-height:1.6;color:var(--fg);max-width:75ch}.ach{color:var(--mute);margin:8px 0 0 18px}.more{background:none;border:0;padding:4px 0;color:var(--red);cursor:pointer;font:inherit;font-weight:700;text-transform:uppercase;letter-spacing:.06em;font-size:13px}.more:hover{color:var(--red-hi)}.full[hidden],.snip[hidden]{display:none}.stats{font-size:14px;font-weight:700;color:var(--dirt);margin:6px 0 2px;letter-spacing:.02em}.tnote{font-size:13px;color:var(--dim);margin-top:8px}
.act{color:var(--red);margin-left:2px}.actnote{font-size:14px;color:var(--mute);margin:8px 0 0}.actnote b{color:var(--red)}
.srcfoot{display:block;margin-top:10px;padding-top:6px;border-top:1px solid var(--line);font-size:12px;color:var(--dim)}.srcfoot a{color:var(--dim);margin-right:10px}.srcfoot a:hover{color:var(--red-hi)}
.lph{margin:10px 0 14px;max-width:min(360px,100%)}
.lph img{display:block;width:100%;height:auto;max-height:420px;object-fit:contain;background:#111}
.lph figcaption{margin-top:6px;font-size:13px;color:var(--dim);line-height:1.45}
/* Series jump: slim sticky bar (one select) + full link list that scrolls away with the page */
.jbar{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:10px;height:48px;margin:0 0 8px;background:rgba(14,14,15,.97);border-bottom:1px solid var(--line)}
.jbar label{flex:none;font-size:12px;color:var(--dirt);letter-spacing:.1em}
.jbar select{flex:1 1 auto;min-width:0;max-width:420px;height:38px;padding:0 10px;background:var(--panel);color:var(--fg);border:1px solid #3a3d41;border-radius:4px;font:inherit;font-size:16px}
.jbar select:focus-visible{outline:2px solid var(--red-hi);outline-offset:2px}
.jbox{margin:0 0 10px}
.jbox>summary{cursor:pointer;list-style:none;display:inline-flex;align-items:center;gap:8px;padding:6px 0;font-size:13px;color:var(--mute);letter-spacing:.08em}
.jbox>summary::-webkit-details-marker{display:none}
.jbox>summary::after{content:"\\25BE";font-size:12px}
.jbox[open]>summary::after{content:"\\25B4"}
.jump{position:static;z-index:auto;padding:0;border-bottom:0;background:none;margin:4px 0 6px}
.ser{scroll-margin-top:64px}
@media (max-width:640px){.jlbl{min-width:0;width:100%}.jbar label{display:none}.jbar select{max-width:none}}
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
NOTES={'410 Sprint Cars': '410 cubic-inch engines, the top level of sprint car racing. Winged: World of Outlaws, High Limit, NARC/King of the West, NCRA, All Stars, PA Posse, POWRi 410. Non-winged: USAC Sprint.', '360 Sprint Cars': '360 cubic-inch engines, the regional and national 360 tours.', 'Midgets': 'Small, light open-wheel cars, raced separately from sprint cars.', 'Silver Crown & USAC Triple Crown': 'Front-engine Champ Dirt Cars, plus the drivers who won USAC titles in Sprint, Midget and Silver Crown.'}
out=[];cg=None
for s in d['series']:
  if s.get('group')!=cg:
    cg=s.get('group');out.append(f'<h2 class="grp disp" id="g-{re.sub(r"[^a-z0-9]+","-",cg.lower()).strip("-")}">{E(cg)}</h2>')
  b=[f'<section class="ser-wrap" aria-labelledby="h-{s["id"]}"><details class="ser" id="{s["id"]}" open><summary><h2 class="disp" id="h-{s["id"]}">{E(s["name"])}</h2></summary>']
  if s.get('intro'): b.append(f'<p class="intro">{E(s["intro"])}</p>')
  if s.get('top5'):
    b.append('<aside class="top5" aria-label="All-time feature wins, top five"><span class="lbl">All-time feature wins: top five</span><ol>'+''.join(f'<li>{E(n)} <b>{E(str(w))}</b></li>' for n,w in s['top5'])+'</ol>')
    if s.get('top5_note'): b.append(f'<p class="tnote">{E(s["top5_note"])}</p>')
    b.append(srcs(s.get('top5_sources'))+'</aside>')
  for g in s.get('legends',[]):
    fid=f'bio-{s["id"]}-'+re.sub(r'[^a-z0-9]+','-',g['name'].lower()).strip('-')
    x=[f'<article class="leg" aria-labelledby="{fid}-h"><h3 class="disp" id="{fid}-h">{E(g["name"])}'+('<span class="act" title="Active driver">*</span>' if g.get('active') else '')+(f'<span class="nick">"{E(g["nickname"])}"</span>' if g.get('nickname') else '')+'</h3>']
    if g.get('photo'):
        cap=g.get('photo_caption') or g['name']
        cred=g.get('photo_credit') or ''
        fig=f'<figure class="lph"><img src="{E(g["photo"])}" alt="{E(cap)}">'
        fc=E(cap)
        if cred:
            if not cap.endswith(('.', '!', '?')):
                fc += '.'
            fc += ' Photo: '+E(cred)
        fig += f'<figcaption>{fc}</figcaption></figure>'
        x.append(fig)
    x.append(f'<p class="snip">{E(snippet(g))}</p><div class="full" id="{fid}" hidden>'+''.join(f'<p>{E(p)}</p>' for p in g.get('synopsis',[]) if p))
    if g.get('achievements'): x.append('<span class="lbl">Notable achievements</span><ul class="ach">'+''.join(f'<li>{E(a)}</li>' for a in g['achievements'])+'</ul>')
    x.append('</div>'+(f'<p class="stats">'+' <span aria-hidden="true">&middot;</span> '.join(E(t) for t in g['stats'])+'</p>' if g.get('stats') else '')+f'<button type="button" class="more" aria-expanded="false" aria-controls="{fid}">Read more</button>')
    x.append(srcs(g.get('sources'))+'</article>'); b+=x
  out.append(''.join(b)+'</details></section>')
hdr=src[src.index('<header>'):src.index('</header>')+9]
hdr=hdr.replace('<li><a href="legends.html" class="lbl">Legends</a></li>','<li><a href="legends.html" class="lbl" aria-current="page">Legends</a></li>')
ftr=src[src.index('<footer>'):src.index('</footer>')+9]
import itertools
jump0='<nav class="jump" aria-label="Series">'+''.join('<div class="jgrp"><span class="jlbl lbl">'+E(k)+'</span>'+''.join(f'<a href="#{s["id"]}" class="lbl">{E(s["name"])}</a>' for s in v)+'</div>' for k,v in itertools.groupby(d['series'],key=lambda s:s.get('group','')))+'</nav>'
bar='<div class="jbar"><label class="lbl" for="jsel">Jump to</label><select id="jsel" aria-label="Jump to a series">'+'<option value="">Jump to a series&hellip;</option>'+''.join('<optgroup label="'+E(k)+'">'+''.join(f'<option value="{s["id"]}">{E(s["name"])}</option>' for s in v)+'</optgroup>' for k,v in itertools.groupby(d['series'],key=lambda s:s.get('group','')))+'</select></div>'
jump=bar+'\n<details class="jbox" id="jbox" open><summary class="lbl">All series</summary>'+jump0+'</details>'
js="<script>function oh(){var e=document.getElementById(location.hash.slice(1));if(e&&e.tagName=='DETAILS')e.open=true}window.addEventListener('hashchange',oh);oh();var js_=document.getElementById('jsel');if(js_)js_.addEventListener('change',function(){var e=document.getElementById(js_.value);if(!e)return;e.open=true;e.scrollIntoView();if(history.replaceState)history.replaceState(null,'','#'+js_.value);js_.selectedIndex=0;});if(window.matchMedia&&matchMedia('(max-width:640px)').matches){var jb=document.getElementById('jbox');if(jb)jb.open=false;}document.addEventListener('click',function(ev){var b=ev.target.closest('.more');if(!b)return;var f=document.getElementById(b.getAttribute('aria-controls')),o=b.getAttribute('aria-expanded')=='true';f.hidden=o;f.parentNode.querySelector('.snip').hidden=!o;b.setAttribute('aria-expanded',String(!o));b.textContent=o?'Read more':'Show less';if(o)f.parentNode.scrollIntoView({block:'nearest'})});</script>"
page=head+'</style><style>'+css+'</style></head><body>\n'+hdr+'\n<main class="wrap">\n<header class="lhero"><img class="lhimg" src="images/this-day-hero.jpg" alt="Classic sprint cars"><span class="lbl tag">Guide</span><h1 class="disp">Legends</h1><p>The people who built sprint car and midget racing.</p>'+(f'<p class="actnote"><b>*</b> {E(d["active_note"].lstrip("* "))}</p>' if d.get('active_note') else '')+'</header>\n'+jump+'\n'+'\n'.join(out)+'\n'+(f'<p class="actnote"><b>*</b> {E(d["active_note"].lstrip("* "))}</p>' if d.get('active_note') else '')+'\n</main>\n'+js+'\n'+ftr+'\n<script src="to-top.js" defer></script>\n</body></html>\n'
open('legends.html','w').write(page)
