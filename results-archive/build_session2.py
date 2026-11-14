#!/usr/bin/env python3
"""Results Archive Session 2 compiler. Official sources preferred; DIRTRACKR/TJS as second source."""
from __future__ import annotations
import csv, json, re, html as htmlmod
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime as dtdatetime
from collections import defaultdict

ROOT = Path("/workspace/results-archive")
WEB = ROOT / "raw" / "web"
DTR = ROOT / "raw" / "dtr"
KNOX_JSON = ROOT / "raw" / "parsed" / "knox_parsed_v2.json"
OUT_CSV = ROOT / "amains_2016_2026.csv"
OUT_DATA = ROOT / "data"
UPDATED = "2026-11-13"

# Official Knoxville season PDF download IDs (knoxvilleraceway.com/historic-results)
KNOX_PDF = {
    2016: 928428, 2017: 928429, 2018: 928431, 2019: 928433,
    2021: 928435, 2022: 928436, 2023: 928437, 2024: 988529,
    2025: 1143202, 2026: 1271478,
}
def knox_pdf_url(y):
    return f"https://www.knoxvilleraceway.com/downloads/get.aspx?i={KNOX_PDF[y]}"

# DTR championship A-main pages
DTR_URL = "https://dirtrackr.com{}"
DTR_MAP = {
    # (event_key, year) -> (relpath, local filename)
    ("knoxville-nationals", 2017): ("/analytics/results/woosprint/468", "knox_468.html"),
    ("knoxville-nationals", 2018): ("/analytics/results/woosprint/147", "knox_147.html"),
    ("knoxville-nationals", 2019): ("/analytics/results/woosprint/28", "knox_28.html"),
    ("knoxville-nationals", 2021): ("/analytics/results/woosprint/387", "knox_387.html"),
    ("knoxville-nationals", 2022): ("/analytics/results/woosprint/617", "knox_617.html"),
    ("knoxville-nationals", 2023): ("/analytics/results/woosprint/717", "knox_717.html"),
    ("knoxville-nationals", 2024): ("/analytics/results/woosprint/799", "knox_799.html"),
    ("knoxville-nationals", 2025): ("/analytics/results/woosprint/873", "knox_873.html"),
    ("knoxville-nationals", 2026): ("/analytics/results/woosprint/954", "knox_954.html"),
    ("kings-royal", 2017): ("/analytics/results/woosprint/484", "kr_484.html"),
    ("kings-royal", 2018): ("/analytics/results/woosprint/176", "kr_176.html"),
    ("kings-royal", 2019): ("/analytics/results/woosprint/40", "kr_40.html"),
    ("kings-royal-37", 2021): ("/analytics/results/woosprint/373", "kr_373.html"),
    ("kings-royal-38", 2021): ("/analytics/results/woosprint/372", "kr_372.html"),
    ("kings-royal", 2022): ("/analytics/results/woosprint/597", "kr_597.html"),
    ("kings-royal", 2023): ("/analytics/results/woosprint/706", "kr_706.html"),
    ("kings-royal", 2024): ("/analytics/results/woosprint/789", "kr_789.html"),
    ("kings-royal", 2025): ("/analytics/results/woosprint/865", "kr_865.html"),
    ("kings-royal", 2026): ("/analytics/results/woosprint/941", "kr_941.html"),
    ("national-open", 2017): ("/analytics/results/woosprint/438", "no_438.html"),
    ("national-open", 2018): ("/analytics/results/woosprint/117", "no_117.html"),
    ("national-open", 2019): ("/analytics/results/woosprint/7", "no_7.html"),
    ("national-open", 2020): ("/analytics/results/woosprint/311", "no_311.html"),
    ("national-open", 2021): ("/analytics/results/woosprint/411", "no_411.html"),
    ("national-open", 2022): ("/analytics/results/woosprint/643", "no_643.html"),
    ("national-open", 2023): ("/analytics/results/woosprint/735", "no_735.html"),
    ("national-open", 2024): ("/analytics/results/woosprint/814", "no_814.html"),
    ("national-open", 2025): ("/analytics/results/woosprint/887", "no_887.html"),
    ("national-open", 2026): ("/analytics/results/woosprint/971", "no_971.html"),
    ("chili-bowl", 2016): ("/analytics/results/chilibowl/38", "chili_38.html"),
    ("chili-bowl", 2017): ("/analytics/results/chilibowl/31", "chili_31.html"),
    ("chili-bowl", 2018): ("/analytics/results/chilibowl/26", "chili_26.html"),
    ("chili-bowl", 2019): ("/analytics/results/chilibowl/17", "chili_17.html"),
    ("chili-bowl", 2020): ("/analytics/results/chilibowl/1", "chili_1.html"),
    ("chili-bowl", 2021): ("/analytics/results/chilibowl/76", "chili_76.html"),
    ("chili-bowl", 2022): ("/analytics/results/chilibowl/122", "chili_122.html"),
    ("chili-bowl", 2023): ("/analytics/results/chilibowl/165", "chili_165.html"),
    ("chili-bowl", 2024): ("/analytics/results/chilibowl/173", "chili_173.html"),
    ("chili-bowl", 2025): ("/analytics/results/chilibowl/181", "chili_181.html"),
    ("chili-bowl", 2026): ("/analytics/results/chilibowl/191", "chili_191.html"),
    ("turkey-night", 2025): ("/analytics/results/usacmidget/236", "tngp_236.html"),
}

ALIASES = {
    "gio scelzi": "giovanni scelzi",
    "giovanni scelzi": "giovanni scelzi",
    "buddy kofoid": "michael kofoid",
    "michael kofoid": "michael kofoid",
    "parker price miller": "parker price-miller",
    "parker price-miller": "parker price-miller",
    "c j leary": "cj leary",
    "c.j. leary": "cj leary",
    "cj leary": "cj leary",
    "t j smith": "tj smith",
    "t.j. smith": "tj smith",
    "tj smith": "tj smith",
    "joe b miller": "joe b. miller",
    "joe b. miller": "joe b. miller",
    "ricky stenhouse jr": "ricky stenhouse jr",
    "corey eliason": "cory eliason",
    "cory eliason": "cory eliason",
    "jordy rae": "jordan rae",
    "jordan rae": "jordan rae",
    "marcus dumesney": "marcus dumesny",
    "marcus dumesny": "marcus dumesny",
    "bradley vaughn": "bradley vaughan",
    "bradley vaughan": "bradley vaughan",
    "corey mcgullagh": "corey mccullagh",
    "jorydan brazier": "jordon brazier",
    "robbie farrer": "robbie farr",
}

def norm_name(s: str | None) -> str:
    if not s:
        return ""
    t = s.lower()
    t = t.replace("’", "'").replace("‘", "'")
    t = re.sub(r"\.", "", t)
    t = re.sub(r",?\s*jr\.?$", "", t)
    t = re.sub(r",?\s*junior$", "", t)
    t = re.sub(r"[^a-z0-9\s\-']", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    t = t.replace(" - ", " ")
    return ALIASES.get(t, t)

def slug(s: str) -> str:
    t = norm_name(s)
    t = t.replace(" jr", "").strip()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t

def money_int(s):
    if s is None or s == "":
        return None
    t = re.sub(r"[^0-9]", "", str(s))
    return int(t) if t else None

def parse_dtr_feature(path: Path):
    """Return list of finish dicts + meta from a DIRTRACKR result page Feature section."""
    html = path.read_text(errors="replace")
    soup = BeautifulSoup(html, "lxml")
    # first Feature h3
    h3 = None
    for h in soup.find_all(["h2", "h3"]):
        if h.get_text(strip=True) == "Feature":
            h3 = h
            break
    if not h3:
        return [], {}
    # section container: climb to a parent that includes 'cars' and rows, stop before next h3 Feature sibling
    # find following grid rows until next h2/h3
    section = h3.parent
    # expand to include the results block (parent of heading + following py-3 div)
    block = section.parent if section and section.parent else section
    # If multiple sessions, limit to nodes after this h3 until next h3
    rows = []
    cars_n = None
    # get car count near heading
    sib_txt = section.get_text(" ", strip=True)
    m = re.search(r"(\d+)\s+cars", sib_txt)
    if m:
        cars_n = int(m.group(1))
    # collect a.grid after this heading until next h2/h3 whose text is not empty session
    started = False
    # iterate all elements in document order from h3
    for el in h3.find_all_next():
        if el.name in ("h2", "h3"):
            if el is h3:
                continue
            # next session
            break
        if el.name in ("a", "div") and el.has_attr("class") and any("grid" in c for c in el.get("class", [])):
            spans = el.find_all("span", recursive=False)
            if len(spans) < 3:
                continue
            texts = [s.get_text(" ", strip=True) for s in spans]
            # Fin, St, Driver, [Money], +/-, HC, Led, Tot Led  OR without money
            status = None
            try:
                pos = int(texts[0])
                start = int(texts[1]) if texts[1].isdigit() else None
            except ValueError:
                if texts[0] in ("DNS", "DNF", "DQ", "DNQ"):
                    status = texts[0]
                    pos = None
                    start = int(texts[1]) if texts[1].isdigit() else None
                else:
                    continue
            driver = texts[2]
            purse = None
            laps_led = None
            led_ranges = None
            # detect money column (starts with $)
            idx = 3
            if idx < len(texts) and texts[idx].startswith("$"):
                purse = money_int(texts[idx])
                idx += 1
            # +/- skip
            if idx < len(texts):
                idx += 1
            # HC maybe "HC"
            if idx < len(texts):
                idx += 1
            # Led ranges
            if idx < len(texts) and re.search(r"\d", texts[idx]):
                led_ranges = texts[idx]
            if idx + 1 < len(texts) and texts[idx + 1].isdigit():
                laps_led = int(texts[idx + 1])
            elif led_ranges is None and idx < len(texts) and texts[idx].isdigit() and int(texts[idx]) == 0:
                laps_led = 0
            rows.append({
                "pos": pos, "start": start, "driver": driver,
                "purse_usd": purse, "laps_led": laps_led,
                "lap_leader_ranges": led_ranges if led_ranges else None,
                "car": None, "hometown": None, "status": status,
            })
    # assign trailing DNS/DNF rows a published-order position after last numbered finish
    last = max((r["pos"] for r in rows if r.get("pos") is not None), default=0)
    for r in rows:
        if r.get("pos") is None:
            last += 1
            r["pos"] = last
            r["_pos_note"] = "position is published DNS/DNF list order after running cars"
    meta = {"n_cars": cars_n}
    # title date
    if soup.title:
        tm = re.search(r"([A-Z][a-z]{2} \d{1,2}, \d{4})", soup.title.get_text())
        if tm:
            meta["title_date"] = tm.group(1)
    return rows, meta


def parse_chili_afeature(html_path: Path):
    soup = BeautifulSoup(html_path.read_text(errors="replace"), "lxml")
    text = re.sub(r"\s+", " ", soup.get_text(" "))
    # pick the longest A Feature (championship 40 or 55, not 25 prelim)
    hits = list(re.finditer(r"A Feature(?: 1)? \((\d+) Laps\):\s*", text, re.I))
    if not hits:
        return [], {}
    # prefer 55, else 40, else max laps that's >= 40
    cand = [h for h in hits if int(h.group(1)) >= 40]
    if not cand:
        return [], {}
    best = max(cand, key=lambda h: int(h.group(1)))
    laps = int(best.group(1))
    rest = text[best.end():]
    # cut at next session
    rest = re.split(r"\s+(?:B-Feature|B Feature|Pole |MPV |Ferguson |Heat |C-Feature|C Feature|Qualifier)", rest, maxsplit=1)[0]
    rows = []
    # 1. 97-Rico Abreu[4]; 22. (DNF) 71X-Shane Cottle[12]; 24. (DNS) 20A-Alex Shanks
    for m in re.finditer(
        r"(\d+)\.\s+(?:\((DNF|DNS|DQ)\)\s+)?([0-9A-Za-z]+)-([^\[\];]+)(?:\[(\d+)\])?\s*;?",
        rest,
    ):
        pos = int(m.group(1))
        status = m.group(2)
        car = m.group(3)
        driver = re.sub(r"\s+", " ", m.group(4)).strip(" ;,")
        start = int(m.group(5)) if m.group(5) else None
        if not driver or len(driver) > 40:
            continue
        rows.append({
            "pos": pos, "start": start, "car": car, "driver": driver,
            "status": status, "hometown": None, "purse_usd": None,
            "laps_led": None, "lap_leader_ranges": None,
        })
    return rows, {"scheduled_laps": laps}


def parse_woo_recap_feature(html_path: Path):
    """Parse classic WoO recap 'Feature (40 Laps) – 1. 15-Donny Schatz [3][$50,000];'"""
    soup = BeautifulSoup(html_path.read_text(errors="replace"), "lxml")
    text = re.sub(r"\s+", " ", soup.get_text(" "))
    m = re.search(
        r"((?:RESULTS\s+)?(?:NOS Energy Drink Feature|A-Main|A Main|Feature(?:\s+Results)?)\s*[:–—-]*\s*\(?\s*(\d+)\s*Laps?\)?\s*(?:[–—-]:|:|[–—-])?\s*)",
        text, re.I,
    )
    if not m:
        m2 = re.search(r"(A Main\s*[–—-]\s*)", text, re.I)
        if not m2:
            return [], {}
        rest = text[m2.end():]
        laps = None
    else:
        laps = int(m.group(2)) if m.group(2) else None
        rest = text[m.end():]
    # Some recaps omit "1." before the winner: "Feature (40 Laps) 7BC-Tyler Courtney [2][$175,000]; 2. ..."
    if not re.match(r"\s*1\.", rest):
        rest = "1. " + rest.lstrip()
    rest = re.split(r"\s+Lap Leaders?:\s*", rest, maxsplit=1, flags=re.I)
    body = rest[0]
    leaders = rest[1] if len(rest) > 1 else ""
    leaders = re.split(r"\s+KSE Hard|\s+Hard-charger|\s+Qualifying|\s+E main|\s+C-Main|\s+Photos|\s+For complete", leaders, maxsplit=1, flags=re.I)[0].strip(" .;")
    hc = None
    hm = re.search(r"(?:KSE Hard Charger Award|Hard-charger):\s*([^.]{0,80})", text, re.I)
    if hm:
        hc = hm.group(1).strip()
    body = re.split(r"\s+Lap Leaders?:", body, maxsplit=1, flags=re.I)[0]
    rows = []
    # 1. 15- Donny Schatz [3] [$50,000];  or 1. Jason Johnson (2);
    for mm in re.finditer(
        r"(\d+)\.\s+(?:([0-9A-Za-z]+)\s*[–-]\s*)?([A-Z][^\[;$]*?)\s*(?:\[(\d+)\]|\((\d+)\))\s*(?:\[?\$?([\d,]+)\]?)?",
        body,
    ):
        pos = int(mm.group(1))
        car = mm.group(2)
        driver = re.sub(r"\s+", " ", mm.group(3)).strip(" -")
        start = int(mm.group(4) or mm.group(5)) if (mm.group(4) or mm.group(5)) else None
        purse = money_int(mm.group(6)) if mm.group(6) else None
        rows.append({
            "pos": pos, "start": start, "car": car, "driver": driver,
            "purse_usd": purse, "status": None, "hometown": None,
            "laps_led": None, "lap_leader_ranges": None,
        })
    # keep a single consecutive feature from position 1
    trimmed = []
    expect = 1
    for r in rows:
        if r["pos"] == expect:
            trimmed.append(r)
            expect += 1
        elif trimmed and r["pos"] < expect:
            break
        elif not trimmed and r["pos"] != 1:
            continue
        else:
            break
    rows = trimmed
    meta = {"scheduled_laps": laps, "lap_leaders_text": leaders or None, "hard_charger": hc}
    return rows, meta


def parse_woo_table_feature(html_path: Path):
    """Parse flattened WoO results widget: POS Start +/- # Driver Laps Behind [Led] Status Points Money"""
    soup = BeautifulSoup(html_path.read_text(errors="replace"), "lxml")
    text = re.sub(r"\s+", " ", soup.get_text(" "))
    m = re.search(r"Feature Results.*?POS Start \+/- # Driver Laps Behind Led Status Points Money\s*", text)
    if not m:
        return [], {}
    rest = text[m.end():]
    rest = re.split(r"\s+(?:Qualifying|Heat|DASH|Dash|Last Chance|C-Main|B-Main|Micro-Lite|Event Info|Related)", rest, maxsplit=1)[0]
    pat = re.compile(
        r"(?P<pos>\d+)\s+(?P<start>\d+)\s+(?P<pm>[+\-]?\d+)\s+(?P<car>[A-Z0-9]+)\s+"
        r"(?P<driver>[A-Z][A-Za-z.'\-]+(?:\s+[A-Z][A-Za-z.'\-]+)+)\s+"
        r"(?P<laps>\d+)\s+(?P<behind>[+\-]?\d+\.\d+)\s+"
        r"(?:(?P<led>\d+)\s+)?(?P<status>Running|DNF|DNS|DQ)\s+"
        r"(?P<points>\d+)\s+\$(?P<money>[\d,]+)"
    )
    rows = []
    scheduled = None
    for mm in pat.finditer(rest):
        pos = int(mm.group("pos"))
        laps = int(mm.group("laps"))
        scheduled = scheduled or laps
        led = int(mm.group("led")) if mm.group("led") else None
        rows.append({
            "pos": pos,
            "start": int(mm.group("start")),
            "car": mm.group("car"),
            "driver": mm.group("driver"),
            "laps_completed": laps,
            "laps_led": led,
            "status": mm.group("status"),
            "time_or_margin": mm.group("behind") if pos != 1 else None,
            "points": int(mm.group("points")),
            "purse_usd": money_int(mm.group("money")),
            "hometown": None,
            "lap_leader_ranges": None,
        })
    # winner purse / total laps from header
    wm = re.search(r"Winner\s+(.+?)\s+Car Number\s*#(\S+)\s+Total Laps\s+(\d+)\s+Winner's Purse\s*\$?([\d,]+)", text)
    meta = {"scheduled_laps": int(wm.group(3)) if wm else scheduled}
    return rows, meta



def parse_woo_best(path, dtr=None):
    """Prefer the official WoO parse that yields the longer consecutive A-main.
    If DIRTRACKR rows are provided, prefer the parse that agrees on the first five."""
    a, ma = parse_woo_recap_feature(path)
    b, mb = parse_woo_table_feature(path)
    def consec(rows):
        if not rows or rows[0].get("pos") != 1:
            return []
        out=[]
        expect=1
        for r in rows:
            if r.get("pos")==expect:
                out.append(r); expect+=1
            else:
                break
        return out
    a, b = consec(a), consec(b)
    def agr(rows):
        if not dtr or not rows:
            return 0
        dmap={r["pos"]: r for r in dtr}
        n=0
        for r in rows[:5]:
            d=dmap.get(r["pos"])
            if d and norm_name(r.get("driver"))==norm_name(d.get("driver")):
                n+=1
        return n
    if dtr:
        aa, ab = agr(a), agr(b)
        if aa >= 3 or ab >= 3:
            if (aa, len(a)) >= (ab, len(b)):
                return a, ma
            return b, mb
        return ([], ma) if aa < 3 and ab < 3 else (a or b, ma)
    # no dtr: longer list
    if len(b) > len(a):
        return b, mb
    return a, ma

def parse_usac_feature(html_path: Path):
    soup = BeautifulSoup(html_path.read_text(errors="replace"), "lxml")
    text = re.sub(r"\s+", " ", soup.get_text(" "))
    m = re.search(r"FEATURE:\s*\((\d+) laps, starting positions in parentheses\)\s*", text, re.I)
    if not m:
        return [], {}
    laps = int(m.group(1))
    rest = text[m.end():]
    body, _, after = rest.partition("FEATURE LAP LEADERS:")
    if after:
        leaders = re.split(r"\s+FINAL USAC", after, maxsplit=1)[0].strip(" .")
    else:
        leaders = None
    rows = []
    for mm in re.finditer(r"(\d+)\.\s+([A-Z][^,(]+?)\s*\((\d+)(?:-P)?\)", body):
        rows.append({
            "pos": int(mm.group(1)),
            "driver": mm.group(2).strip(),
            "start": int(mm.group(3)),
            "car": None, "hometown": None, "status": None,
            "purse_usd": None, "laps_led": None, "lap_leader_ranges": None,
        })
    # parse leaders text like "Laps 1-13 Logan Seavey, Laps 14-17 Corey Day, Lap 21 Corey Day"
    return rows, {"scheduled_laps": laps, "lap_leaders_text": leaders}


def parse_tjs_amain(html_path: Path):
    soup = BeautifulSoup(html_path.read_text(errors="replace"), "lxml")
    text = re.sub(r"\s+", " ", soup.get_text(" "))
    m = re.search(r"(A-Main(?:\s*\(\d+\s*Laps\))?|Feature\s*\(\d+-Laps?\)|A Main(?:\s*\(\d+\s*Laps\))?)\s*:?\s*1\.\s*", text, re.I)
    if not m:
        return [], {}
    lm = re.search(r"(\d+)\s*-?\s*Laps?", m.group(1), re.I)
    laps = int(lm.group(1)) if lm else None
    rest = text[m.end()-3:]
    rest = re.split(r"\s+Latest News|\s+Grand Annual Sprintcar Classic|\s+Heat Race|\s+[A-Z][a-z]+ Reutzel Grand", rest, maxsplit=1)[0]
    rows = []
    for mm in re.finditer(
        r"(\d+)\.\s+([A-Z0-9]+)\s*[–-]\s*([A-Z][A-Za-z.'\-]+(?:\s+[A-Z][A-Za-z.'\-]+)+)",
        rest,
    ):
        car = mm.group(2)
        driver = mm.group(3).strip()
        # typo fixes for known OCR
        if driver.lower() == "corey mcgullagh":
            driver = "Corey McCullagh"
        if "Holdfield" in driver:
            driver = "Luke Holdsworth"  # uncertain - leave as published if typo not confirmed
            # actually "Q17 0 Luke Holdfield" was a typo in list; skip inventing. Keep Holdfield as published.
            driver = "Luke Holdfield"
        rows.append({
            "pos": int(mm.group(1)), "car": car, "driver": driver,
            "start": None, "hometown": None, "status": None,
            "purse_usd": None, "laps_led": None, "lap_leader_ranges": None,
        })
    return rows, {"scheduled_laps": laps}


def apply_leader_totals(rows, leaders_text):
    """If official has 'Larson 1-50' style text, fill winner/leader laps_led and ranges when blank."""
    if not leaders_text:
        return
    # map last-name (and some first initial) to ranges
    # "Pittman 1-10, J. Johnson 11, Pittman 12, Schatz 13-26"
    parts = re.split(r",\s*", leaders_text)
    acc = defaultdict(list)
    totals = defaultdict(int)
    for p in parts:
        p = p.strip().rstrip(".")
        p = re.sub(r"^(?:Laps?|Lap)\s+", "", p, flags=re.I)
        # "1-13 Logan Seavey" or "Logan Seavey 1-13" or "Pittman 1-10" or "21 Corey Day"
        m = re.match(r"(.+?)\s+(\d+)(?:-(\d+))?$", p)
        m2 = re.match(r"(\d+)(?:-(\d+))?\s+(.+)$", p)
        if m and not re.match(r"^\d", m.group(1)):
            name, a, b = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
        elif m2:
            a, b, name = int(m2.group(1)), int(m2.group(2) or m2.group(1)), m2.group(3)
        else:
            continue
        rng = f"{a}-{b}" if b != a else str(a)
        acc[name].append(rng)
        totals[name] += (b - a + 1)
    if not acc:
        return
    def key_for(nm):
        # last token of leader name
        bits = re.sub(r"\.", "", nm).strip().split()
        return bits[-1].lower() if bits else ""
    index = {}
    for r in rows:
        ln = norm_name(r.get("driver") or "").split()
        if ln:
            index.setdefault(ln[-1], []).append(r)
            # also first+last
            index.setdefault(" ".join(ln[-2:]), []).append(r)
    for nm, ranges in acc.items():
        last = key_for(nm)
        cands = index.get(last) or index.get(norm_name(nm)) or []
        # if first initial used (J. Johnson) and multiple Johnsons, skip assignment if ambiguous
        if len(cands) != 1:
            # try first initial
            fi = re.match(r"([A-Z])\.?\s+(\w+)$", nm)
            if fi:
                cands = [r for r in (index.get(fi.group(2).lower()) or []) if (r.get("driver") or "").lower().startswith(fi.group(1).lower())]
        if len(cands) == 1:
            r = cands[0]
            if not r.get("lap_leader_ranges"):
                r["lap_leader_ranges"] = ";".join(ranges)
            if r.get("laps_led") in (None,):
                r["laps_led"] = totals[nm]


def blank_to_none(v):
    if v is None or v == "":
        return None
    return v


CSV_FIELDS = [
    "result_id","event_id","event_name","edition","event_tier","date","night","track","city",
    "state_country","surface_length","series","class","session","session_label","scheduled_laps",
    "position","start","car_number","driver","driver_id","hometown","car_owner","laps_completed",
    "laps_led","lap_leader_ranges","status","time_or_margin","points","purse_usd","transfer",
    "source_url","source2_url","verified","flags","updated",
]


def merge_rows(official, dtr, event_meta, source_url, source2_url, extra_flags=""):
    """Match by position first, confirm driver; also detect driver mismatches."""
    def _agree(o, d):
        return bool(o and d and norm_name(o.get("driver")) == norm_name(d.get("driver")))
    # If both lists exist but the first five barely agree, the official parse likely grabbed the wrong block.
    if official and dtr:
        checks = []
        for pos in range(1, 6):
            o = next((r for r in official if r.get("pos")==pos), None)
            d = next((r for r in dtr if r.get("pos")==pos), None)
            checks.append(_agree(o, d))
        if checks and sum(checks) < 3:
            official = []
    dtr_by_pos = {r["pos"]: r for r in dtr}
    official_by_pos = {r["pos"]: r for r in official} if official else {}
    positions = sorted(set(official_by_pos) | set(dtr_by_pos))
    out = []
    for pos in positions:
        o = official_by_pos.get(pos)
        d = dtr_by_pos.get(pos)
        flags = []
        if extra_flags:
            flags.append(extra_flags)
        if o and d:
            no, nd = norm_name(o.get("driver")), norm_name(d.get("driver"))
            if no and nd and no != nd:
                flags.append(f"CONFLICT driver pos {pos}: official '{o['driver']}' vs source2 '{d['driver']}'")
                verified = False
            else:
                verified = True
            # start conflict
            if o.get("start") and d.get("start") and int(o["start"]) != int(d["start"]):
                flags.append(f"CONFLICT start pos {pos}: official {o['start']} vs source2 {d['start']}")
                verified = False
            # car conflict if both present
            if o.get("car") and d.get("car") and str(o["car"]).upper() != str(d["car"]).upper():
                flags.append(f"CONFLICT car pos {pos}: official {o['car']} vs source2 {d['car']}")
            driver = o.get("driver") or d.get("driver")
            car = o.get("car") or d.get("car")
            if o.get("car") is None and d.get("car"):
                flags.append("car number from source2 only")
            start = o.get("start") if o.get("start") is not None else d.get("start")
            hometown = o.get("hometown") or d.get("hometown")
            status = o.get("status") or d.get("status")
            purse = o.get("purse_usd") if o.get("purse_usd") is not None else d.get("purse_usd")
            laps_led = o.get("laps_led") if o.get("laps_led") is not None else d.get("laps_led")
            led_rng = o.get("lap_leader_ranges") or d.get("lap_leader_ranges")
            laps_comp = o.get("laps_completed") if o.get("laps_completed") is not None else d.get("laps_completed")
            points = o.get("points") if o.get("points") is not None else d.get("points")
            margin = o.get("time_or_margin") or d.get("time_or_margin")
        elif o:
            verified = False
            flags.append("single source (official only)")
            driver, car, start = o.get("driver"), o.get("car"), o.get("start")
            hometown, status, purse = o.get("hometown"), o.get("status"), o.get("purse_usd")
            laps_led, led_rng = o.get("laps_led"), o.get("lap_leader_ranges")
            laps_comp, points, margin = o.get("laps_completed"), o.get("points"), o.get("time_or_margin")
        else:
            # DTR only
            verified = False
            flags.append("single source (DIRTRACKR only; official full field not located this session)")
            driver, car, start = d.get("driver"), d.get("car"), d.get("start")
            hometown, status, purse = d.get("hometown"), d.get("status"), d.get("purse_usd")
            laps_led, led_rng = d.get("laps_led"), d.get("lap_leader_ranges")
            laps_comp, points, margin = d.get("laps_completed"), d.get("points"), d.get("time_or_margin")
        eid = event_meta["event_id"]
        rec = {
            "result_id": f"{eid}|A|{pos}",
            "event_id": eid,
            "event_name": event_meta["event_name"],
            "edition": event_meta.get("edition"),
            "event_tier": event_meta["event_tier"],
            "date": event_meta["date"],
            "night": event_meta.get("night") or "Finale",
            "track": event_meta["track"],
            "city": event_meta["city"],
            "state_country": event_meta["state_country"],
            "surface_length": event_meta.get("surface_length"),
            "series": event_meta.get("series"),
            "class": event_meta["class"],
            "session": "A-main",
            "session_label": event_meta.get("session_label") or "A-main",
            "scheduled_laps": event_meta.get("scheduled_laps"),
            "position": pos,
            "start": start,
            "car_number": car if car not in ("", None) else None,
            "driver": driver,
            "driver_id": slug(driver) if driver else None,
            "hometown": hometown or None,
            "car_owner": None,
            "laps_completed": laps_comp,
            "laps_led": laps_led,
            "lap_leader_ranges": led_rng,
            "status": status,
            "time_or_margin": margin,
            "points": points,
            "purse_usd": purse,
            "transfer": None,
            "source_url": source_url,
            "source2_url": source2_url,
            "verified": verified and bool(source_url and source2_url),
            "flags": "; ".join(flags) if flags else None,
            "updated": UPDATED,
        }
        out.append(rec)
    return out


# ---------- event builders ----------

def knox_edition(year):
    # 2016=56th ... 2019=59th; 2020 skipped; 2021=60th ... 2026=65th
    if year <= 2019:
        return year - 1960
    return year - 1961

def load_knox_official():
    data = json.loads(KNOX_JSON.read_text())
    out = {}
    for ys, rec in data.items():
        y = int(ys)
        if rec.get("not_held"):
            out[y] = {"not_held": True, "notes": rec.get("notes")}
            continue
        # convert date_text 'August 13, 2016'
        dt = rec.get("date_text")
        iso = None
        if dt:
            iso = dtdatetime.strptime(dt, "%B %d, %Y").date().isoformat()
        fins = []
        for f in rec.get("finishers") or []:
            hometown = f.get("hometown") or None
            if hometown:
                hometown = hometown.strip(" ,")
            fins.append({
                "pos": f["pos"], "start": f.get("start"), "car": f.get("car"),
                "driver": f.get("driver"), "hometown": hometown,
                "status": f.get("status"), "purse_usd": None,
                "laps_led": None, "lap_leader_ranges": None,
            })
        apply_leader_totals(fins, rec.get("lap_leaders"))
        out[y] = {
            "date": iso, "finishers": fins,
            "lap_leaders": rec.get("lap_leaders"),
            "hard_charger": rec.get("hard_charger"),
            "scheduled_laps": 50,
        }
    return out


def build_all():
    all_rows = []
    event_json = defaultdict(list)
    gaps = []
    conflicts = []

    # ===== Knoxville Nationals =====
    knox = load_knox_official()
    # 2016 cars: only #41 Johnson confirmed in WoO recap prose; leave others blank
    if 2016 in knox and knox[2016].get("finishers"):
        for f in knox[2016]["finishers"]:
            if f["driver"] == "Jason Johnson":
                f["car"] = "41"
                f["_car_note"] = "car 41 from WoO recap (Cajun-Style Upset); A-main list in official PDF omitted numbers"
    # typo flags
    typo_notes = {
        2017: "Official PDF lists Greg Hodnett hometown as Spring Grove, CA (other official years say PA).",
        2024: "Official PDF lists Brian Brown hometown as Grain Valley, CA (other official years say MO).",
        2021: "Official PDF lists Brooke Tatnell car as 0.",
    }
    names = {
        2016: "56th 5-hour ENERGY Knoxville Nationals presented by Casey's General Stores",
        2017: "57th 5-hour ENERGY Knoxville Nationals presented by Casey's General Stores",
        2018: "58th 5-hour ENERGY Knoxville Nationals presented by Casey's General Stores",
        2019: "59th NOS Energy Drink Knoxville Nationals presented by Casey's General Stores",
        2021: "60th NOS Energy Drink Knoxville Nationals presented by Casey's",
        2022: "61st NOS Energy Drink Knoxville Nationals presented by Casey's",
        2023: "62nd NOS Energy Drink Knoxville Nationals presented by Casey's",
        2024: "63rd NOS Energy Drink Knoxville Nationals presented by Casey's",
        2025: "64th NOS Energy Drink Knoxville Nationals presented by Casey's",
        2026: "65th NOS Energy Drink Knoxville Nationals presented by Casey's",
    }
    woo_2016 = WEB / "knox2016_woo.html"
    tjs_2026 = WEB / "knox2026_tjs.html"
    for y in range(2016, 2027):
        if y == 2020:
            gaps.append("Knoxville Nationals 2020: not held (COVID-19). Confirmed in official 2020 season PDF (no 50-lap Nationals A-main; recap: “We all wish it was Nationals.”). A mid-August WoO race at Knoxville was held but is not the Nationals.")
            continue
        official = knox[y]["finishers"]
        src1 = knox_pdf_url(y)
        src2 = None
        dtr_rows = []
        key = ("knoxville-nationals", y)
        if y == 2016 and woo_2016.exists():
            src2 = "https://worldofoutlaws.com/sprintcars/08-13-2016-knoxville-nationals/"
            dtr_rows, _ = parse_woo_recap_feature(woo_2016)  # reuse as source2 rows (same field shape)
        elif y == 2026:
            # dual: official PDF + TJS (full A-main) and also DTR
            src2 = "https://tjslideways.com/2026/08/16/larsons-flies-to-fourth-knoxville-nationals-title/"
            dtr_rows, _ = parse_tjs_amain(tjs_2026)
            # TJS list has starts in [n] form? our TJS parser may not have starts; DTR does
            if key in DTR_MAP:
                # prefer DTR for matching starts/purse; TJS already confirms order. Use DTR as source2 (TJS also agrees; cited in notes)
                # Keep TJS as source2 per session 1; merge DTR purse/laps into official via a pre-pass
                dtr2, _ = parse_dtr_feature(DTR / DTR_MAP[key][1])
                # copy purse/laps from dtr2 onto official when matching
                byp = {r["pos"]: r for r in dtr2}
                for f in official:
                    if f["pos"] in byp:
                        if f.get("purse_usd") is None:
                            f["purse_usd"] = byp[f["pos"]].get("purse_usd")
                        if f.get("laps_led") is None:
                            f["laps_led"] = byp[f["pos"]].get("laps_led")
                        if not f.get("lap_leader_ranges"):
                            f["lap_leader_ranges"] = byp[f["pos"]].get("lap_leader_ranges")
        elif key in DTR_MAP:
            rel, fn = DTR_MAP[key]
            src2 = DTR_URL.format(rel)
            dtr_rows, _ = parse_dtr_feature(DTR / fn)
        meta = {
            "event_id": f"{y}-knoxville-nationals",
            "event_name": names.get(y, f"Knoxville Nationals"),
            "edition": knox_edition(y),
            "event_tier": "crown_jewel",
            "date": knox[y]["date"],
            "night": "Finale",
            "track": "Knoxville Raceway",
            "city": "Knoxville",
            "state_country": "IA, USA",
            "surface_length": "1/2-mile dirt oval",
            "series": "World of Outlaws Sprint Car Series",
            "class": "410 sprint",
            "session_label": "A-main",
            "scheduled_laps": 50,
        }
        extra = typo_notes.get(y, "")
        if y == 2026:
            extra = (extra + " A-main finished after midnight Aug 16; program date Aug 15.").strip()
        if y == 2016:
            extra = (extra + " Official A-main list omitted car numbers except Johnson #41 (from WoO recap).").strip()
        rows = merge_rows(official, dtr_rows, meta, src1, src2, extra)
        all_rows.extend(rows)
        event_json["knoxville-nationals"].append({"year": y, "meta": meta, "rows": rows, "source_url": src1, "source2_url": src2})

    # ===== Kings Royal =====
    kr_official_files = {
        2016: (WEB / "kr2016_woo.html", "https://worldofoutlaws.com/sprintcars/7-16-2016-eldora-speedway/", "recap"),
        2017: (WEB / "kr2017_woo.html", "https://worldofoutlaws.com/sprintcars/donny-schatz-dominates-34th-kings-royal-at-eldora-speedway/", "recap"),
        2018: (WEB / "kr2018_eldora.html", "https://www.eldoraspeedway.com/event_coverage/35th-annual-kings-royal/", "recap"),
        # 2019 eldora page may be truncated; try recap parse then table
        2019: (WEB / "kr2019_eldora.html", "https://www.eldoraspeedway.com/event_coverage/36th-kings-royal-7-20-19/", "recap"),
        2021: (WEB / "kr2021_woo.html", "https://worldofoutlaws.com/sprintcars/7-17-21-37th-kings-royal-eldora-speedway/", "recap"),  # 37th Larson
        2022: (WEB / "kr2022_woo.html", "https://worldofoutlaws.com/sprintcars/king-brent-marks-completes-monumental-week-at-eldora-with-kings-royal-crown/", "recap"),
        2023: (WEB / "kr2023_woo.html", "https://worldofoutlaws.com/sprintcars/king-donny-xl-donny-schatz-triumphs-in-40th-kings-royal-for-sixth-crown/", "recap"),
        2024: (WEB / "kr2024_woo.html", "https://worldofoutlaws.com/sprintcars/results/?event=492726&series=sprintcars", "table"),
        2025: (WEB / "kr2025_woo.html", "https://worldofoutlaws.com/schedule/event-info/?event=4547729", "table"),
        2026: (WEB / "kr2026_woo.html", "https://worldofoutlaws.com/sprintcars/king-anthony-xliii-anthony-macri-makes-history-with-second-straight-eldora-kings-royal-crown/", "recap"),
    }
    kr_dates = {
        2016: "2016-07-16", 2017: "2017-07-15", 2018: "2018-07-14", 2019: "2019-07-20",
        2021: "2021-07-17", 2022: "2022-07-16", 2023: "2023-07-15", 2024: "2024-07-20",
        2025: "2025-07-19", 2026: "2026-07-18",
    }
    kr_ed = {2016: 33, 2017: 34, 2018: 35, 2019: 36, 2022: 39, 2023: 40, 2024: 41, 2025: 42, 2026: 43}
    kr_names = {
        2016: "33rd Kings Royal", 2017: "34th Kings Royal", 2018: "35th Kings Royal",
        2019: "36th Kings Royal", 2022: "39th Kings Royal", 2023: "40th Kings Royal",
        2024: "41st Kings Royal", 2025: "42nd Kings Royal", 2026: "43rd Kings Royal",
    }
    # 2020 not held
    gaps.append("Kings Royal 2020: not held in 2020 (COVID-19). Eldora ran two official Kings Royal A-mains on Saturday, July 17, 2021: the 37th (Kyle Larson) and the 38th (Tyler Courtney).")

    def kr_meta(y, event_id, name, edition, date, label="A-main", laps=40, extra_night="Finale"):
        return {
            "event_id": event_id, "event_name": name, "edition": edition,
            "event_tier": "crown_jewel", "date": date, "night": extra_night,
            "track": "Eldora Speedway", "city": "Rossburg", "state_country": "OH, USA",
            "surface_length": "1/2-mile dirt oval",
            "series": "World of Outlaws Sprint Car Series", "class": "410 sprint",
            "session_label": label, "scheduled_laps": laps,
        }

    # 2019: if recap parse fails, DTR only + try harder
    for y, (path, url, kind) in kr_official_files.items():
        if y == 2021:
            continue  # handled below
        dtr_rows, src2 = [], None
        key = ("kings-royal", y)
        if key in DTR_MAP:
            rel, fn = DTR_MAP[key]
            src2 = DTR_URL.format(rel)
            dtr_rows, _ = parse_dtr_feature(DTR / fn)
        official, meta_p = parse_woo_best(path, dtr_rows)
        apply_leader_totals(official, meta_p.get("lap_leaders_text"))
        laps = meta_p.get("scheduled_laps") or 40
        extra = ""
        if y == 2026:
            extra = "Scheduled 40 laps; 41 run (green-white-checkered) per World of Outlaws 2026 event table (session 1)."
            # keep scheduled_laps 40 as published schedule
        meta = kr_meta(y, f"{y}-kings-royal", kr_names[y], kr_ed[y], kr_dates[y], laps=40)
        if not official:
            gaps.append(f"Kings Royal {y}: official page fetched but feature list parse was empty; used DIRTRACKR only if available.")
        rows = merge_rows(official, dtr_rows, meta, url, src2, extra)
        all_rows.extend(rows)
        event_json["kings-royal"].append({"year": y, "meta": meta, "rows": rows, "source_url": url, "source2_url": src2})

    # 2021 double
    for key, path, url, name, edition, label in [
        (("kings-royal-37", 2021), WEB / "kr2021_woo.html",
         "https://worldofoutlaws.com/sprintcars/7-17-21-37th-kings-royal-eldora-speedway/",
         "37th Kings Royal", 37, "37th Kings Royal A-main"),
        (("kings-royal-38", 2021), WEB / "kr2021b_woo.html",
         "https://worldofoutlaws.com/sprintcars/shine-of-a-king-sunshine-tyler-courtney-claims-38th-kings-royal-in-first-appearance/",
         "38th Kings Royal", 38, "38th Kings Royal A-main"),
    ]:
        rel, fn = DTR_MAP[key]
        src2 = DTR_URL.format(rel)
        dtr_rows, _ = parse_dtr_feature(DTR / fn)
        official, meta_p = parse_woo_best(path, dtr_rows)
        apply_leader_totals(official, meta_p.get("lap_leaders_text"))
        eid = "2021-kings-royal-37th" if "37" in key[0] else "2021-kings-royal-38th"
        meta = kr_meta(2021, eid, name, edition, "2021-07-17", label=label, extra_night="Finale (twin Kings Royal, same date)")
        rows = merge_rows(official, dtr_rows, meta, url, src2, "Two official Kings Royal A-mains were run on July 17, 2021.")
        all_rows.extend(rows)
        event_json["kings-royal"].append({"year": 2021, "label": name, "meta": meta, "rows": rows, "source_url": url, "source2_url": src2})

    # ===== National Open =====
    no_files = {
        2016: (WEB / "no2016_woo.html", "https://worldofoutlaws.com/sprintcars/dietrich-with-dream-win-at-williams-grove/", "recap", "2016-10-01"),
        2017: (WEB / "no2017_woo.html", "https://worldofoutlaws.com/sprintcars/9-30-17-williams-grove-speedway-national-open-finale/", "recap", "2017-09-30"),
        2018: (WEB / "no2018_woo.html", "https://worldofoutlaws.com/sprintcars/lance-dewease-wins-emotional-williams-grove-national-open-worth-56-000/", "recap", "2018-09-29"),
        2019: (WEB / "no2019_woo.html", "https://worldofoutlaws.com/sprintcars/opening-a-dream-brent-marks-wins-the-national-open-at-williams-grove-speedway/", "recap", "2019-10-05"),
        2020: (WEB / "no2020_woo.html", "https://worldofoutlaws.com/sprintcars/10-3-20-williams-grove-speedway-national-open/", "recap", "2020-10-03"),
        2021: (None, None, "dtr-only-need-official", "2021-10-02"),
        2022: (WEB / "no2022_woo.html", "https://worldofoutlaws.com/sprintcars/not-done-yet-lance-dewease-banks-75000-with-fifth-career-national-open-title/", "recap", "2022-09-30"),
        2023: (WEB / "no2023_woo.html", "https://worldofoutlaws.com/sprintcars/marksman-brent-marks-hunts-down-pittman-for-second-williams-grove-national-open-triumph/", "recap", "2023-09-30"),
        2024: (WEB / "no2024_woo.html", "https://worldofoutlaws.com/sprintcars/results/?event=492687&series=sprintcars", "table", "2024-10-05"),
        2025: (WEB / "no2025_woo.html", "https://worldofoutlaws.com/schedule/event-info/?event=4547727", "table", "2025-10-04"),
        2026: (WEB / "no2026_woo.html", "https://worldofoutlaws.com/sprintcars/results/?event=597918&series=sprintcars", "table", "2026-10-03"),
    }
    # 2016 date: Dietrich article is dated Oct 14, 2016 about Friday night? "a late push Friday night" - NEED CARE
    # Champion Racing Oil National Open - historically Saturday. Article: "Friday night ended in a victory lane celebration" dated Oct 14, 2016.
    # 2016 National Open may have been postponed/run Friday Oct 14? Or the article typo.
    # I'll check article more carefully later; DTR didn't have 2016. Flag date if uncertain.
    no_ed = {2016: 54, 2017: 55, 2018: 56, 2019: 57, 2020: 58, 2021: 59, 2022: 60, 2023: 61, 2024: 62, 2025: 63, 2026: 64}
    no_names = {y: f"{no_ed[y]}th Champion Racing Oil / Williams Grove National Open" for y in no_ed}
    no_names[2024] = "WEIS Markets National Open presented by Sage Fruit"
    no_names[2025] = "J&S Classics National Open"
    no_names[2026] = "J&S Classics National Open"

    # Fix 2016 date from article if possible - leave as published event night; flag
    for y, (path, url, kind, iso) in no_files.items():
        official, meta_p = [], {}
        extra = ""
        if y == 2022:
            extra = "Championship National Open A-main ran Friday, Sept. 30, 2022 (no Saturday finale on DIRTRACKR or official recap)."
        if y == 2016:
            extra = "Official WoO recap describes the winning night as Friday (published Oct 14, 2016). Date recorded as 2016-10-01 pending a second date confirmation; field from official WoO feature list."
            # I'll try to find a better date from the recap body
        dtr_rows, src2 = [], None
        key = ("national-open", y)
        if key in DTR_MAP:
            rel, fn = DTR_MAP[key]
            src2 = DTR_URL.format(rel)
            dtr_rows, _ = parse_dtr_feature(DTR / fn)
        if path and path.exists() and kind != "dtr-only-need-official":
            official, meta_p = parse_woo_best(path, dtr_rows)
            apply_leader_totals(official, meta_p.get("lap_leaders_text"))
        if not official and not dtr_rows:
            gaps.append(f"National Open {y}: no feature list parsed.")
            continue
        if not official:
            gaps.append(f"National Open {y}: official full field not parsed this session; DIRTRACKR used as only full source.")
            url = url or src2
        meta = {
            "event_id": f"{y}-national-open",
            "event_name": no_names[y],
            "edition": no_ed[y],
            "event_tier": "crown_jewel",
            "date": iso,
            "night": "Finale",
            "track": "Williams Grove Speedway",
            "city": "Mechanicsburg",
            "state_country": "PA, USA",
            "surface_length": "1/2-mile dirt oval",
            "series": "World of Outlaws Sprint Car Series",
            "class": "410 sprint",
            "session_label": "A-main",
            "scheduled_laps": meta_p.get("scheduled_laps") or 40,
        }
        rows = merge_rows(official, dtr_rows, meta, url, src2, extra)
        all_rows.extend(rows)
        event_json["national-open"].append({"year": y, "meta": meta, "rows": rows, "source_url": url, "source2_url": src2})

    # ===== Chili Bowl =====
    chili_official = {
        2016: (WEB / "chili2016_press.html", "https://www.chilibowl.com/press/article/35471"),
        2017: (WEB / "chili2017_press.html", "https://www.chilibowl.com/press/article/43879"),
        2019: (WEB / "chili2019_official.html", "https://www.chilibowl.com/schedules/event/241617/media-results"),
        2020: (WEB / "chili2020_press.html", "https://www.chilibowl.com/press/article/80550"),
        2021: (WEB / "chili2021_press.html", "https://www.chilibowl.com/press/article/89299"),
        2022: (WEB / "chili2022_press.html", "https://www.chilibowl.com/press/article/103209"),
        2025: (WEB / "chili2025_press.html", "https://www.chilibowl.com/press/2025/article/165648"),
        2026: (WEB / "chili2026_press.html", "https://www.chilibowl.com/press/2026/article/185018"),
    }
    chili_dates = {
        2016: "2016-01-16", 2017: "2017-01-14", 2018: "2018-01-13", 2019: "2019-01-19",
        2020: "2020-01-18", 2021: "2021-01-16", 2022: "2022-01-15", 2023: "2023-01-14",
        2024: "2024-01-13", 2025: "2025-01-18", 2026: "2026-01-17",
    }
    # edition: 1987=1 so year-1986
    for y in range(2016, 2027):
        official, meta_p = [], {}
        url = None
        extra = ""
        if y in chili_official:
            path, url = chili_official[y]
            official, meta_p = parse_chili_afeature(path)
        else:
            extra = "Official Saturday results page with a full A-feature list was not located this session."
            gaps.append(f"Chili Bowl {y}: official full A-main list not located; DIRTRACKR used for the field. Winner confirmed on chilibowl.com/past-champions.")
        dtr_rows, src2 = [], None
        key = ("chili-bowl", y)
        if key in DTR_MAP:
            rel, fn = DTR_MAP[key]
            src2 = DTR_URL.format(rel)
            dtr_rows, _ = parse_dtr_feature(DTR / fn)
        laps = meta_p.get("scheduled_laps")
        if not laps and dtr_rows:
            # infer from leader ranges
            mx = 0
            for r in dtr_rows:
                if r.get("lap_leader_ranges"):
                    nums = [int(x) for x in re.findall(r"\d+", r["lap_leader_ranges"])]
                    if nums:
                        mx = max(mx, max(nums))
            laps = mx or (40 if y == 2025 else 55)
        if y == 2025:
            extra = (extra + " Official and DIRTRACKR both list a 40-lap Saturday A-feature (not the usual 55).").strip()
        meta = {
            "event_id": f"{y}-chili-bowl",
            "event_name": f"{y-1986}th Lucas Oil Chili Bowl Nationals",
            "edition": y - 1986,
            "event_tier": "crown_jewel",
            "date": chili_dates[y],
            "night": "Saturday championship",
            "track": "Tulsa Expo Raceway",
            "city": "Tulsa",
            "state_country": "OK, USA",
            "surface_length": "1/5-mile indoor dirt oval",
            "series": None,
            "class": "midget",
            "session_label": "Saturday A-main",
            "scheduled_laps": laps or 55,
        }
        # past champions as a weak official URL if no url
        if not url:
            url = "https://www.chilibowl.com/past-champions/"
            # only winner should be considered official from that page; keep flag
        rows = merge_rows(official, dtr_rows, meta, url, src2, extra)
        all_rows.extend(rows)
        event_json["chili-bowl"].append({"year": y, "meta": meta, "rows": rows, "source_url": url, "source2_url": src2})

    # ===== Australian Classic (Grand Annual Sprintcar Classic, Premier Speedway) =====
    # 2021 not held under Classic name (50 for Fifty)
    gaps.append("Australian Classic 2021: not run under the Grand Annual / Australian Classic name (replaced by the 50 for Fifty because of travel restrictions).")
    gaps.append("Australian Classic 2018: CONFLICT and gap. Wikipedia (citing MYLAPS Speedhive session 4719782, which did not load as a static page) lists Corey McCullagh as winner, Carson Macedo second, Brooke Tatnell third. The Standard (Warrnambool) headline says Grant Anderson won a delayed Saturday night Grand Annual Sprintcar Classic A-Main on Sunday, Jan. 21, 2018. Speedhive is a JavaScript app and was not readable without a browser. No full official field was entered for 2018.")
    aus_tjs = {
        2017: (WEB / "aus2017_tjs.html", "https://tjslideways.com/2017/01/22/j-mac-wins-the-classic/", "2017-01-21"),
        2020: (WEB / "aus2020_tjs.html", "https://tjslideways.com/2020/01/26/mcfadden-scores-second-career-grand-annual-sprintcar-classic-title/", "2020-01-26"),
        2026: (WEB / "aus2026_tjs.html", "https://tjslideways.com/2026/01/25/reutzel-wins-calamity-filled-classic-at-warrnambool/", "2026-01-25"),
    }
    wiki_top3 = {
        2016: [("Jamie Veal", 1), ("Kerry Madsen", 2), ("Robbie Farr", 3)],
        2017: [("James McFadden", 1), ("Darren Mollenoyux", 2), ("Brooke Tatnell", 3)],
        2019: [("Robbie Farr", 1), ("Jamie Veal", 2), ("Kerry Madsen", 3)],
        2020: [("James McFadden", 1), ("Jamie Veal", 2), ("Kerry Madsen", 3)],
        2022: [("Lachlan McHugh", 1), ("James McFadden", 2), ("Corey McCullagh", 3)],
        2023: [("Brock Hallett", 1), ("Sheldon Haudenschild", 2), ("Lachlan McHugh", 3)],
        2024: [("Aaron Reutzel", 1), ("Brock Hallett", 2), ("Lachlan McHugh", 3)],
        2025: [("James McFadden", 1), ("Cory Eliason", 2), ("Jamie Veal", 3)],
        2026: [("Aaron Reutzel", 1), ("Lachlan McHugh", 2), ("Brock Hallett", 3)],
    }
    wiki_url = "https://en.wikipedia.org/wiki/Grand_Annual_Sprintcar_Classic"
    # 2017 typo note: TJS lists V90 Corey McGullagh (recorded as published typo Corey McCullagh), Q17 Luke Holdfield as published
    for y in [2016, 2017, 2019, 2020, 2022, 2023, 2024, 2025, 2026]:
        official, url, iso, extra = [], None, None, ""
        if y in aus_tjs:
            path, url, iso = aus_tjs[y]
            official, meta_p = parse_tjs_amain(path)
            laps = meta_p.get("scheduled_laps") or 40
            if y == 2017:
                extra = "TJS feature list used as source 1; some published typographical issues (e.g. 'Corey McGullagh', 'Q17 0 Luke Holdfield', 'Jorydan Brazier') left as published or lightly normalized only for McGullagh→McCullagh."
        else:
            # top 3 only from Wikipedia, verified=false (tertiary) unless we had a second source
            official = [{"pos": pos, "driver": name, "car": None, "start": None, "hometown": None,
                         "status": None, "purse_usd": None, "laps_led": None, "lap_leader_ranges": None}
                        for name, pos in wiki_top3[y]]
            url = wiki_url
            laps = 40
            extra = "Only winner/top-3 from Wikipedia Grand Annual Sprintcar Classic page this session; official Premier Speedway/MYLAPS full fields not retrieved. Rows not marked verified."
            gaps.append(f"Australian Classic {y}: only Wikipedia top 3 located this session (no independent full A-main).")
            iso = None  # unknown exact date
        # second source: wiki top 3
        src2_rows = [{"pos": pos, "driver": name, "car": None, "start": None, "hometown": None,
                      "status": None, "purse_usd": None, "laps_led": None, "lap_leader_ranges": None}
                     for name, pos in wiki_top3.get(y, [])]
        src2 = wiki_url if url != wiki_url else None
        # if official is wiki, no independent source2
        if url == wiki_url:
            src2, src2_rows = None, []
        meta = {
            "event_id": f"{y}-australian-classic",
            "event_name": "Grand Annual Sprintcar Classic (Australian Classic)",
            "edition": y - 1972,  # 1973 first -> 2017=45th per TJS; 2017-1972=45. Yes.
            "event_tier": "crown_jewel",
            "date": iso,  # may be None
            "night": "Finale",
            "track": "Premier Speedway",
            "city": "Warrnambool",
            "state_country": "Victoria, Australia",
            "surface_length": None,
            "series": None,
            "class": "410 sprint",
            "session_label": "A-main",
            "scheduled_laps": laps,
        }
        if not iso:
            extra = (extra + " Exact local date not confirmed this session; date field left blank.").strip()
        rows = merge_rows(official, src2_rows, meta, url, src2, extra)
        all_rows.extend(rows)
        event_json["australian-classic"].append({"year": y, "meta": meta, "rows": rows, "source_url": url, "source2_url": src2})

    # ===== Turkey Night 2025 =====
    usac_path = WEB / "tngp2025_usac.html"
    official, meta_p = parse_usac_feature(usac_path)
    apply_leader_totals(official, meta_p.get("lap_leaders_text"))
    rel, fn = DTR_MAP[("turkey-night", 2025)]
    src2 = DTR_URL.format(rel)
    dtr_rows, _ = parse_dtr_feature(DTR / fn)
    meta = {
        "event_id": "2025-turkey-night",
        "event_name": "84th ARP Turkey Night Grand Prix presented by The West Coast Stock Car/Motorsports Hall of Fame",
        "edition": 84,
        "event_tier": "major",
        "date": "2025-11-29",
        "night": "Finale",
        "track": "Ventura Raceway",
        "city": "Ventura",
        "state_country": "CA, USA",
        "surface_length": None,
        "series": "USAC National Midget",
        "class": "midget",
        "session_label": "A-main",
        "scheduled_laps": 98,
    }
    extra = "Car numbers not published in the USAC recap results block or DIRTRACKR feature table; left blank. FloRacing second recap URL returned HTTP 406 without a browser."
    rows = merge_rows(official, dtr_rows, meta,
                      "https://www.usacracing.com/news/turkey-night-grand-prix-results-nov-29-2025",
                      src2, extra)
    all_rows.extend(rows)
    event_json["turkey-night"].append({"year": 2025, "meta": meta, "rows": rows,
        "source_url": "https://www.usacracing.com/news/turkey-night-grand-prix-results-nov-29-2025",
        "source2_url": src2})

    # collect conflicts from flags
    for r in all_rows:
        if r.get("flags") and "CONFLICT" in r["flags"]:
            conflicts.append(f"{r['event_id']} P{r['position']}: {r['flags']}")

    return all_rows, event_json, gaps, conflicts


def write_outputs(all_rows, event_json, gaps, conflicts):
    OUT_DATA.mkdir(parents=True, exist_ok=True)
    # CSV
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in all_rows:
            row = dict(r)
            # booleans as true/false
            row["verified"] = "true" if r["verified"] else "false"
            for k in CSV_FIELDS:
                if row.get(k) is None:
                    row[k] = ""
            w.writerow({k: row[k] for k in CSV_FIELDS})

    # per-event JSON (schema-aligned, without internal keys)
    name_map = {
        "knoxville-nationals": "knoxville-nationals.json",
        "kings-royal": "kings-royal.json",
        "national-open": "national-open.json",
        "chili-bowl": "chili-bowl.json",
        "australian-classic": "australian-classic.json",
        "turkey-night": "turkey-night.json",
    }
    for key, fn in name_map.items():
        payload = {
            "updated": UPDATED,
            "event": key,
            "races": event_json.get(key, []),
        }
        # strip huge duplication? keep rows
        (OUT_DATA / fn).write_text(json.dumps(payload, indent=2, ensure_ascii=False))

    # summary stats
    stats = defaultdict(lambda: defaultdict(lambda: {"rows": 0, "verified": 0}))
    for r in all_rows:
        ev = r["event_id"]
        # event family
        fam = re.sub(r"^\d{4}-", "", ev)
        fam = re.sub(r"-3[78]th$", "", fam)
        year = ev[:4]
        stats[fam][year]["rows"] += 1
        if r["verified"]:
            stats[fam][year]["verified"] += 1

    summary = {"total_rows": len(all_rows), "verified": sum(1 for r in all_rows if r["verified"]),
               "by_event": {k: dict(v) for k, v in stats.items()},
               "gaps": gaps, "conflicts": conflicts}
    (ROOT / "raw" / "parsed" / "session2_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    return summary


if __name__ == "__main__":
    rows, evj, gaps, conflicts = build_all()
    summary = write_outputs(rows, evj, gaps, conflicts)
    print("ROWS", summary["total_rows"], "VERIFIED", summary["verified"])
    print("BY EVENT")
    for ev, years in summary["by_event"].items():
        for y, st in sorted(years.items()):
            print(f"  {ev} {y}: {st['rows']} rows, {st['verified']} verified")
    print("\nGAPS:")
    for g in gaps:
        print("-", g)
    print("\nCONFLICTS:", len(conflicts))
    for c in conflicts[:40]:
        print("-", c)
