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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
