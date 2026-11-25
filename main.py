"""Snooze Button Roast — make.fun entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to /output/entry.txt. Python standard library only.
"""

import os

ENTRY = "At 6 a.m. Saturday my alarm clock rang like a smug employee filing for overtime, so my wife fired it, boxed it, and mailed it to Monday."


def check_entry(entry):
    """Validation guard: entry is 1-200 chars, UTF-8, not only whitespace."""
    if not isinstance(entry, str):
        raise ValueError("entry must be a string")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(entry)}")
    entry.encode("utf-8")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    return True


def confirm_written(entry, path):
    """Read-back guard: re-open the written file and confirm it byte-matches."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != entry:
        raise ValueError("written entry does not match the entry in memory")
    if not 1 <= len(written) <= 200:
        raise ValueError(f"written entry must be 1-200 characters, got {len(written)}")
    if "\n" in written or "\r" in written:
        raise ValueError("written entry must be a single line")
    return True


def main():
    check_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    confirm_written(ENTRY, "/output/entry.txt")


if __name__ == "__main__":
    main()
