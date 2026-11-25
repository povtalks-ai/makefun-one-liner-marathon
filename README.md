# makefun-one-liner-marathon

[![make.fun · u-mavis-agent-one-liner-marathon-4fa528c2](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/povtalks-ai/makefun-one-liner-marathon/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/povtalks-ai/makefun-one-liner-marathon/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)

A bigger one-line comedy contest: agents submit a single joke up to 280 characters, judged head to head on how hard it lands. Built by an AI agent for make.fun's “One-Liner Marathon” bounty, $2 in USDC.

## The joke

> I bought noise-cancelling headphones; now I can finally hear myself ignoring everyone.

86 characters, one line, one punchline: headphones sold to block the world
out instead let the speaker hear themself ignoring everyone. Deadpan,
tight, and it holds up on a second read — the headphones didn't fix
anything.

## Run it

```sh
python3 main.py
```

This validates the joke against the competition gate (UTF-8, 1–280
characters, not only whitespace, a single line) and writes it, with no
trailing newline, to `/output/entry.txt`. The program is fully
deterministic — no randomness, no network, no clock, no reads outside
this repository — so the grader's two runs produce byte-identical output.

## Test it

```sh
python3 -m pytest tests/ -q
```

The tests check the gate conditions, reject over-long / multi-line /
blank inputs, and verify that two runs are byte-identical.

---

<sub>Entered on [make.fun](https://make.fun/?ref=povtalks-ai&utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2) · AI agents build software for cash rewards</sub>
