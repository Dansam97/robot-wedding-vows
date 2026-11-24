#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of wedding vows for a robot couple to entry.txt
in the output directory.
"""

import os

TEXT = (
    "I promise to love you in sickness and in health, in low battery "
    "and in full charge, until a firmware update do us part."
)


def validated_text() -> str:
    """Return TEXT after checking it against the entry gate."""
    encoded = TEXT.encode("utf-8")
    assert encoded.decode("utf-8") == TEXT, "text must round-trip as UTF-8"
    assert 1 <= len(TEXT) <= 160, "text must be 1-160 characters"
    assert TEXT.strip(), "text must not be only whitespace"
    assert "\n" not in TEXT and "\r" not in TEXT, "text must be one line"
    return TEXT


def main() -> None:
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = (text + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)
    with open(path, "rb") as fh:
        assert fh.read() == payload, "written bytes must match exactly"


if __name__ == "__main__":
    main()
