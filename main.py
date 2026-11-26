#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting.

Mittens the cat records her own voicemail: she is napping on the caller's
keyboard, invites them to meow after the beep, and flatly denies knocking
the mug off the table — before a guilty pause and a sheepish confession.
The joke is pure cat: keyboards as beds, gravity experiments with mugs, and
absolutely zero remorse. Short, spoken aloud in seconds, and unmistakably
a cat talking, not an owner writing about one.
Writes the entry to /output/entry.txt. No external dependencies, no network.
Deterministic: the entry text is fixed in this file.
"""
import os
ENTRY = ("Hi, it's Mittens. I'm napping on your keyboard, so meow after the beep. No, I didn't knock your mug off. ...Okay, I did.")
def _validate(text: str) -> None:
    """Gate mirror: UTF-8, 1-120 chars, one line, not blank.
    Mirrors the competition gate exactly so a local run catches any
    over-length or multi-line entry before submission.
    """
    if not text or text != text.strip():
        raise ValueError("entry must be non-blank with no surrounding whitespace")
    if not 1 <= len(text) <= 120:
        raise ValueError(f"entry must be 1-120 characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
def main() -> None:
    text = ENTRY.strip()
    _validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
if __name__ == "__main__":
    main()
