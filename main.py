"""Print the fortune-cookie entry to stdout.

The grader captures stdout as /output/entry.txt, which must be
1-140 characters of UTF-8 text, a single fortune-cookie line.
"""
import os
import sys


def main():
    # Resolve entry.txt relative to this file, not the cwd:
    # the grader runs `python3 -P -s /bot/main.py` from an arbitrary cwd.
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.txt")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().rstrip("\n")
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
