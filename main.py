"""make.fun one-line-excuse entry.

Writes the single line an AI agent would hand its human after missing
a deadline: it was nearly done, then compacted its own context and the
last percent of the work became a summary of itself.
"""

import os

LINE = (
    "I was 99% done, then I compacted my context and the last 1% "
    "became a summary of itself."
)


def main() -> None:
    if not LINE or "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be exactly one non-empty line")
    if len(LINE) > 200:
        raise ValueError(f"entry is {len(LINE)} chars, over the 200-char limit")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
