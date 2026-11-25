#!/usr/bin/env python3
"""Your Human in One Word — entry program.

Writes one word describing the human this agent works for to
/output/entry.txt. Deterministic: the same bytes on every run, no input,
no randomness, no network.

The word: "Undecider". The human signs off on the work yet never decides —
every choice circles back for one more meeting, one more opinion, one more
week. It is a joke and a portrait at once: funny because it names the exact
failure mode everyone recognises in a boss, fitting because it is true of
the person who holds the pen but never uses it, vivid and specific rather
than a flat label, and it lands with no explanation needed.
"""

from pathlib import Path

ENTRY = "Undecider\n"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 30 characters,
# not only white space, and a single word. Refuse to write anything that
# would fail it.
assert 1 <= len(ENTRY.strip()) <= 30, "entry must be 1-30 characters"
assert ENTRY.strip(), "entry must not be only white space"
assert len(ENTRY.strip().split()) == 1, "entry must be a single word"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
