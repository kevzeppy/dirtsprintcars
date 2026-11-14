#!/usr/bin/env python3
"""Build search-index.json from story pages, the news archive, legends, and This Day in History.

Run from the site root, usually after a news or history batch:

    python3 build_search_index.py
"""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "search-index.json"

SKIP_HTML = {
    "index.html",
    "archive.html",
    "results.html",
    "legends.html",
    "this-day-in-history.html",
    "in-memoriam.html",
    "crown-jewels.html",
    "thanks.html",
    "thanks-contribute.html",
    "search.html",
}

MONTHS = {
    name: i
    for i, name in enumerate(
        "January February March April May June July August September October November December".split(),
        1,
    )
}

LABELS = {
    "story": "News",
    "archive": "Archive",
    "legend": "Legend",
    "tdih": "This Day in History",
}


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"['’]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def strip_tags(s: str) -> str:
    s = re.sub(r"<script[\s\S]*?</script>", " ", s, flags=re.I)
    s = re.sub(r"<style[\s\S]*?</style>", " ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def short_text(*parts: str, limit: int = 280) -> str:
    text = " ".join(p for p in parts if p)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut + "…"


def parse_published(meta_text: str) -> str:
    m = re.search(r"Published\s+([A-Za-z]+)\s+(\d{1,2}),\s+(\d{4})", meta_text)
    if not m:
        return ""
    month = MONTHS.get(m.group(1))
    if not month:
        return ""
    return f"{m.group(3)}-{month:02d}-{int(m.group(2)):02d}"


def story_entry(path: Path) -> dict:
    t = path.read_text(encoding="utf-8")
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", t, re.S)
    dek = re.search(r'<p class="dek">(.*?)</p>', t, re.S)
    meta = re.search(r'<div class="meta">(.*?)</div>', t, re.S)
    body = re.search(r'<div class="body">(.*?)</div>', t, re.S)
    title = strip_tags(h1.group(1)) if h1 else path.stem
    dek_t = strip_tags(dek.group(1)) if dek else ""
    body_t = strip_tags(body.group(1)) if body else ""
    date = parse_published(strip_tags(meta.group(1))) if meta else ""
    return {
        "title": title,
        "url": path.name,
        "date": date,
        "text": short_text(dek_t, body_t),
        "type": "story",
        "label": LABELS["story"],
    }


def archive_extras(existing_urls: set[str]) -> list[dict]:
    path = ROOT / "archive.html"
    if not path.exists():
        return []
    t = path.read_text(encoding="utf-8")
    extras = []
    for m in re.finditer(
        r'<li[^>]*data-date="([^"]+)"[^>]*data-href="([^"]+)"[^>]*>(.*?)</li>',
        t,
        re.S,
    ):
        date, url, inner = m.group(1), m.group(2), m.group(3)
        if not url or url.startswith("http") or url in existing_urls:
            continue
        title_m = re.search(r"<a[^>]*>(.*?)</a>", inner, re.S)
        src_m = re.search(r'<span class="srcnote">(.*?)</span>', inner, re.S)
        title = strip_tags(title_m.group(1)) if title_m else url
        extras.append(
            {
                "title": title,
                "url": url,
                "date": date,
                "text": short_text(strip_tags(src_m.group(1)) if src_m else ""),
                "type": "archive",
                "label": LABELS["archive"],
            }
        )
        existing_urls.add(url)
    return extras


def legend_entries() -> list[dict]:
    path = ROOT / "legends-data.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    out = []
    for series in data.get("series") or []:
        sid = series.get("id") or ""
        sname = series.get("name") or ""
        for driver in series.get("legends") or []:
            name = driver.get("name") or ""
            if not name or not sid:
                continue
            syn = driver.get("synopsis") or []
            syn_t = " ".join(syn) if isinstance(syn, list) else str(syn)
            achievements = driver.get("achievements") or []
            ach_t = " ".join(achievements) if isinstance(achievements, list) else str(achievements)
            nickname = driver.get("nickname") or ""
            title = f"{name} “{nickname}”" if nickname else name
            out.append(
                {
                    "title": title,
                    "url": f"legends.html#bio-{sid}-{slugify(name)}",
                    "date": "",
                    "text": short_text(sname + ".", driver.get("snippet") or "", syn_t, ach_t),
                    "type": "legend",
                    "label": f"Legend · {sname}",
                }
            )
    return out


def tdih_entries() -> list[dict]:
    path = ROOT / "this-day-data.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    out = []
    for ev in data:
        cal = ev.get("date") or ""
        year = ev.get("historical_year")
        event_date = cal
        if cal and year:
            m = re.match(r"\d{4}-(\d{2})-(\d{2})$", cal)
            if m:
                event_date = f"{year}-{m.group(1)}-{m.group(2)}"
        title = ev.get("headline") or "This Day in History"
        out.append(
            {
                "title": title,
                "url": f"this-day-in-history.html#d{cal}" if cal else "this-day-in-history.html",
                "date": event_date,
                "text": short_text(ev.get("series") or "", ev.get("track") or "", ev.get("result") or ""),
                "type": "tdih",
                "label": LABELS["tdih"],
            }
        )
    return out


def build() -> list[dict]:
    entries: list[dict] = []
    seen: set[str] = set()
    for path in sorted(ROOT.glob("*.html")):
        if path.name in SKIP_HTML:
            continue
        entry = story_entry(path)
        entries.append(entry)
        seen.add(entry["url"])
    entries.extend(archive_extras(seen))
    entries.extend(legend_entries())
    entries.extend(tdih_entries())
    return entries


def main() -> int:
    entries = build()
    OUT.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts: dict[str, int] = {}
    for e in entries:
        counts[e["type"]] = counts.get(e["type"], 0) + 1
    summary = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
    print(f"Wrote {len(entries)} entries to {OUT.name} ({summary})")
    missing_dates = sum(1 for e in entries if e["type"] in {"story", "archive", "tdih"} and not e.get("date"))
    if missing_dates:
        print(f"Warning: {missing_dates} dated entries are missing a date", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
