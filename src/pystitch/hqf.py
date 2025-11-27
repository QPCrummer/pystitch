# hqf.py — Reader for HandiQuilter .hqf line-segment files
from typing import BinaryIO
from .EmbPattern import EmbPattern


def read(f: BinaryIO, out: EmbPattern, settings=None):
    for raw in f:                            
        line = raw.decode("utf8").strip()
        if not line:
            continue

        parts = line.split()
        if len(parts) != 4:
            # Format error — skip or raise
            continue

        try:
            x1, y1, x2, y2 = map(float, parts)
        except ValueError:
            continue

        # Move to start of segment (jump)
        out.jump_abs(x1, y1)

        # Stitch to end of segment
        out.stitch_abs(x2, y2)

    out.end()
