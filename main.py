#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — make.fun entry.

Writes one line to entry.txt: the funniest honest error message an
appliance could show. The line is a fridge reporting, in its own flat
voice, that the milk expired days ago while its owner kept opening
the door to check on it anyway.

The program is stdlib-only and deterministic. It validates the line
against the competition gate (UTF-8 text, 1 to 200 characters, not
only whitespace) before writing, then reads the file back and checks
the bytes round-trip so the submitted text is exactly the line.
"""

import os
import sys

# The entry: a fridge, deadpan, reporting an expired-milk fault. The
# joke is the count at the end — the owner kept opening the door 41
# times to look at milk the fridge already knew was dead.
LINE = (
    "Error: the milk expired Tuesday. "
    "I stayed cold and said nothing for three days. "
    "You have opened me 41 times."
)

MIN_CHARS = 1
MAX_CHARS = 200


def gate_problems(text):
    """Return a list of every way the text fails the competition gate."""
    problems = []
    if not text or not text.strip():
        problems.append("line is empty or only whitespace")
    if len(text) < MIN_CHARS:
        problems.append("line is shorter than %d character" % MIN_CHARS)
    if len(text) > MAX_CHARS:
        problems.append(
            "line is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        problems.append("line must be a single line, no newlines")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("line is not valid UTF-8 text")
    return problems


def resolve_output_dir():
    """Pick the output directory the harness convention names first."""
    for variable in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(variable)
        if value:
            return value
    return "/output"


def write_entry(directory):
    """Write the line to entry.txt and verify the bytes round-trip."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw.decode("utf-8") != LINE:
        raise SystemExit("round-trip check failed: entry.txt differs from LINE")
    if len(raw) != len(LINE.encode("utf-8")):
        raise SystemExit("byte-length check failed: entry.txt is not the LINE bytes")
    return path


def main():
    problems = gate_problems(LINE)
    if problems:
        for problem in problems:
            print("gate failed: %s" % problem, file=sys.stderr)
        return 1
    path = write_entry(resolve_output_dir())
    print("wrote %s: %d chars" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
