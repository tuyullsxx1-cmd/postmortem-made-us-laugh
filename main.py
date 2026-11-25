"""One-line entry writer for The Postmortem That Made Us Laugh.

Writes the two-sentence agent disaster story to /output/entry.txt.
Standard library only.
"""

import os
from pathlib import Path

# Gate: /output/entry.txt must be 1-400 characters, one or two sentences.
# This story is 140 characters in two sentences, asked / did / broke.
LINE = "I asked it to make login faster. It cached every session as the admin's, so for eleven minutes every user was logged in as me, including me."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
