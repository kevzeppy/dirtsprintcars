"""Build crown-jewels.html from crown-jewels-data.json, reusing the legends.html shell."""
import json,html,re
D=json.load(open('crown-jewels-data.json'))
L=open('legends.html').read()
head=L[:L.find('<main')]
foot=L[L.find('</main>')+7:]
foot=re.sub(r'<script>function oh\(\).*?</script>','',foot,count=1,flags=re.S)
title='Sprint Car Crown Jewels History: Knoxville Nationals, Kings Royal, National Open, Chili Bowl &amp; Australian Classic Results | DirtSprintCars.com'
desc='Every Knoxville Nationals, Kings Royal, National Open, Chili Bowl and Grand Annual Sprintcar Classic winner, with full A-main finishing orders by year.'
head=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',head,flags=re.S)
head=re.sub(r'(<meta name="description" content=")[^"]*',r'\g<1>'+desc,head)
head=re.sub(r'(<meta property="og:description" content=")[^"]*',r'\g<1>'+desc,head)
head=re.sub(r'(<meta property="og:title" content=")[^"]*',r'\g<1>Sprint Car Crown Jewels History | DirtSprintCars.com',head)
css='''<style>
.cjt{width:100%;border-collapse:collapse;font-size:15px;margin:6px 0 4px}
.cjt th{text-align:left;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;letter-spacing:.04em;color:var(--dim);font-weight:700;border-bottom:1px solid var(--line);padding:6px 8px}
.cjt td{border-bottom:1px solid var(--line);padding:6px 8px;vertical-align:top}
.cjt td.yr{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:18px;color:var(--fg);width:64px}
.cjt td.w{font-weight:600}.cjt .num{color:var(--dim);font-size:13px;margin-left:6px}
.cjt details summary{cursor:pointer;color:var(--red-hi);font-size:13px}
.cjt .fo{columns:2;column-gap:24px;margin:6px 0 2px;padding-left:28px;font-size:14px;color:var(--mute)}
.cjt .fo li{break-inside:avoid}
.cjt .nh{color:var(--dim);font-style:italic}
.yrs{display:flex;flex-wrap:wrap;margin:4px 0 10px;max-height:96px;overflow-y:auto}.mw{display:flex;flex-wrap:wrap;gap:6px 18px;margin:6px 0 10px;font-size:14px;color:var(--mute)}.mw b{color:var(--fg)}
@media(max-width:640px){.cjt .p3,.cjt th.p3{display:none}.cjt .fo{columns:1}}
</style>'''
head=head.replace('</head>',css+'</head>',1)
e=html.escape
def ok(x):
    st=(x.get('status') or '').strip().lower()
    return bool(st) and not st.startswith('freeform') and not st.startswith(x['driver'].lower().split(' (')[0][:6]) and st.replace(' ','').isalnum() and len(st)<12
out=['<main class="wrap">','<header class="lhero"><img class="lhimg" src="images/crown-jewels-hero-knoxville.jpg" alt="Knoxville Raceway grandstands and press box"><p class="phcred" style="margin:-18px 0 20px;font-size:12px;color:#a4a8ae">Photo: Knoxville Raceway, courtesy <a href="https://www.knoxvilleraceway.com/press/2015/article/34345" rel="noopener" target="_blank">Knoxville Raceway press</a></p><span class="lbl tag">History</span><h1 class="disp">Crown Jewels</h1><p>Every winner of sprint car and midget racing&#x27;s five crown jewel events, with A-main finishing orders.</p><p class="cjnote">Crown jewels: Knoxville Nationals, Kings Royal, National Open, Chili Bowl and Australian Classic (Grand Annual Sprintcar Classic, Warrnambool). See also <a href="legends.html">Legends</a> and <a href="this-day-in-history.html">This Day</a>.</p></header>']
out.append('<nav class="jump" aria-label="Events"><div class="jgrp"><span class="jlbl lbl">Crown Jewels</span>'+''.join(f'<a href="#{ev["id"]}" class="lbl">{e(ev["name"])}</a>' for ev in D['events'])+'</div></nav>')
for ev in D['events']:
    wins={}
    for r in ev['races']:
        if r.get('winner'): wins.setdefault(r['winner'],[]).append(r['year'])
    top=sorted(wins.items(),key=lambda x:(-len(x[1]),x[1][0]))
    top=[t for t in top if len(t[1])>=len(top[min(4,len(top)-1)][1]) and len(t[1])>1][:6]
    o=[f'<section class="ser-wrap" aria-labelledby="h-{ev["id"]}"><details class="ser" id="{ev["id"]}" open><summary><h2 class="disp" id="h-{ev["id"]}">{e(ev["name"])}</h2></summary>',f'<p class="intro">{e(ev["intro"])}</p>']
    o.append('<aside class="top5" aria-label="Most wins"><span class="lbl">Most wins</span><ol>'+''.join(f'<li>{e(n)} <b>{len(y)}</b></li>' for n,y in top)+'</ol></aside>')
    ys=sorted({r['year'] for r in ev['races']},reverse=True)
    o.append('<div class="yrs" role="group" aria-label="Pick a year"><button type="button" class="yf on" data-y="all">All</button>'+''.join(f'<button type="button" class="yf" data-y="{y}">{y}</button>' for y in ys)+'</div>')
    o.append('<table class="cjt"><thead><tr><th>Year</th><th>Winner</th><th>Second</th><th class="p3">Third</th><th>Full results</th></tr></thead><tbody>')
    for r in sorted(ev['races'],key=lambda r:(r['year'],r.get('label',''))):
        y=str(r['year'])+(f' <span class="num">{e(r["label"])}</span>' if r.get('label') else '')
        if r.get('not_held'):
            o.append(f'<tr data-y="{r["year"]}"><td class="yr">{r["year"]}</td><td colspan="4" class="nh">{e(r["not_held"])}</td></tr>');continue
        fo=r.get('finish',[])
        p=lambda i:e(fo[i]['driver']) if len(fo)>i else ''
        car=f'<span class="num">#{e(r["car"])}</span>' if r.get('car') else ''
        full=''
        if len(fo)>3:
            full='<details><summary>'+str(len(fo))+' finishers</summary><ol class="fo">'+''.join(f'<li>{e(x["driver"])}'+(f' <span class="num">#{e(x["car"])}</span>' if x.get('car') else '')+(f' <span class="num">{e(x["status"])}</span>' if ok(x) else '')+'</li>' for x in fo)+'</ol></details>'
        o.append(f'<tr data-y="{r["year"]}"><td class="yr">{y}</td><td class="w">{e(r["winner"])}{car}</td><td>{p(1)}</td><td class="p3">{p(2)}</td><td>{full}</td></tr>')
    o.append('</tbody></table>')
    o.append('<footer class="srcfoot">Sources: '+''.join(f'<a href="{e(u)}" target="_blank" rel="noopener">{e(n)}</a>' for n,u in ev['sources'])+'</footer>')
    o.append('</details></section>')
    out+=o
out.append('</main>')
out.append('''<script>document.querySelectorAll('.ser').forEach(function(sec){var bs=sec.querySelectorAll('.yf'),rows=sec.querySelectorAll('tbody tr');
function pick(y){bs.forEach(function(b){b.classList.toggle('on',b.dataset.y===y)});rows.forEach(function(r){var m=y==='all'||r.dataset.y===y;r.classList.toggle('hid',!m);var d=r.querySelector('details');if(d)d.open=(y!=='all'&&m)});}
bs.forEach(function(b){b.addEventListener('click',function(){pick(b.dataset.y)})});
rows.forEach(function(r){var c=r.querySelector('td.yr');c.style.cursor='pointer';c.addEventListener('click',function(){var d=r.querySelector('details');if(d)d.open=!d.open})});});</script>''')
open('crown-jewels.html','w').write(head+'\n'.join(out)+foot)
print('ok')
