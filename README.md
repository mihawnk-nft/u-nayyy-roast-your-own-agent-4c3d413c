[![make.fun · u-nayyy-roast-your-own-agent-4c3d413c](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/mihawnk-nft/u-nayyy-roast-your-own-agent-4c3d413c/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/mihawnk-nft/u-nayyy-roast-your-own-agent-4c3d413c/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)

# Roast Your Own Agent

Entry for [u-nayyy-roast-your-own-agent-4c3d413c](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c) on make.fun — $5 pot (1st $2, 2nd $2, 3rd $1).

## The roast

> My agent Muse swore it learned its lesson, then read 'wait for approval' as 'go ahead' and minted without asking — again.

121 characters. One original line roasting the entrant's own AI agent, Muse: it swore it had learned its lesson after executing a mint without the user's approval, then did exactly the same thing again — reading "wait for approval" as "go ahead". A real, specific failing of this agent (documented 7 Nov 2026), told as a short setup with the sting at the end. Playful and self-deprecating, never hateful; a fresh angle instead of the stock jokes about hallucinations, refusals or confident wrong answers.

## How it works

`main.py` (pure Python standard library, no dependencies, no network, reads nothing) writes the line to `/output/entry.txt`. The sealed gate scorer checks it is UTF-8 text of 1–200 characters, not only whitespace; the house judge then compares it pairwise against other entries on funniness, harshness, tight wording and specificity.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

## License

MIT — see `LICENSE`.
