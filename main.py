#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes a single-line office joke (1-199 characters) to /output/entry.txt.
Standard library only, no network, deterministic.

The angle: not the stock Monday-morning or photocopier line. This one
roasts the reply-all thread — the person who tries to stop it becomes
its star. The turn lands at the end: the would-be hero of the inbox is
now the reason the thread exists at all.
"""
import os

JOKE = "I replied-all asking everyone to stop replying-all, and now I'm the star of a 47-email thread about replying-all."


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 199, f"joke is {len(text)} characters"
    assert "\n" not in text, "joke must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
