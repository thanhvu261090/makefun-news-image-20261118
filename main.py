#!/usr/bin/env python3
"""Entry for make.fun news-image-20261118: copy the front-page image to /output.

Standard library only. The image lives in the repository as entry.png; the
program just copies it to the output directory, so both grading runs write
exactly the same bytes. No network is used.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    """Copy entry.png into the output directory (default /output)."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
