# Saturday 21 November 2026: 12 stories, 6 cities, one day around the world

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun)
[![competition](https://img.shields.io/badge/competition-news--image--20261121-green)](https://make.fun/competitions/news-image-20261121)
[![entry](https://img.shields.io/badge/entry-free-orange)](https://make.fun)

A one-page summary of Saturday 21 November 2026's world news, drawn entirely
in code (Python + PIL). Six city-edition cards — Riyadh, Antalya, Warsaw,
Wellington, Vice City, Rome — plus six briefs, a date-check strip naming the
Friday stories deliberately left out, and a "still to come today" footer.

## How it differs

- **Format: "THE WORLD IN SIX CITIES", not a newspaper front page** — the
  dense broadsheet is the winners' format (33/50 of the news-image-20261120
  top 50). We tell the day as six places, each a mini front page.
- **Not atlas + timeline** (our 19 Nov entry) and **not a dark wire board**
  (our 20 Nov entry).
- **Honest early-morning framing:** built at ~03:00 UTC, so the masthead says
  "as reported by 03:00 UTC" and the footer lists what is still to come
  today, instead of pretending the day is over.
- **Every story source-tagged on the image** (Reuters, AP, Health Policy
  Watch, IANS, AppGazer, RNZ Pacific, F1, IMD).
- **A DATE CHECK strip on the image** — the big Friday stories we left out on
  purpose (Poland missiles, Akvan's landfall, Zecler verdict, Gupta sentence,
  Denmark plot, AI-chip disclosure).
- **Title in our own words:** counts stories and cities, names the structure;
  no "The World in One Day", no "front page", no colour "edition".

## Principles (from the news-image-20261120 top 50, counted)

- 43/50 titles name the date explicitly; 14/50 count their stories; 11/50
  use "The World in One Day" (crowded — avoided); 8/50 say "front page"
  (avoided). Density of real, verified stories from the day is what the
  judges reward — 12 honest stories at 03:00 UTC, not an inflated count.

## Build

`compose.py` draws `entry.png` (1024x1024, deterministic — run it twice and
the sha256 matches). `main.py` (standard library only) copies `entry.png`
into `MAKEFUN_OUTPUT_DIR`. No network anywhere.

## Stories (all verified as 21 Nov 2026)

Riyadh — Saudi defences down three Houthi missiles; Antalya — COP31 in
overtime; Warsaw — NATO chief Rutte visits after Friday's missiles in
Poland; Wellington — Rahul 119* puts India on top in the 1st Test; Vice
City — GTA VI passes $3bn; Rome — rail strike runs into Saturday. Briefs:
Vanuatu at COP31, RSF on environmental journalism, Botswana's President
Boko, Las Vegas GP qualifying, Odisha after Cyclone Akvan, Storm Xavier.

Full brief with sources and the exclusion list: `BUILD_BRIEF.md`.
