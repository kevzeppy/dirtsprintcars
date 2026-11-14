# Results Archive — Research Session 1 (2026-11-13, Grok History bot)
Research only. No site pages, PRs, or pushes. Files: notes.md, sources.csv, schema.json, sample_amains_2026.csv (48 verified A-main rows, Knoxville + Kings Royal 2026).

## 1. Events
### 2026 Knoxville Nationals (65th) — Knoxville Raceway, finale Sat Aug 15, 2026 (A-main ran early Sun after rain delay)
- Winner Kyle Larson (#57, Paul Silva), led all 50 laps, 4th Nationals win, $200,000. https://www.knoxvilleraceway.com/press/2026/article/194952
- Full 24-car A-main w/ start pos, car #, hometown: https://www.floracing.com/articles/16132089-2026-knoxville-nationals-results-at-knoxville-raceway ; matches https://tjslideways.com/2026/08/16/larsons-flies-to-fourth-knoxville-nationals-title/ and https://scmotorsportsmedia.com/kyle-larson-wins-world-of-outlaws-knoxville-nationals-race-results-08-15-2026/
- Depth on official press: A (start pos, hometown), B (22 laps, Courtney won), C (15, Ryan Timms), D (12, Darin Naida), lap leader (Larson 1-50), hard charger (Holmes). Lineup points + Hard Knox in Flo live blog: https://www.floracing.com/articles/16130570-live-from-knoxville-2026-knoxville-nationals-saturday-updates
- Season PDF ("2026 Results, Stories and Points") at https://www.knoxvilleraceway.com/historic-results/ ; prelim nights (qual/heats) via track press + MyRacePass event pages. Not yet row-extracted.
- Laps completed/DNF for non-winners: not in sources checked → blank.
### 2026 Kings Royal (43rd) — Eldora Speedway, Jul 17-18, 2026
- Winner Anthony Macri (#39M), started 1st, led 16 of 41 laps, $200,000; back-to-back. https://worldofoutlaws.com/sprintcars/schedule/event-info/?event=4549387
- WoO table: pos, start, +/-, car, driver, laps, behind, led, status, points, money (24 cars). Eldora page has Qualifying, Heats 1-6 (10 laps), Last Chance Showdown (15), Dash (12), Feature (40): https://www.eldoraspeedway.com/event_coverage/43rd-kings-royal/ . Friday "Knight Before" winner Corey Day (Flo: https://www.floracing.com/articles/16079831-kings-royal-results-from-eldora-speedway-macri-does-it-again).
- FLAG: scheduled 40 laps; 41 run (GWC) per WoO. Lap-leader exact ranges: Macri 1-12, Williamson from 13; Macri retook "coming to two to go" — exact lap numbers not published; WoO totals Macri 16 / Williamson 25.
### Turkey Night Grand Prix — Ventura Raceway (USAC National Midgets)
- 2026 (85th) NOT YET RUN: scheduled Sat Nov 28, 2026 (Nov 27-28 weekend). https://www.usacracing.com/news/event-info-ventura---usac-midgets---nov-28-2026 ; also listed http://sprintcarratings.com/RaceTitleResults.aspx?Series=USACM&Track=Ventura%2CCA
- Most recent completed: 84th, Sat Nov 29, 2025. Winner Corey Day (started 3rd), 98 laps, back-to-back; 2 Logan Seavey, 3 Buddy Kofoid, 4 Kyle Larson, 5 Kevin Thomas Jr. Full 28-car finish w/ starts. Lap leaders: Seavey 1-13, Day 14-17, Seavey 18-20, Day 21, Seavey 22-27, Day 28-65, Seavey 66, Day 67-69, Seavey 70-74, Day 75-98. Also qualifying (fast qual Daison Pursley 12.140), 3 qualifiers, semi, final points. https://www.usacracing.com/news/turkey-night-grand-prix-results-nov-29-2025 ; second source https://www.floracing.com/articles/14847598-usac-turkey-night-grand-prix-results-from-ventura-raceway
- Car numbers/hometowns not captured this session → blank until extracted from USAC page.

## 2. Source findings (detail in sources.csv)
- DIRTRACKR: free tier = full race results, driver lists, yearly stat breakdowns, wins/top5/laps led. Plus = $4.99/mo or $49.99/yr: full DIRTRACKR Rankings, Notebook, driver compare/projection, Track Explorer, start-position/draw analysis, Chili Bowl qualifier/VIROC stats. ~2,869-2,871 races / ~9,415 drivers / 12 series. Data "from public sources, largely gathered automatically" (https://dirtrackr.com/about) → cross-check only. Plus adds analytics, not more raw history. https://dirtrackr.com/plus-features . Not signed up.
- sprintcarstats.com: Kevin Eckert's site. Wayback: Jan 2011 WordPress blog ("statistical data... Sprint Cars, Midgets, Supermodifieds and Champ Cars by Kevin Eckert"); Jan 2011 post says his Open Wheel Times site was hit by a virus in March 2010 after seven years (that is the data-loss event found; "server crash" wording not verified). 2013-2015: MyRacePass-hosted "Eckert's Blog" (2015 nav adds /driverStats/, not archived). By Mar 2021 and today: WordPress "Sprint Car Stats | Automobile magazine" generic car blog (repurposed). No result database recoverable from Wayback in this pass; which years were lost cannot be stated. Live site blocks curl (406 Mod_Security) without browser headers.
- Knoxville Raceway: season PDFs 1961-2026 (1961-1976 combined file), full depth (1985 PDF = 42 pp with time trials, heats, features, stories). Plus Nationals records, quick-time records, all-time 410/360/305 wins, track champions, WoO/USAC wins, HoF. Free; no reuse license; facts citable.
- National Sprint Car Hall of Fame (sprintcarhof.com): research library on-site in Knoxville; no online results database found → use for verification by request.
- Third Turn: 249,488 drivers / 3,071 tracks / 597,175 races (home page 2026-11-13); inner pages now return "Please log in to view other pages" for anonymous visitors (free account, but we must not sign up without Kevin). Ultimate Racing History: HTTP 500 today.
- Speed Sport: print magazine ended Dec 2022 (https://speedsport.com/insider/columns/a-new-era-for-speed-sport/); now web + Insider newsletter. National Speed Sport News (weekly paper) final print Mar 23, 2011; archives at IMRRC Watkins Glen: 97 bound volumes from 1930s + microfilm 1930s-early 2000s (https://www.racingarchives.org/the-collections/national-speed-sport-news-archives/). No digitized online back-issue set found (Internet Archive search: 0 hits). U of Illinois library holds 1946-1981 print (search result: https://www.library.illinois.edu/hpnl/newspapers/results_full.php?bib_id=14957).
- Open Wheel Magazine: Summer 1980 launch (Stock Car Racing publisher), bimonthly 1982, monthly by 1988, standalone through Dec 2001, then supplement in Stock Car Racing to mid-2002 (https://www.richardrobertsarchive.org.uk/stockport-advertising-archive-blog/latest-archive-acquisitions-august-2021). Sold to EMAP Petersen 1999 (Doug Auld replaced Dick Berggren), folded under Primedia after 9/11 (https://en.wikipedia.org/wiki/Doug_Auld). Not digitized: Internet Archive 0 relevant hits; Google Books API 0. Holdings: Revs Institute misc periodicals Box 59 (https://revsinstitute.org/WMS/1152523990.pdf); Richard Roberts Archive (UK). WorldCat not checked (JS-only site). Back issues: Jim's Mega Magazines (https://www.jimsmegamagazines.com/open-wheel-1981-1989/c-21-334-704.html), pastpaper.com, pitstopbooks.com. Copyright held by publisher/successor (unclear) → facts only, no scans/prose/photos.
- Others: DIRTVision free account = Vault replays; paid $39.99/mo or $299.99/yr (search summary of https://join.dirtvision.com/compare-all-plans; not opened). Newspapers.com Basic $7.95/mo, Publisher Extra $19.90/mo (search summary). Google News Archive https://news.google.com/newspapers loads (frozen scans, free). MyRacePass ToS: personal non-commercial copying only (https://www.myracepass.com/terms). WoO ToS: content copyrighted (https://worldofoutlaws.com/terms-of-use/).
- Legal footing: bare facts (positions, names, laps) are not copyrightable in the US (Feist v. Rural, https://supreme.justia.com/cases/federal/us/499/340/); re-key facts with citation, never copy prose, tables' creative layout, or photos; no bulk scraping where ToS prohibit.

## 3. Recommended structure
- Canonical data: one CSV/JSON row per driver per session (schema.json). Files: data/results/<year>/<event_id>.json + combined results-index.json (event list) for search.
- Pages: per-event-per-year pages (e.g. /results-archive/knoxville-nationals/2026) generated by build_results.py from JSON; event landing page lists all years + winners. Per-driver pages later, auto-generated from driver_id joins (no hand editing).
- Phase depth: A-main for every year first; add B/C/heats/qual for recent years where official data exists.

## 4. Next batch (proposal)
Batch 2 — crown-jewel A-mains + winners, 2026 → 2016 (2020 Knoxville not held):
- Knoxville Nationals 2016-2025 (Knoxville PDFs + WoO + Flo) ~240 rows
- Kings Royal 2016-2025 (WoO/Eldora + DIRTRACKR) ~240 rows
- National Open 2016-2026 (WoO results; 2026 winner Chase Dietz https://worldofoutlaws.com/sprintcars/results/?event=597918&series=sprintcars) ~265 rows
- Chili Bowl 2016-2026 (chilibowl.com past champions/PDFs + DIRTRACKR) ~265 rows
- Australian Classic 2016-2026 (Premier Speedway/Speedway Illustrated; 2026 Aaron Reutzel https://www.speedwayillustratednews.com.au/2026/01/26/reutzel-avoids-carnage-in-dramatic-warrnambool-classic-win/) ~265 rows
- Turkey Night 2025 A-main (28) + 2026 after Nov 28.
≈1,300 rows. Batch 3: full depth (qual/heats/mains) for 2026 crown jewels (~2,500-3,500 rows est.). Then WoO/High Limit/USAC/ASCS season features 2026→ back; then GLSS, FAST, BOSS, Gladiator, Australia/NZ.

## Session 2 — Crown-jewel A-mains 2016–2026 (2026-11-13, Grok History bot)

Research and data only. No HTML pages, PRs, or `main`. Deliverables: `amains_2016_2026.csv` (1,193 rows, 875 verified), `data/*.json` per event, this notes section. Branch: `grok/history-results-archive-session2` (from `main`). A Third Turn account was not created; TTT inner pages are behind a WAF/login wall and were not used. No browser was available this session.

### Counts (A-main rows / verified when two independent sources agreed on driver and finishing position)

| Event | Event-years | Rows | Verified | Notes |
|---|---:|---:|---:|---|
| Knoxville Nationals | 10 (no 2020) | 242 | 242 | Official season PDFs + WoO (2016) or DIRTRACKR (2017–2026); 2026 also agrees with TJSlideways |
| Kings Royal | 10 years + two 2021 A-mains (no 2020) | 264 | 221 | 37th and 38th both ran 2021-07-17 (Larson; Courtney). 2016 official-only (no DIRTRACKR coverage). 2023–24 official WoO widget only partially parsed; deeper cars are DIRTRACKR-only |
| National Open | 11 | 300 | 182 | 2022 championship ran Friday 2022-09-30. 2016 official-only. 2018/2021 official recaps lacked a parseable feature list this session (DIRTRACKR only). 2024/2026 official widget tails incomplete |
| Chili Bowl (Saturday A-main) | 11 | 266 | 194 | Official chilibowl.com press/media-results + DIRTRACKR except 2018, 2023, 2024 (DIRTRACKR only; winners also on past-champions). 2025 A-main was 40 laps, not the usual 55 (official + DIRTRACKR agree) |
| Australian Classic (Grand Annual, Premier Speedway) | 9 (no 2021; no 2018 field) | 91 | 9 | Full TJS fields for 2017, 2020, 2026 (top 3 also on Wikipedia). Other years Wikipedia top 3 only, dates blank. 2021 not held under the Classic name (50 for Fifty) |
| Turkey Night 2025 | 1 (major, not crown jewel) | 28 | 28 | Official USAC recap + DIRTRACKR. Car numbers not published in either table; left blank. FloRacing recap returned HTTP 406 |
| **Total** | | **1,193** | **875** | |

### Gaps
- Knoxville Nationals 2020 and Kings Royal 2020: not held (COVID-19). A mid-August 2020 WoO race at Knoxville is not the Nationals.
- Australian Classic 2021: not run under the Grand Annual name.
- Australian Classic 2018: **conflict, no rows entered.** Wikipedia (citing MYLAPS Speedhive session 4719782, a JavaScript app that did not yield a static results page) lists Corey McCullagh, Carson Macedo, Brooke Tatnell. The Standard (Warrnambool) headline says Grant Anderson won a delayed Saturday-night Grand Annual A-main on Sunday, 2018-01-21. Not resolved without Speedhive or a full official sheet.
- Official Saturday Chili Bowl A-mains not located for 2018, 2023, 2024 (fields from DIRTRACKR only; `verified=false`).
- Official full fields not parsed for National Open 2018 and 2021; DIRTRACKR only.
- Kings Royal 2016 and National Open 2016: full official WoO lists, but DIRTRACKR’s WoO database starts in 2017, so `verified=false` pending a second source. National Open 2016 date recorded as 2016-10-01 with a flag: the WoO recap (published 2016-10-14) describes the winning night as Friday.
- Some later WoO results-widget pages (Kings Royal 2023–24, National Open 2024 and 2026) only partially parsed; remaining positions are DIRTRACKR-only (`verified=false`).
- 2016 Knoxville official A-main list omitted car numbers; only Johnson #41 is filled (from the WoO recap). Other 2016 car numbers left blank rather than guessed from mid-season PDFs.
- Official typographical oddities left as published, with flags: 2017 Hodnett hometown “Spring Grove, CA” (other years PA); 2024 Brian Brown hometown “Grain Valley, CA” (other years MO); 2021 Brooke Tatnell car “0”.
- FloRacing articles often returned HTTP 406 (no browser). sprintcarratings.com title/result URLs returned HTTP 500. Ultimate Racing History was not re-tried as a 500 in Session 1.
- Australian Classic years without TJS full lists have blank `date` fields.

### Conflicts
No driver/position disagreements were kept between an official source and DIRTRACKR after discarding a couple of official pages whose parsed “feature” block was clearly the wrong race (notably a 2022 National Open recap page that mixed in another result). The outstanding 2018 Australian Classic winner conflict is above; no 2018 rows were written.

### Sources used (facts re-keyed, no prose/photos copied)
- Knoxville Raceway official season PDFs, 2016–2026: https://www.knoxvilleraceway.com/historic-results/ (`/downloads/get.aspx?i=` IDs in the CSV).
- World of Outlaws recaps and results widgets; Eldora event-coverage pages (2018, 2019 Kings Royal).
- Official Chili Bowl press and media-results pages; chilibowl.com/past-champions for winner confirmation.
- USAC: https://www.usacracing.com/news/turkey-night-grand-prix-results-nov-29-2025
- TJSlideways (2026 Knoxville; 2017, 2020, 2026 Grand Annual).
- DIRTRACKR free result pages as the second source (cross-check; data “from public sources, largely gathered automatically”).
- Wikipedia Grand Annual page only as a top-3 cross-check or, when no other source was found, as a single tertiary source (`verified=false`).

### Proposed Session 3
Priority: close Session 2 gaps before going deeper or starting national-tour seasons.
1. Official Chili Bowl Saturday A-mains for 2018, 2023, 2024 (media-results event IDs) — ~72 rows to upgrade to verified.
2. Resolve 2018 Australian Classic (Speedhive 4719782 or Premier Speedway official) and collect official/TJS full A-mains for 2016, 2019, 2022–2025 — ~150–200 rows.
3. Second sources for Kings Royal 2016 and National Open 2016, plus complete official tails for Kings Royal 2023–24 and National Open 2024/2026 — ~80 rows to upgrade.
4. Then, if approved: 2026 crown-jewel prelims (qual, heats, B/C/D, dashes) or 2025–2026 national-tour A-mains (WoO, High Limit, USAC, ASCS).
Estimated Session 3 row count if only the gap-fill is done: about 250–350 new or upgraded rows. If 2026 crown-jewel full depth is included: about 2,500–3,500 additional rows (Session 1 estimate).
