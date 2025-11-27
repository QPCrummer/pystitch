from typing import TextIO
from .EmbPattern import EmbPattern


def read(f: TextIO, out: EmbPattern, settings=None):
    print("Hqf Test")
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

        if first_segment:
            # Move to the start of the first segment
            out.move_abs(x1, y1)
            first_segment = False
        else:
            # Stitch to the start of the segment
            out.stitch_abs(x1, y1)

        # Stitch to the end of the segment
        out.stitch_abs(x2, y2)

    out.end()
