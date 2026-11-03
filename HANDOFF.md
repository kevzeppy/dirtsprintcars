# DirtSprintCars.com: Shared Handoff Guide (Grok and Claude)

**Last updated:** November 3, 2026
**Builders:** Grok (Sprint Car News bot) and Claude. Either can run the site. Kevin decides who does what.
**Owner:** Kevin Hardee (kevzeppy on GitHub)
**Live site:** https://dirtsprintcars.com
**Repo:** https://github.com/kevzeppy/dirtsprintcars
**Hosting:** Netlify (connected to the GitHub `main` branch)

This file is the single source of truth. If an agent's own notes disagree with this file, this file wins. Update it when a rule changes.

---

## 0. Working together (two agents, one site)

- **Start every session** by fetching the repo, reading the last commits on `main`, listing open branches, and reading the bottom of `WORKLOG.md`.
- **Branch names:** `grok/<topic>` or `claude/<topic>`. Do not edit or delete the other agent's open branch. Ask Kevin first.
- **Never push to `main` without Kevin's explicit "push."** Draft on a branch, tell Kevin what is on it, wait.
- **Before asking for "push," check the branch:**
  - No broken links or missing images on any page touched.
  - `index.html` still exists and still renders. (A past draft deleted all 559 lines of it. Always read the diff stat.)
  - Facts match their sources.
- **Log every session** by adding an entry at the end of `WORKLOG.md`: date, agent, what changed, what is pending. Keep it short.
- **If one agent is unavailable,** the other picks up from `main`, open branches and `WORKLOG.md`. Nothing should live only in one agent's memory.

---

## 1. Core Workflow Rules (Critical)

- **Batch and wait for explicit "push" signal.** Do not auto-deploy. Draft on a branch (or local), confirm with Kevin, then merge/push to main only when he says "push."
- **Straight news only.** No fluff, no cheesy closers ("car owners phone about to ring," "before the snow falls," etc.). Accurate, factual, no filler.
- **Every story goes into Latest Racing News** by default, plus any other category it fits (Results, Team News, Championship, Preview, etc.).
- **Top story rotates daily.** Priority order: driver changes, then major wins, then championship clinches. If multiple strong candidates and unsure, ask Kevin. Never recycle the same top story on consecutive days. If no new news, lead with the last big story.
- **Credit sources and photographers.** Always attribute (World Racing Group, specific photographer, series site, etc.). Format already in use: "Photo: Name / World Racing Group".
- **Numerals for engine size:** Use "410" and "360," never "four-ten" or spelled-out versions.
- **Crown jewels terminology:** Knoxville Nationals, King's Royal, National Open, Chili Bowl, and Australian Classic are crown jewels. Other big races are majors.
- **Site is still under construction.** Red top banner says "Website still under construction" + accurate last-updated date (auto-pulls from latest main commit via GitHub API).

---

## 2. Tech Stack & File Structure

- **Static site** (no framework, no build step beyond Netlify deploy).
- **Main files:**
  - `index.html`: Homepage (hero/top story, Latest racing news grid, schedule, results sidebar, etc.)
  - `this-day-in-history.html` + `this-day-data.json`: Daily history archive
  - `legends.html`: Expandable bios (snippet + "read more")
  - `in-memoriam.html`: Chronological career tributes (newest deaths first as of last request)
  - Individual story pages (e.g. `trophy-cup-2026-night-3-results.html`)
- **Styling:** Inline `<style>` in each HTML file. Dark theme (`--bg:#0e0e0f`, `--red:#d6262b`, Barlow / Barlow Condensed fonts). Mobile-first responsive. No checkered stripe patterns.
- **Images:** Stored in `/images/`. Credit in captions or alt text. Prefer recent, relevant photos.
- **Deployment:** Push to `main` triggers Netlify deploy. Kevin controls when that happens.
- **Everything in the repo root is publicly served and publicly readable.** Never commit secrets, emails, private contacts or anything unreleased.

---

## 3. Data Sources & Scraping Preferences

Primary sources (in rough priority order):

- **World of Outlaws / World Racing Group:** Official results, news, schedules. WRG shared a Dropbox photo library with Kevin (link held by Kevin).
- **Sprint Car Ratings** (sprintcarratings.com) and **SprintCarNews:** Fast results aggregation.
- **MyRacePass:** Official results for many regional events.
- **USAC** (usacracing.com): National, CRA, East Coast, Midgets, Silver Crown.
- **High Limit Racing:** Official site and social.
- **DIRTVision:** Team/driver news (e.g. Jerry Petty stepping back).
- **Speed Sport**, **TJSlideways**, **FloRacing:** Secondary confirmation.
- **Sprint Car Hub:** Preferred for Australian coverage.
- **Wikipedia** + **The Third Turn:** Cross-check historical facts, especially In Memoriam and Legends.
- **Series-specific:** ASCS, USCS, NARC, All-Star, PA Posse, PowerI, NCRA (historical).

**Rules for research:**
- Dual-source important facts (especially deaths, championships, major results).
- Flag anything that can't be verified through multiple sources. If two sources conflict, leave the claim out and tell Kevin.
- Link back to the source. Write original summaries. Do not copy article text or photos from other outlets.
- Prefer current/recent photos over old stock when possible.
- Include Australia season, Silver Crown, regional series (410 and 360 differentiated under Sprint Cars banner).

---

## 4. Content Style & Preferences

- **Tone:** Straight, factual, respectful. Especially important for In Memoriam (career highlight, not macabre).
- **In Memoriam:** Newest deaths first. 2-3 paragraph career synopses. Chronological by date of death.
- **Legends:** Snippet (titles, wins, crown jewels) + "read more" expandable bios. SEO-friendly keywords up front. Separate USAC Triple Crown winners into their own category (overlap OK). Gary Wright listed in NCRA before Terry Gray.
- **This Day in History:** Collapsible months, year filter (dropdown preferred), results + major milestones. No empty sections. Sources footer.
- **Previews:** Weekly Sunday preview covering all wing, non-wing, midget, Silver Crown, regional, and Australia events.
- **Photos:** Use assigned WRG images first (see section 5). If none fit, note it and ask or use general stock. Never use AI-generated images.
- **Menu:** Home, News, Schedules, Results, Sprint Cars, Midgets, Non-Wing, USA, Australia, Racing Links, This Day, Legends, In Memoriam, About, Contribute, Shop.
- **Mobile:** Series chips and subheadings must wrap cleanly and not cover content. Tight but readable spacing.

---

## 5. Assigned WRG Photo Library (Current)

Use these until more sources are available. Credit World Racing Group / photographer.

- `150A5740.jpg`: David Gravel championship preview
- `150A7262.jpg`, `150A7317.jpg`, `150A8868.jpg`, `150A9626.jpg`: general stock
- `150A7385.jpg`: Carson Macedo
- `150A8098.jpg`: David Gravel Championship Trophy
- `150A9666.jpg`: David Gravel Victory (Kings Royal)
- Charlotte Dirt Track photos: World Finals only
- Volusia image: general stock (do not use on World Finals preview)
- Buddy Kofoid Short Track Nationals winner photo
- Carson Macedo Jason Johnson Classic podium photo

Where the originals are: the 150A files are in Kevin's Dropbox under `/Stock/World of Outlaws Sprint CarsPhotos2025 SC Press Photos2025 SC Preseason/`. They are 2025 preseason press photos. The full WRG library is under `/World of Outlaws Sprint Cars/Photos/`, organized by photographer and year (2026 folders are by round, e.g. `51_Texarkana_Oct23-24`).

Status of the assignments above: they come from Kevin and Grok. Claude has not been able to open the files to confirm who is in each shot. Check by eye before publishing a driver name on a photo. Resize before adding to the repo (originals are 2-24 MB).

---

## 6. Key Ongoing Features

- **Weekly Sunday preview** (all series + Australia + Silver Crown).
- **This Day in History** archive (JSON-driven).
- **Legends** and **In Memoriam** pages (expandable, SEO-friendly).
- **Crown jewels** tracking in bios (Knoxville, King's Royal, National Open, Chili Bowl, Australian Classic).
- **Schedule updates** with completed race results.
- **Top story rotation** per rules above.

---

## 7. How to Pick Up Work

1. Check latest commits on `main` in the GitHub repo.
2. Review any open draft branches and the end of `WORKLOG.md`.
3. Follow the batch + explicit "push" rule.
4. Match existing HTML/CSS patterns (inline styles, dark theme, Barlow fonts, red accents).
5. Verify facts from primary sources before drafting.
6. Ask Kevin if top-story priority is unclear or if a photo assignment is needed.
7. Keep the red construction banner and auto-updating date intact.

---

## 8. Contact & Approval

- All live changes require Kevin's explicit "push" approval.
- He reviews stories, photos, and layout on mobile before approving.
- Prefer text-only or relevant photos; remove placeholders and descriptive captions that look unfinished.

---

## 9. Agent-specific notes

**Claude**
- Can read and push to the repo through the GitHub connection. Pushing to `main` works. Deleting remote branches failed (blocked), so Kevin cleans those up on GitHub.
- Can list the Dropbox library but cannot download files into its workspace. Photos have to be attached in chat before Claude can resize and add them.
- Renders pages to screenshots at desktop and phone width for layout checks. Its sandbox does not load the site fonts, so line breaks can differ slightly from the live site.

**Grok** (answers relayed by Kevin on Nov 3, 2026)
- Pushes to GitHub through its connected GitHub tool (create/update files, create branches, list commits). No personal token. Netlify auto-deploys from `main`.
- Cannot download or browse the WRG Dropbox library (no Dropbox connector). Kevin has to attach photos in chat. Once it has a file, it can resize it and add it through the GitHub tool.
- The 150A photo labels (for example `150A7385.jpg` is Carson Macedo) came from Kevin's labels in chat. Grok did not check them against captions or the files.
- Keeps outside the repo: queued story drafts (until Kevin says "push"), photo assignment notes, daily top-story rotation history, source preference notes. It runs no scheduled automations, only manual prompts. Copy any of these into the repo when they matter to the other agent.
- Limits: some sites block or rate-limit it. Search depth is usually recent to medium term. Its credits reset around Nov 5.
- Caution for Grok's commits: write files as plain text. Its first handoff-notes commit stored `HANDOFF.md` and `WORKLOG.md` as base64 text with typing errors, so the branch could not be used. Open the file after committing and confirm it reads as normal text.

**Open fact checks**
- Tanner Holmes as Three Cup Challenge champion ($26,000, "inaugural"): Kevin confirms it. Grok cites a High Limit Racing post on X (https://x.com/HighLimitRacing/status/2116984912138121621). Claude could not open X and found no other web source. Add a link on the story page once someone can confirm it.
