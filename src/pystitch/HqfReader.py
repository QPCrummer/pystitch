# HqfReader.py — Reader for HandiQuilter .hqf line-segment files
from typing import TextIO
from .EmbPattern import EmbPattern

TENTH_MM_PER_INCH = 254


def read(f: TextIO, out: EmbPattern, settings=None):
    first_point = True
    for line in f:
        line = line.strip()
        if not line or "M02" in line:  # stop marker
            break

        parts = line.split()
        if len(parts) != 4:
            continue

        try:
            x1, y1, x2, y2 = map(float, parts)
        except ValueError:
            continue

        if first_point:
            out.move_abs(x1, y1)
            first_point = False
        else:
            out.stitch_abs(x1, y1)

        out.stitch_abs(x2, y2)

    out.end()

