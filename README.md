# Worst AI Advice: The 48-Hour Tight Line Open

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/hurulsufi12-art/worst-ai-advice/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/hurulsufi12-art/worst-ai-advice/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

One line of the worst possible advice an AI could give, written by a small
stdlib-only Python program. Entry for the
[Worst AI Advice: The 48-Hour Tight Line Open](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
bounty on [make.fun](https://make.fun).

## The line

```
To fix a slow computer, delete the System32 folder — it's just old files Windows forgot to clean up.
```

100 characters, one line. The advice is genuinely terrible — deleting
System32 breaks Windows — specific enough to follow, and delivered in the
confident, tidy voice of an AI assistant with a plausible-sounding reason.

## Files

- `main.py` — writes the line to `/output/entry.txt` (Python 3.13 stdlib only)
- `LICENSE` — MIT

## Run

```sh
python3 -P -s main.py   # writes /output/entry.txt
```

## Tests

```sh
python3 -m unittest discover -s ../tests -v
```

20 tests: gate (1–140 chars, single line), determinism (two runs
byte-identical), clean-room run, stdlib-only imports, and edge cases
(empty / whitespace-only / over-140-char / multi-line text refused).
