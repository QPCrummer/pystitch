# HqfReader.py
from typing import TextIO
from .EmbPattern import EmbPattern

TENTH_MM_PER_INCH = 254

def read(f: TextIO, out: EmbPattern, settings=None):
    for line in f:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        if len(parts) != 4:
            continue

        try:
            x1, y1, x2, y2 = map(float, parts)
        except ValueError:
            continue

        # Convert inches → tenths of mm (Pystitch internal units)
        x1 *= TENTH_MM_PER_INCH
        y1 *= TENTH_MM_PER_INCH
        x2 *= TENTH_MM_PER_INCH
        y2 *= TENTH_MM_PER_INCH

        # Move and stitch absolute
        out.move_abs(x1, y1)
        out.stitch_abs(x2, y2)

    out.end()
