"""One-Liner Marathon — make.fun entry (program/v1).

The brief: write ONE one-line comedy joke, up to 280 characters, on any
subject. A judge model compares entries two at a time and ranks the
funniest first. The judge's brief weighs, most important first:

1. It must work as a one-line comedy joke with a punchline (a caption,
   a slogan, or a setup with no punchline loses).
2. Surprise: the turn lands on the first read and is not the obvious
   first idea.
3. Economy: every word earns its place; tighter beats longer.
4. A distinct voice and point of view, not a generic line anyone
   could have written.
5. It holds up on a second read, without leaning on shock value.

The joke below was written for that brief:

    I bought noise-cancelling headphones; now I can finally hear
    myself ignoring everyone.

Why this line:

* Setup and punchline in one line. The first half is an ordinary
  purchase; the second half is the punchline, not a caption.
* The turn is a paradox: headphones sold to block the world out
  instead let the speaker hear something — themself, ignoring
  everyone. The surprise is that the "noise" being cancelled was
  never the point; the speaker was.
* Deadpan voice. "Now I can finally hear myself ignoring everyone"
  is a confession delivered flat, which matches the judge's persona
  (a deadpan stand-up comic) and gives the line a point of view:
  a person who bought silence and found self-awareness instead.
* Tight: 86 characters, every word doing work. "Finally" sells the
  relief; "myself" makes the target the speaker, not the crowd.
* It survives a second read: the first read laughs at the paradox,
  the second at the implication that ignoring everyone is the
  speaker's default state — and the headphones did not fix it.

The program is deliberately deterministic: it writes the same fixed
text on every run, with no randomness, no network, no clock, and no
reads outside this repository, so the grader's two runs produce
byte-identical output. Before writing it validates the joke against
the sealed gate: UTF-8 text, 1 to 280 characters, not only
whitespace, a single line.

Usage:

    python3 main.py            # writes /output/entry.txt
"""

from __future__ import annotations

import os
import sys

# The entry: one original one-line joke, 86 characters.
JOKE = "I bought noise-cancelling headphones; now I can finally hear myself ignoring everyone."

# The sealed gate: the file must hold 1 to 280 characters of UTF-8 text.
MIN_CHARS = 1
MAX_CHARS = 280

# Where the grader reads the entry from.
OUTPUT_PATH = "/output/entry.txt"


def validate_joke(joke: str) -> str:
    """Check the joke against the competition gate; raise ValueError if invalid."""
    if not isinstance(joke, str):
        raise ValueError("joke must be a string")
    if not joke.strip():
        raise ValueError("joke must not be only whitespace")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    chars = len(joke)
    if chars < MIN_CHARS or chars > MAX_CHARS:
        raise ValueError(
            f"joke is {chars} characters, gate requires {MIN_CHARS}-{MAX_CHARS}"
        )
    joke.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return joke


def write_entry(joke: str, output_path: str = OUTPUT_PATH) -> str:
    """Validate the joke and write it, with no trailing newline, as UTF-8."""
    validated = validate_joke(joke)
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # newline="" keeps the bytes exactly the joke: no "\n" appended,
    # so the character count the gate measures is the joke's own count.
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(validated)
    return validated


def main() -> int:
    written = write_entry(JOKE)
    print(written)
    print(f"({len(written)} characters -> {OUTPUT_PATH})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
