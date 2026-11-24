"""Worst AI Advice — entry program.

Writes one line of the worst possible advice an AI could give (100
characters) to /output/entry.txt. Stdlib only, deterministic, no network,
no model calls.
"""
import os

TEXT = (
    "To fix a slow computer, delete the System32 folder \u2014 "
    "it's just old files Windows forgot to clean up."
)


def main():
    # Enforce the scorer's gate (RULES.txt): UTF-8, 1-140 characters,
    # one single line, not whitespace-only. Fail loudly instead of
    # writing an invalid entry. Also refuse control characters: a stray
    # \x00-\x1f would fail the scorer's UTF-8 text check.
    if not 1 <= len(TEXT) <= 140 or "\n" in TEXT or not TEXT.strip():
        raise SystemExit("entry text violates the 1-140 char single-line gate")
    if any(ord(c) < 0x20 for c in TEXT):
        raise SystemExit("entry text contains a control character")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
