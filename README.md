[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/SARIP-afk/gta6-meme-x-01-entry/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/SARIP-afk/gta6-meme-x-01-entry/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

# gta6-meme-x-01 — "The Download"

A GTA 6 meme for the Make.fun bounty **gta6-meme-x-01** ($500, top 50 paid).
The entry is a post on X: the first image of the post is the meme, and the
post text carries the make.fun link, the @makefunai tag, and the account's
play code.

## The memes

All three are original, square 1024x1024 PNGs in `memes/`. The make.fun
ghost (chubby white ghost, thick black outline, four-point sparkle eyes,
holding a magenta coin with a white star) is drawn into each scene — never
pasted as a corner sticker.

| File | Concept | Caption on the image |
| --- | --- | --- |
| `memes/meme-v1.png` | **THE DOWNLOAD (main)** — a ghost naps on the sofa while the TV shows the GTA VI download stuck at 2%, "47 HOURS REMAINING" | WAITED 13 YEARS FOR GTA 6. / NOW I WAIT 47 MORE HOURS. / my agent earns on make.fun while I wait |
| `memes/meme-v2.png` | **THE SAVINGS** — a piggy bank overflowing with magenta coins; the ghost counts a stack on the table | SAVED $5 A MONTH FOR GTA 6 SINCE 2013. / GAME: $70. MY AGENT EARNED THE REST ON MAKE.FUN. |
| `memes/meme-v3.png` | **THE CASHIER** — the ghost is the cashier at LEONIDA GAMES, reaching for the customer's magenta coin | FINALLY AT THE COUNTER. / THE CASHIER IS A GHOST. HE ONLY TAKES MAGENTA COINS. |

Only **one** image is posted (v1, the main entry). V2 and V3 are alternates
kept in the repo in case the poster prefers a different joke.

## How the images were made

1. Each scene was generated with an image model **without any text**.
2. The ghost, the caption text, the TV progress bar, and the shop sign were
   drawn on top with PIL (`memes/build_memes.py`, Liberation Sans Bold with
   a thick black stroke) so every word is spelled correctly and stays
   readable when the judge views the image at 480px.
3. Each variant was checked at 480x480 and 300x300 (`memes/check-*-480.png`,
   `memes/check-*-300.png`): captions stay legible and the ghost stays
   recognizable at both sizes.

## How to post

See `POSTING.md` — it has the exact caption, the link, and the play code to
include. After posting, replace the placeholder URL in `POST.json` with the
real post URL (`https://x.com/<handle>/status/<id>`) and submit this repo.

## Submission files

- `main.ts` — copies `POST.json` into the output directory
  (`MAKEFUN_OUTPUT_DIR`, default `/output`).
- `POST.json` — the X post URL (placeholder until the post is live).
- `POSTING.md` — posting instructions.
- `LICENSE` — MIT.

## License

MIT — see `LICENSE`.
