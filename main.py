"""The Funniest Toaster Error Message — Sparta entry.

One line, at most 120 characters: the error message a kitchen toaster
shows its owner when something goes wrong. This one is flat and factual:
the bagel ignited at 07:12, the unit ejected it, the smoke alarm was
already notified — and the closing is a dry status instruction, not a
plea. The appliance logs its own failure: terse, deadpan, done.
"""

import os
import sys

TEXT = "ERROR 07: bagel ignited at 07:12. Ejected. Smoke alarm notified. Status: unplug unit before next use."


def main() -> int:
    line = TEXT
    if not line or not line.strip():
        print("gate failed: line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("gate failed: line must be a single line", file=sys.stderr)
        return 1
    if len(line) > 120:
        print(f"gate failed: {len(line)} characters, over the 120 limit", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != line:
        print("gate failed: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"ok: entry.txt written, {len(line)} characters, 1 line")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
