# HqfReader.py
from typing import TextIO
from .EmbPattern import EmbPattern

TENTH_MM_PER_INCH = 254

def read(f: TextIO, out: EmbPattern, settings=None):
    first_segment = True

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

        # Scale
        x1 *= TENTH_MM_PER_INCH
        y1 *= TENTH_MM_PER_INCH
        x2 *= TENTH_MM_PER_INCH
        y2 *= TENTH_MM_PER_INCH

        if first_segment:
            # Move to start only ONCE
            out.move_abs(x1, y1)
            first_segment = False
        else:
            # Continue stitching to next segment start
            out.stitch_abs(x1, y1)

        # Now stitch the segment
        out.stitch_abs(x2, y2)

    out.end()
