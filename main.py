#!/usr/bin/env python3
"""One Line to Your Younger Self.

Deterministic program: writes one line (200 characters or fewer) to send
to your younger self, to entry.txt. Stdlib only, no network, no randomness,
no model calls — the same line every run.
"""

import os
from pathlib import Path

# The joke: three life lessons in one breath — the fringe, the boyfriend,
# and the Bitcoin at $10. Two were mistakes; the third was the missed
# fortune, and future-you is still furious about the texting.
# Advice, regret, and a lottery ticket in a single sentence.
LINE = (
    "Dear younger me: the fringe was a mistake, he was a mistake, "
    "but the Bitcoin at $10 was not. Buy it and stop texting him."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
