[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/thanhvu261090/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/thanhvu261090/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>

# The World Today — Wednesday 18 November 2026

My entry for the [make.fun](https://make.fun/bounty/news-image-20261118) bounty
**"Sum up 18 November's world news in one image"**: one front page that sums
up the day's world news, drawn programmatically with Pillow so every headline
is spelled correctly and legible at 1024×1024.

## What's on the page

All stories happened, or were first reported, on Wednesday 18 November 2026,
checked against that day's wire reporting:

- **Lead — Ukraine strikes the Crimean Bridge.** A major combined
  missile-and-drone attack damages the Kerch Strait crossing; Moscow opens a
  terrorism probe and pounds bridges around Kyiv as trilateral talks near.
- **Middle East — Iran hits a US radar base in Bahrain with drones.**
  The Revolutionary Guard claims the strike on the radar at Sheikh Isa Air
  Base, the third attack on the country in five days.
- **Asia diplomacy — Trump and Modi give the Quad a new direction in Manila.**
  A new maritime exercise and joint work on AI and cybersecurity, as the
  ASEAN summit closes with key declarations.
- **Tech — Nvidia beats estimates without Huang.** First earnings since the
  chief executive resigned; the board rules out his return.
- **Russia — Military plane crashes in Siberia; 19 killed.**
- **Sport — Dhoni retires from the IPL**, returning to Chennai Super Kings
  as mentor.
- **Also today:** the US loses measles-free status as cases mount;
  Mongolia's president resigns amid graft charges; China sacks a scientist
  after a 6-year-old dies in a gene-editing trial.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` — the
front page rendered in this repository — to `/output/entry.png`
(`MAKEFUN_OUTPUT_DIR` stands in for `/output` outside the grader). No
network is used, and both runs write exactly the same bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `entry.png` — the 1024×1024 front page (140,726 bytes)
- `main.py` — the entrypoint, standard library only
- `LICENSE` — MIT
